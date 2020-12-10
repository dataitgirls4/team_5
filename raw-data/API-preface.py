# chicken.dinner 라이브러리 사용하지 않고 가져올 때
# Change points

import requests
import pandas as pd

# point 1 your API KEY
api_key = "your API Key"

header = {
  "Authorization": api_key,
  "Accept": "application/vnd.api+json"
}

# point 2 change URL parameters
url = "https://api.pubg.com/shards/tournaments/{match_id}" 
r = requests.get(url, headers=header)

# point 3 now you can see the results
json_r = r.json()


### example ###

# Find info of "GEN_pio"

import requests

# 1. filter[playerNames]={playerName}
url = "https://api.pubg.com/shards/steam/players?filter[playerNames]=GEN_Pio"

# 2. players/{account Id}
# url = "https://api.pubg.com/shards/steam/players/account.e57c514acd19440bbc8a52233e482d93"

header = {
  "Authorization": "your API KEY",
  "Accept": "application/vnd.api+json"
}

r = requests.get(url, headers=header)
json_r = r.json()
json_r

# tip. you can get --
# 'id' - accountId (account.e57c514acd19440bbc8a52233e482d93)
# 'Match ID' - Used to lookup the full match object on the '/matches' endpoint
