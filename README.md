# instaHOTplace

crawlingData.py 와 crawlingDataCafe.py: 인스타 해시태그 페이지에서 데이터를 크롤링하는 코드.
crawlingdata.csv와 crawlingdataCafe.csv에 저장됨
Insta_explore.py: 익스플로어 탭에서 데이터를 크롤링해서 ex_crawlingdata.csv에 저장.

Clean.ipynb, Clean_explore.ipynb,csv_pretreatment.ipynb: 데이터 전처리 코드.

findName.ipynb, findName.py, gpt_extract.py: 이름 추출을 위한 코드.

addr_lat_log.ipynb: restaurant의 도로명 주소, 위도, 경도를 추출하는 코드
addr_lat_log_cafe.ipynb: cafe의 도로명 주소, 위도, 경도를 추출하는 코드
combine.ipynb: addr_lat_log.ipynb와 addr_lat_log_cafe.ipynb의 output들을 합치는 코드

navigation.ipynb: 제주도 도로망을 불러와 최종적으로 경로를 추천하는 코드.
Jeju_links.csv와 Jeju_nodes.csv를 통해 제주도 도로망을 만들고,
output.csv를 열어 음식점 및 카페의 정보를 저장하여 최종적으로 경로를 만들어 추천한다.
