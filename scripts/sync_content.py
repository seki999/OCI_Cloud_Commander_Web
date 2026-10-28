from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
root=Path(__file__).resolve().parents[1]
url='https://codeload.github.com/seki999/OCI_Cloud_Commander_Android/zip/refs/heads/main'
with urlopen(url,timeout=120) as response: archive=response.read()
with ZipFile(BytesIO(archive)) as z:
    files=[n for n in z.namelist() if '/content/' in n and not n.endswith('/')]
    levels=[n for n in files if '/content/chapters/' in n and n.endswith('.json')]
    assert len(levels)==30,f'Expected 30 actual levels, got {len(levels)}'
    for n in files:
        rel=n.split('/content/',1)[1];dest=root/'public'/'content'/rel
        dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(z.read(n))
print('Synced',len(levels),'levels and',len(files),'content assets')