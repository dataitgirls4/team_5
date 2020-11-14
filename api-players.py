# 예시 playerName - GEN_pio

import requests

# 1. filter[playerNames]={playerName}
url = "https://api.pubg.com/shards/steam/players?filter[playerNames]=GEN_Pio"

# 2. players/{account Id}
# url = "https://api.pubg.com/shards/steam/players/account.e57c514acd19440bbc8a52233e482d93"

header = {
  "Authorization": "본인 API KEY",
  "Accept": "application/vnd.api+json"
}

r = requests.get(url, headers=header)
players_pio = r.json()
players_pio

# 알 수 있는 것
# 'id' - accountId (account.e57c514acd19440bbc8a52233e482d93)
# 'Match ID' - Used to lookup the full match object on the /matches endpoint (많음)