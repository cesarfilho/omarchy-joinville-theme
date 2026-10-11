# Plano — Omarchy Theme **Joinville** (SC)

Tema escuro inspirado em Joinville: a noite azul da Baía da Babitonga e da
bandeira municipal, o ouro do brasão, a madeira do enxaimel, o verde das
palmeiras imperiais e o brilho do metal fundido da "Manchester Catarinense".

---

## 1. Pesquisa — o que define Joinville

| Eixo | Fatos | Como vira tema |
|---|---|---|
| **Símbolos** | Bandeira: campo **azul** com losango **branco** e o brasão no centro (Lei 617/1963). Brasão: quartéis azuis com ouro (flor-de-lis de Orléans, besantes de Bragança), cruz suíça branca em vermelho, leão norueguês dourado, águia; **roda dentada dourada** (indústria) no listel vermelho. | Base azul-noite + texto branco-quente; **accent dourado**; vermelho heráldico. |
| **História** | Fundada em 9/3/1851 como **Colônia Dona Francisca** (barca *Colon*, 191 imigrantes suíços, alemães e noruegueses). Dote da princesa Francisca ao Príncipe de Joinville → "Cidade dos Príncipes". | Nome de paleta/wallpaper "Colon 1851"; tons de pergaminho no foreground. |
| **Arquitetura** | Casas **enxaimel** centenárias (vigas escuras, reboco claro, telhado vermelho); Palácio dos Príncipes (Museu Nacional de Imigração); **Rua das Palmeiras** (palmeiras imperiais de ~1873). | `brown` = madeira; `red` = telha; `green` = palmeiras. Bordas de janela em "viga" (2px, cantos retos). |
| **Natureza / clima** | Cidade plana (~4 m), à beira da **Baía da Babitonga**, manguezais, Mata Atlântica, Serra do Mar ao fundo; chuva o ano todo (~1.900 mm/ano). | `cyan` = mangue/baía; wallpaper de neblina/chuva na serra. |
| **Cultura** | **Festival de Dança** (maior do mundo, julho); **Escola do Teatro Bolshoi** (única fora da Rússia); **Festa das Flores** (orquídeas, novembro) → "Cidade das Flores"/"Cidade da Dança"; Joinville Jazz Festival; Cidadela Cultural Antarctica. | `magenta` = orquídea; wallpaper do palco/Centreventos; possível variante clara "Festa das Flores". |
| **Lazer / gastronomia** | Cervejarias (Moinho/Pórtico com Opa Bier), cucas, apfelstrudel, melado; Rua Visconde de Taunay; Mirante; Parque da Caieira (sambaquis); **Cidade das Bicicletas** (Museu da Bicicleta, 16 mil peças). | `yellow` âmbar = cerveja; ícone/glyph de bicicleta no README/preview. |
| **Indústria / comércio** | Maior PIB e polo metal-mecânico de SC: **Tupy** (fundição), Whirlpool, Nidec/Embraco, Tigre, Schulz, Krona, Ciser, Döhler, Totvs; ferramentaria, plásticos, software. | `orange` = **aço em fusão** (fundição); estética de chão de fábrica no wallpaper industrial. |
| **Esporte** | JEC (futebol e futsal, Centreventos Cau Hansen), vôlei. | **Fora do tema** (decisão). |

---

## 2. Conceito visual

**"Babitonga à noite"** — modo `dark`. O fundo é o azul da bandeira escurecido
até a hora azul sobre a baía; o texto é o branco do losango aquecido como reboco
de enxaimel; o destaque é o ouro do brasão. As cores ANSI contam a cidade:

