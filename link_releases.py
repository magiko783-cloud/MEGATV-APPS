"""After publishing APK files in a GitHub Release, build per-app download URLs.
Usage: python link_releases.py GITHUB_USERNAME REPOSITORY [TAG]
Example: python link_releases.py myname MEGATV-APPS v1
"""
import json, sys, pathlib
from urllib.parse import quote
if len(sys.argv)<3:
    print('Usage: python link_releases.py USERNAME REPOSITORY [TAG]'); raise SystemExit(2)
owner,repo=sys.argv[1:3]; tag=sys.argv[3] if len(sys.argv)>3 else 'v1'
root=pathlib.Path(__file__).resolve().parent
p=root/'apps.json'; data=json.loads(p.read_text(encoding='utf-8'))
for app in data:
    app['downloadUrl']=f'https://github.com/{quote(owner,safe="")}/{quote(repo,safe="")}/releases/download/{quote(tag,safe="")}/{quote(app["filename"),safe="")}'
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Prepared',len(data),'links; verify each GitHub Release file exists before Cloudflare deployment.')
