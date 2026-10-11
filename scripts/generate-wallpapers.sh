#!/usr/bin/env bash
# Gera wallpapers do tema Joinville com o image_gen embutido do Codex CLI
# (usa a conta ChatGPT do Codex; não precisa de OPENAI_API_KEY).
#
# Uso: scripts/generate-wallpapers.sh [nome ...]
#   sem argumentos: gera todos os prompts de docs/prompts/NN-*.txt que ainda
#   não têm imagem em backgrounds/. Ex.: scripts/generate-wallpapers.sh 01-colon-1851
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
mkdir -p backgrounds output/logs

if (($#)); then
  names=("$@")
else
  names=()
  for p in docs/prompts/[0-9][0-9]-*.txt; do
    n="$(basename "$p" .txt)"
    [[ -e "backgrounds/$n.png" ]] || names+=("$n")
  done
fi

for n in "${names[@]}"; do
  prompt="docs/prompts/$n.txt"
  out="backgrounds/$n.png"
  [[ -f "$prompt" ]] || { echo "sem prompt: $prompt" >&2; exit 1; }
  if [[ -e "$out" ]]; then
    out="backgrounds/$n-v$(date +%H%M%S).png" # nunca sobrescreve uma imagem aprovada
  fi
  echo ">> $n -> $out"
  {
    echo "Use the built-in image_gen tool (not the CLI fallback) to generate exactly ONE"
    echo "landscape 16:9 desktop wallpaper from the specification below, at the largest"
    echo "16:9 size the built-in tool supports. Do not augment the creative content."
    echo "Then copy the generated PNG to: $out"
    echo "Do not create or modify any other file. Reply with the saved path only."
    echo
    cat "$prompt"
  } | codex exec -s workspace-write --skip-git-repo-check - >"output/logs/$n.log" 2>&1 \
    || { echo "falhou: $n (veja output/logs/$n.log)" >&2; continue; }
  if [[ -f "$out" ]]; then
    magick identify -format "   %wx%h %b\n" "$out"
  else
    echo "   nenhuma imagem salva; veja output/logs/$n.log" >&2
  fi
done
