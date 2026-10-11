"""Valida os wallpapers e regrava docs/backgrounds.json (Python 3.11+, ImageMagick)."""
import hashlib,json,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[1]
prompts={p.stem:p for p in (root/'docs/prompts').glob('[0-9][0-9]-*.txt')}
items=[];problems=[]
for img in sorted((root/'backgrounds').glob('*.png')):
 w,h=map(int,subprocess.run(['magick','identify','-format','%w %h',str(img)],capture_output=True,text=True,check=True).stdout.split())
 stem=img.stem.split('-v')[0] if img.stem not in prompts else img.stem
 title=prompts[stem].read_text().splitlines()[0].removeprefix('Title: ') if stem in prompts else None
 if stem not in prompts:problems.append(f'{img.name}: sem prompt correspondente')
 if abs(w/h-16/9)>0.01:problems.append(f'{img.name}: {w}x{h} não é 16:9')
 if w<1600:problems.append(f'{img.name}: largura {w} < 1600')
 items.append({'title':title,'file':f'backgrounds/{img.name}','prompt':f'docs/prompts/{stem}.txt','width':w,'height':h,
  'native_4k':(w,h)==(3840,2160),'generator':'codex built-in image_gen','bytes':img.stat().st_size,
  'sha256':hashlib.sha256(img.read_bytes()).hexdigest()})
(root/'docs/backgrounds.json').write_text(json.dumps(items,indent=2,ensure_ascii=False)+'\n')
missing=sorted(set(prompts)-{Path(i['prompt']).stem for i in items})
print(f'{len(items)} wallpapers; faltando: {", ".join(missing) or "nenhum"}')
for p in problems:print('  !',p)
raise SystemExit(1 if problems else 0)
