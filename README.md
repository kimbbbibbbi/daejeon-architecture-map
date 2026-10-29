# 대전건축여지도

대전광역시 우수건축자산을 지도·목록·권역별 추천 동선으로 둘러보는 아카이브 웹사이트입니다.
UI는 오픈하우스서울(ohseoul.org) 지도 페이지를 참고했습니다.

> 현재는 샘플 데이터 25건입니다. 대전광역시 근현대 건축문화유산 전수조사 308건 데이터로 교체할 예정입니다.

## 페이지
- `#map` 전체 화면 지도 (필터, 검색, 목록 패널, 마커 클러스터)
- `#list` 전체목록 (`#era-joseon`, `#era-colonial`, `#era-postwar`, `#era-recent` 시대별)
- `#b01` … 건축자산 상세
- `#routes` 권역별 추천 동선
- `#about` 소개 · 데이터 출처
- `#links` 관련 사이트

## 파일
| 파일 | 내용 |
|---|---|
| `index.src.html` | 화면 구조 · 스타일 · 동작 원본 |
| `data.js` | 건축물 · 동선 데이터 (엑셀 반영 시 이 파일만 교체) |
| `districts.json` | 대전 5개 구 경계 (통계청 2013, southkorea-maps 가공) |
| `rivers.json` | 갑천 · 유등천 · 대전천 (© OpenStreetMap contributors) |
| `leaflet.css`, `mc_MarkerCluster.css`, `maplibre-gl.css` | 지도 라이브러리 스타일 |
| `build.py` | 위 파일을 합쳐 `index.html` 한 파일로 만듦 |
| `index.html` | 빌드 결과물 (바로 열어 볼 수 있음) |

## 빌드
```bash
python3 build.py
```

## 배포
`index.html` 한 파일이면 됩니다. GitHub Pages(Settings → Pages → main 브랜치 / root)로 켜면
OpenFreeMap 배경 지도(가게·건물 이름 표시)가 자동으로 나옵니다.

## 출처
- 건축물 좌표 · 하천: © OpenStreetMap contributors (ODbL)
- 행정구역 경계: 통계청, southkorea-maps
- 배경 지도: OpenFreeMap © OpenMapTiles, Data from OpenStreetMap
- 라이브러리: Leaflet, Leaflet.markercluster, MapLibre GL, maplibre-gl-leaflet

기획 · 제작: 서광일 · 디지털인문학 프로젝트
