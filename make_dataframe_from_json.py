## import & install list
import requests
import pprint as pp
import requests
import pandas as pd
#installation chicken-dinner module
pip install chicken-dinner
#import chicken-dinner class
from chicken_dinner.models.tournament import Tournament
from chicken_dinner.pubgapi import PUBG
from chicken_dinner.pubgapi import PUBGCore

# needed variables
api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyZTUxN2M3MC0wNzhkLTAxMzktNjA3My0xM2VlZDFhM2VmZGQiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjA1MjM3NjYyLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImRhdGFpdGdpcmxzIn0.TKzOoZ4svDG-sGFbMGv-uCV51jFsPAvSO0oU3nvgve4"

# PUBG / PUBGCore class를 토너먼트용 class로 custom!
PUBG = PUBG(api_key=api_key, shard='pc-tournament', gzip=True)
PUBGCore = PUBGCore(api_key=api_key, shard='pc-tournament', gzip=True)

# {as-pcs3as} 부분에 esports_tournaments_summary.csv의 tournament_id
url = "https://api.pubg.com/tournaments/as-pcs3as"
header = {
  "Authorization": api_key,
  "Accept": "application/vnd.api+json"
}
r = requests.get(url, headers=header)
tournament_pcs3as = r.json()
tournament_pcs3as

# 모든 match_id와 created_at을 꺼내주는 반복문
matchId_dict = {match['attributes']['createdAt']: match['id'] for match in tournament_pcs3as['included']}
matchId_dict
# 데이터프레임화
pcs3_matchId_df = pd.DataFrame(sorted(matchId_dict.items(), key=lambda x: x[0]), columns=['createdAt', 'matchId'])
# 모든 match id & createdat dataframe
pcs3_matchId_df

########################
# MATCH TABLE 만들기 시작 #
########################

## NEEDED LIST
# match_info
match_id = []
created_at = []
map_id = []
map_name = []
telemetry_link = []
# match_participant
player_name = []
player_won = []
team_roster_id = []
team_rank = []
team_id = []
team_won = []
match_id_2 = []
# match_participant_stats
participant_stats = []

## EXTRACTING 'FOR'
# for i in matchid_list :
for i in pcs3_matchId_df['matchId'] :
  # match_info
  # match_id, created_at, map_id, map_name, telemetry_link
  match = PUBG.match(i)
  match_id.append(match.id)
  created_at.append(match.created_at)
  map_id.append(match.map_id)
  map_name.append(match.map_name)
  telemetry_link.append(match.telemetry_url)
  # match_participant
  # match_id, player_name, player_id, roster_id, roster_rank, team_id, won, participant_won
  rosters = match.rosters
  for i in range(len(rosters)):
    roster = rosters[i]
    roster_participant = roster.participants
    for i in range(0,4):
      participant = roster_participant[i]
      player_name.append(participant.name)
      player_won.append(participant.won)
      team_roster_id.append(roster_participant[i].id)
      team_rank.append(roster.stats['rank'])
      team_id.append(roster.stats['team_id'])
      team_won.append(roster.stats['won'])
      match_id_2.append(match.id)
      stats = participant.stats
      # match_participant_stats
      participant_stats.append(stats)

# MAKE DATAFRAME USING LISTS
match_info = pd.DataFrame({ 'created_at': created_at, 'map_id': map_id, 'map_name' : map_id, 'telemetry_link': telemetry_link}, index=match_id)
match_participant = pd.DataFrame({'player_name': player_name, 'player_won': player_won, 'team_roster_id': team_roster_id, 'team_id': team_id, 'team_rank': team_rank, 'team_won': team_won}, index=match_id_2)
match_participant_stats = pd.DataFrame(participant_stats, index= match_id_2)

# check the Dataframe
match_info.to_excel('/Users/kimheeji/Documents/데잇걸즈/gamedata/sample_excel')
match_participant
match_participant_stats

# excel_export
import os
base_dir = "/Users/kimheeji/Documents/데잇걸즈/gamedata/"
file_nm = "sampledf.xlsx"
xlxs_dir = os.path.join(base_dir, file_nm)
with pd.ExcelWriter(xlxs_dir) as writer:
    match_info.to_excel(writer, sheet_name = 'match_info')
    match_participant.to_excel(writer, sheet_name = 'match_participant')
    match_participant_stats.to_excel(writer, sheet_name= 'match_participant_stats') 
