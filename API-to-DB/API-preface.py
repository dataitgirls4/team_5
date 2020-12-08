import requests
import pandas as pd

# point 1 본인 API KEY
api_key = "본인 API Key"

header = {
  "Authorization": api_key,
  "Accept": "application/vnd.api+json"
}

# point 2 URL 파라미터 변경
url = "https://api.pubg.com/shards/tournaments/{match_id}" 

r = requests.get(url, headers=header)

# point 3 변수명 지정
변수명_지정 = r.json()
