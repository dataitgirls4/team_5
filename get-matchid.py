import requests
import pandas as pd

api_key = "your API Key"
header = {
  "Authorization": api_key,
  "Accept": "application/vnd.api+json"
}

# tournaments 까지만 넣으면 모든 토너먼트 아이디 얻을 수 있음
# 마지막에 토너먼트 아이디를 넣으면 해당 토너먼트의 데이터를 보여줌
url = "https://api.pubg.com/tournaments/as-pcs3as"


r = requests.get(url, headers=header)
json_r = r.json()

matchId_dict = {match['attributes']['createdAt']: match['id'] for match in json_r['included']}
matchId_dict

r_matchId_df = pd.DataFrame(sorted(matchId_dict.items(), key=lambda x: x[0]), columns=['createdAt', 'matchId'])

# 저장하기
r_matchId_df.to_csv("pcs3-matchId.csv")

#
matches_pcs3_url = []
for m_id in pcs3_matchId_df['matchId']:
    url = f'https://api.pubg.com/shards/tournaments/matches/{m_id}'
    matches_pcs3_url.append(url)
    print(matches_pcs3_url)
