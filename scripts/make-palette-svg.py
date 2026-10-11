"""Gera docs/palette.svg a partir de colors.toml (Python 3.11+)."""
from pathlib import Path
import tomllib
root=Path(__file__).resolve().parents[1]
c=tomllib.loads((root/'colors.toml').read_text())
rows=[['background','lighter_background','foreground','accent','selection','muted'],
      ['red','orange','yellow','green','cyan','blue','magenta','brown']]
W,PAD,SW=1270,20,140
out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="300" viewBox="0 0 {W} 300">',f'<rect width="{W}" height="300" fill="{c["background"]}"/>']
for r,names in enumerate(rows):
 y=20+r*145
 for i,n in enumerate(names):
  x=PAD+i*(SW+15)
  out.append(f'<rect x="{x}" y="{y}" width="{SW}" height="76" rx="4" fill="{c[n]}" stroke="{c["muted"]}"/>'
   f'<text x="{x}" y="{y+100}" fill="{c["foreground"]}" font-family="sans-serif" font-size="12">{n}</text>'
   f'<text x="{x}" y="{y+120}" fill="{c["muted"]}" font-family="monospace" font-size="12">{c[n]}</text>')
out.append('</svg>')
(root/'docs/palette.svg').write_text('\n'.join(out)+'\n')
print('docs/palette.svg')
