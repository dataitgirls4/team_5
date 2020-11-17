import requests
import pandas as pd

api_key = "본인 API Key"

header = {
  "Authorization": api_key,
  "Accept": "application/vnd.api+json"
}

# tournaments 까지만 넣으면 토너먼트 아이디 얻을 수 있음(as-pcs3as)
url = "https://api.pubg.com/tournaments/as-pcs3as"


r = requests.get(url, headers=header)
leagues_pcs3as = r.json()
leagues_pcs3as


matchId_dict = {match['attributes']['createdAt']: match['id'] for match in leagues_pcs3as['included']}
matchId_dict

pcs3_matchId_df = pd.DataFrame(sorted(matchId_dict.items(), key=lambda x: x[0]), columns=['createdAt', 'matchId'])

pcs3_matchId_df
# 
pcs3_matchId_df.to_csv("pcs3-matchId.csv")

#
matches_pcs3_url = []
for m_id in pcs3_matchId_df['matchId']:
    url = f'https://api.pubg.com/shards/tournaments/matches/{m_id}'
    matches_pcs3_url.append(url)
    print(matches_pcs3_url)