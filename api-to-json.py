import json
import requests

api_key = "본인 API KEY"

header = {
  "Authorization": api_key,
  "Accept": "application/vnd.api+json"
}

url = "https://api.pubg.com/tournaments/as-pcs3as"

r = requests.get(url, headers=header)
r_data = r.json()
r_data

# dict 형태로 되어있는 데이터를 json 형식으로 바꿔주는 코드
load_data = json.dumps(r_data)

# 'tournaments_pcs3as.json' -> 저장할 파일명 지정
with open('tournaments_pcs3as.json', 'w') as make_file:
    json.dump(load_data, make_file, ensure_ascii=False)

# 작업 중인 이 파일이 있는 폴더에 가면 json 생성