# index.src.html에 Leaflet CSS와 데이터를 넣어 한 파일짜리 dist/index.html을 만든다.
import os
here = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: open(os.path.join(here, f), encoding="utf-8").read()
html = (rd("index.src.html")
        .replace("/*LEAFLET_CSS*/", rd("leaflet.css"))
        .replace("/*CLUSTER_CSS*/", rd("mc_MarkerCluster.css"))
        .replace("/*DATA*/", rd("data.js"))
        .replace("/*DISTRICTS*/", rd("districts.json"))
        .replace("/*RIVERS*/", rd("rivers.json")))
os.makedirs(os.path.join(here, "dist"), exist_ok=True)
open(os.path.join(here, "dist", "index.html"), "w", encoding="utf-8").write(html)
print("dist/index.html", len(html.encode()), "bytes")
