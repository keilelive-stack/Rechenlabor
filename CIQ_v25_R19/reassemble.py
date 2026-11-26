from pathlib import Path
import hashlib,json,zipfile
p=Path(__file__).resolve().parent
m=json.loads((p/'MANIFEST.json').read_text());target=p/m['archive'];h=hashlib.sha256()
with target.open('wb') as out:
 for part in m['parts']:
  b=(p/part['file']).read_bytes()
  if len(b)!=part['bytes'] or hashlib.sha256(b).hexdigest()!=part['sha256']:raise ValueError(part['file'])
  out.write(b);h.update(b)
assert h.hexdigest()==m['sha256']
with zipfile.ZipFile(target) as z: assert z.testzip() is None
print('OK:',target)
