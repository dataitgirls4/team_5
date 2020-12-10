import requests
import pprint

# example: endpoint "telemetry"
# telemetry 데이터 불러와서 pprint로 depth별로 정리해서 확인하기

url =  "https://telemetry-cdn.pubg.com/bluehole-pubg/kakao/2020/11/11/06/32/b9ce6b56-23e7-11eb-a79a-bebdf03c2562-telemetry.json"
header = {
  "Authorization": "Personal API",
  "Accept": "application/vnd.api+json"
}
r = requests.get(url, headers=header)
json_r = r.json()

# warning! it's tooo big. 결과물의 행이 백만개가 넘습니다.
pprint.pprint(telemetry_sample, depth=15)
