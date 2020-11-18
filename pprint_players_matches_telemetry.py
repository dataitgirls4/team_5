# 필요한 모듈 import

import requests
import pprint

# players 데이터 불러와서 pprint로 depth별로 정리해서 확인하기
url = "https://api.pubg.com/shards/kakao/players?filter[playerNames]=de_javu_" 

header = {
  "Authorization": "Personal API",
  "Accept": "application/vnd.api+json"
}
r = requests.get(url, headers=header)
players_sample = r.json()
pprint.pprint(players_sample, depth=15)


# matches 데이터 불러와서 pprint로 depth별로 정리해서 확인하기
url =  "https://api.pubg.com/shards/kakao/matches/e35b54c0-973d-4378-b28e-6671dc071d22" 
header = {
  "Authorization": "Personal API",
  "Accept": "application/vnd.api+json"
}
r = requests.get(url, headers=header)
matches_sample=r.json()
pprint.pprint(matches_sample, depth=15)

# telemetry 데이터 불러와서 pprint로 depth별로 정리해서 확인하기

url =  "https://telemetry-cdn.pubg.com/bluehole-pubg/kakao/2020/11/11/06/32/b9ce6b56-23e7-11eb-a79a-bebdf03c2562-telemetry.json"
header = {
  "Authorization": "Personal API",
  "Accept": "application/vnd.api+json"
}
r = requests.get(url, headers=header)
telemetry_sample=r.json()
# warning! 결과물의 행이 백만개가 넘습니다.
pprint.pprint(telemetry_sample, depth=15)
