# 한 tournament의 모든 match_id와 created_at을 데이터프레임으로 만들어주는 코드

import requests
import pandas as pd

api_key = "your API Key"
header = {
  "Authorization": api_key,
  "Accept": "application/vnd.api+json"
}

# {as-pcs3as} 부분에 esports_tournaments_summary.csv의 tournament_id
url = "https://api.pubg.com/tournaments/as-pcs3as"

r = requests.get(url, headers=header)
json_r = r.json()
json_r

# 모든 match_id와 created_at을 꺼내주는 반복문
matchId_dict = {match['attributes']['createdAt']: match['id'] for match in json_r['included']}
matchId_dict

# 데이터프레임화
pcs3_matchId_df = pd.DataFrame(sorted(matchId_dict.items(), key=lambda x: x[0]), columns=['createdAt', 'matchId'])
pcs3_matchId_df
