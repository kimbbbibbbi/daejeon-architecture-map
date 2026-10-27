# index.src.html에 Leaflet CSS와 데이터를 넣어 한 파일로 합친다.
# dist/index.html: Claude 공유 링크용(문서 머리는 게시할 때 붙음)
# index.html: GitHub Pages용 완전한 HTML 문서
import os
here = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: open(os.path.join(here, f), encoding="utf-8").read()
body = (rd("index.src.html")
        .replace("/*LEAFLET_CSS*/", rd("leaflet.css"))
        .replace("/*CLUSTER_CSS*/", rd("mc_MarkerCluster.css"))
        .replace("/*DATA*/", rd("data.js"))
        .replace("/*DISTRICTS*/", rd("districts.json"))
        .replace("/*RIVERS*/", rd("rivers.json")))
os.makedirs(os.path.join(here, "dist"), exist_ok=True)
open(os.path.join(here, "dist", "index.html"), "w", encoding="utf-8").write(body)
page = ('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
        '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
open(os.path.join(here, "index.html"), "w", encoding="utf-8").write(page)
print("dist/index.html, index.html", len(page.encode()), "bytes")
