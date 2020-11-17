import requests
import pandas as pd

api_key = "본인 API-key"

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

matchId_df = pd.DataFrame(sorted(matchId_dict.items(), key=lambda x: x[0]), columns=['createdAt', 'matchId'])

matchId_df.to_csv("pcs3-matchId.csv")