| Slot | Hex (rascunho) | Origem |
|---|---|---|
| `background` | `#0f1a2a` | Azul da bandeira, noite na baía |
| `dark_background` / `darker_background` | `#0b1421` / `#070d16` | Mangue à noite |
| `lighter_background` | `#18263a` | Superfícies (barra, menus) |
| `foreground` | `#eeeae0` | Losango branco / reboco enxaimel |
| `light_foreground` / `bright_foreground` | `#d9d4c8` / `#ffffff` | |
| `dark_foreground` / `muted` | `#8593a8` | Névoa da Serra do Mar |
| `accent` / `yellow` | `#e0b043` | Ouro do brasão (flor-de-lis, coroa, roda dentada) |
| `selection` | `#1f4e8c` | Azul heráldico |
| `red` | `#e46f57` | Telha / cruz suíça |
| `orange` | `#e8833a` | Ferro em fusão (Tupy) |
| `green` | `#62a86d` | Palmeiras imperiais / Mata Atlântica |
| `cyan` | `#4fb8b4` | Águas da Babitonga |
| `blue` | `#5b93dc` | Céu sobre a baía |
| `magenta` | `#c876bb` | Orquídeas da Festa das Flores |
| `brown` | `#c28c60` | Madeira do enxaimel |
| `bright_*` | `#ec8470` `#f2cd6b` `#86c890` `#7fd6d1` `#8ab4ec` `#e19ad6` | Versões claras |

Contraste já pré-checado (WCAG): foreground 14.5:1 no fundo, 6.9:1 na seleção;
todas as cores ≥ 4.5:1 no `background` e no `lighter_background`.

---

## 3. Wallpapers — pixel art no estilo `1800` (10 × 3840×2160)

Ilustração própria em *painterly pixel art*, ancorada na paleta. Prompts completos em
[`docs/prompts/`](docs/prompts/); cada um repete o bloco de estilo compartilhado.

| # | Cena | Hora / clima | Eixo |
|---|---|---|---|
| 01 | Barca *Colon* chegando pela Babitonga (1851) | amanhecer com névoa | história |
| 02 | Rua das Palmeiras → Palácio dos Príncipes | hora azul pós-chuva | símbolo |
| 03 | Casa enxaimel na Estrada Bonita | garoa matinal | arquitetura |
| 04 | Rio Cachoeira, centro c. 1900 | noite chuvosa | cidade |
| 05 | O Moinho e canteiros de flores | fim de tarde | lazer |
| 06 | Orquídeas na Festa das Flores | luz úmida de estufa | cultura |
| 07 | Noite de Dança — palco de balé | noite, spot único | cultura |
| 08 | Fundição — ferro em fusão | escuro + laranja | indústria |
| 09 | Turno de bicicleta — operários indo à fábrica | manhã com névoa | comércio/indústria |
| 10 | Mirante — Babitonga à noite | hora azul | natureza |

Extra: `unlock-monogram.txt` — emblema "JOINVILLE" com losango da bandeira para a tela de desbloqueio.

**Geração**: não há chave de API de imagem nesta máquina. Opções: `gpt-image` (como o `1800`),
outro gerador, ou gerar em 1536×864, aprovar e re-renderizar em 4K por *edit* com a imagem aprovada
como referência (o fluxo usado no `1800`). Registrar tudo em `docs/backgrounds.json`
(arquivo, prompt, modelo, sha256) e validar com `scripts/check-wallpapers.py`.

---

## 4. Estrutura de arquivos

```
omarchy-theme-joinville-sc/
├── colors.toml          # paleta acima (formato Omarchy 4)
├── shell.toml           # barra/controles opacos: bg #18263a, active #e0b043
├── icons.theme          # ex.: Yaru-blue
├── backgrounds/         # 01-colon-1851.png … 10-mirante-babitonga.png
├── docs/prompts/        # prompts de cada wallpaper + monograma
├── docs/backgrounds.json  # manifesto: prompt, modelo, sha256
├── scripts/
│   ├── check-theme.py   # contraste WCAG (adaptado do 1800)
│   └── check-wallpapers.py # 3840×2160, checksums, prompts presentes
├── preview.png          # screenshot do tema aplicado
└── README.md            # pt-BR: aplicar, paleta, créditos
```

Templates (`alacritty`, `kitty`, `ghostty`, `btop`, `neovim`, `vscode`, `hyprland`…)
são gerados pelo Omarchy a partir de `colors.toml` (`/usr/share/omarchy/default/themed/*.tpl`),
então **não precisamos escrevê-los à mão** — só sobrescrever se algum app ficar ruim.

---

## 5. Etapas

1. **Paleta** — criar `colors.toml` + `shell.toml`; rodar `check-theme.py` (falha < 4.5:1).
2. **Teste rápido** — `ln -s` em `~/.config/omarchy/themes/joinville` → `omarchy theme set joinville`;
   revisar terminal, btop, neovim, barra, lock screen, notificações.
3. **Ajustes finos** — bordas Hyprland (ativo = ouro, inativo = `#18263a`), seleção no nvim, diff no git.
4. **Wallpapers** — gerar rascunhos, aprovar composição, re-renderizar em 4K, registrar no manifesto.
5. **Unlock** — monograma transparente + `omarchy plymouth preview '#0F1A2A' '#EEEAE0' unlock.png preview-unlock.png`.
6. **README + preview** — screenshots, tabela de paleta com a "história" de cada cor, créditos.
7. **Publicação** — repo `omarchy-joinville-theme` (o instalador remove `omarchy-` e `-theme` → tema `joinville`) no GitHub para instalar via `omarchy theme install <url>`.

### Extras opcionais
- Variante clara **"Festa das Flores"** (`mode = "light"`: fundo creme, accent orquídea).
- Wallpaper rotativo por estação/evento (julho = dança, novembro = flores).
- Esquema RGB de teclado (`keyboard.rgb`) em ouro.

---

## Decisões tomadas

- **Wallpapers**: pixel art no estilo `1800` (sem fotos).
- **Nome**: `joinville`.
- **Esporte**: JEC fora; nenhum escudo ou marca.

## Status (11/10/2026)

- [x] `colors.toml`, `shell.toml`, `icons.theme` (Yaru-blue-dark)
- [x] `scripts/check-theme.py` — 55 checagens, mínimo 4.83:1
- [x] 10 wallpapers gerados (Codex `image_gen`, 1672×941) e revisados visualmente
- [x] Monograma `unlock.png` + `preview-unlock.png`
- [x] `docs/palette.svg`, `docs/previews/`, `docs/backgrounds.json`, `preview.png`
- [x] README, LICENSE (MIT, com atribuição ao 1800), `.gitignore`
- [x] Testado no Omarchy (`omarchy theme set joinville`): terminal, bordas, barra
- [ ] Publicar no GitHub
- [ ] (opcional) Re-renderizar wallpapers em 3840×2160 via CLI com `OPENAI_API_KEY`

## Fontes

- [Wikipedia — Joinville](https://pt.wikipedia.org/wiki/Joinville)
- [FOTW — Bandeira e brasão de Joinville](https://crwflags.com/FOTW/FLAGS/br-sc137.html)
- [NSC Total — cidade das flores, dança, vôlei e cerveja](https://www.nsctotal.com.br/?p=7165488)
- [Catraca Livre — da dança à natureza](https://catracalivre.com.br/viagem-livre/da-danca-a-natureza-joinville-tem-atracoes-para-todos-os-gostos/)
- [Prefeitura — Pontos turísticos imperdíveis (PDF)](https://www.joinville.sc.gov.br/wp-content/uploads/2021/11/Pontos-Turísticos-Imperdíveis-de-Joinville.pdf)
- [NSC Total — economia e inovação](https://www.nsctotal.com.br/?p=2480946)
- [Smargiassi — Joinville/SC (empregadores)](https://smargiassi.com.br/sc/joinville/)
- [NSC Total — ruas mais antigas (Rua das Palmeiras)](https://www.nsctotal.com.br/?p=2419150)
- [Esse Mundo É Nosso — Pórtico e Moinho](https://www.essemundoenosso.com.br/?p=36172)
