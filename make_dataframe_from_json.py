## import & install list
import requests
import pprint as pp
import requests
import pandas as pd
#installation chicken-dinner module
# pip install chicken-dinner
#import chicken-dinner class
from chicken_dinner.models.tournament import Tournament
from chicken_dinner.pubgapi import PUBG
from chicken_dinner.pubgapi import PUBGCore

# needed variables
api_key = "personalAPI"

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
# FIRST TABLE
# match_info
match_id = []
created_at = []
map_name = []
duration = []
telemetry_link = []
# SECOND TABLE
# match_participant
player_id = []
team_roster_id = []
team_id = []
team_rank = []
match_id_2 = []
# match_participant_stats
participant_stats = []

## EXTRACTING 'FOR'
# for i in matchid_list :
for i in pcs3_matchId_df['matchId'] :
  # match_info
  # match_id, created_at, map_name, duration, telemetry_link
  match = PUBG.match(i)
  match_id.append(match.id)
  created_at.append(match.created_at)
  map_name.append(match.map_name)
  duration.append(match.duration)
  telemetry_link.append(match.telemetry_url)
  # match_participant
  # match_id, player_id, team_roster_id, team_rank, team_id
  rosters = match.rosters
  for i in range(len(rosters)):
    roster = rosters[i]
    roster_participant = roster.participants
    for i in range(len(roster_participant)):
      participant = roster_participant[i]
      match_id_2.append(match.id)
      player_id.append(participant.name)
      team_roster_id.append(roster.id)
      team_rank.append(roster.stats['rank'])
      team_id.append(roster.stats['team_id'])
      # match_participant_stats
      stats = participant.stats
      participant_stats.append(stats)

# MAKE DATAFRAME USING LISTS
match_info = pd.DataFrame({ 'match_id': match_id, 'created_at': created_at, 'map_name' : map_name, 'duration': duration, 'telemetry_link': telemetry_link})
match_participant = pd.DataFrame({'match_id': match_id_2, 'player_id': player_id, 'team_roster_id': team_roster_id, 'team_id': team_id, 'team_rank': team_rank})
match_participant_stats = pd.DataFrame(participant_stats).drop(columns='player_id')
#인덱스 기준으로 join
match_participant_all = pd.merge(match_participant, match_participant_stats, how='inner', left_index=True, right_index=True) 


# check the Dataframe
match_info
match_participant_all


#export csv
match_info.to_csv("/Users/kimheeji/Documents/데잇걸즈/gamedata/dataframe_output/pcs3_match_info.csv")
match_participant_all.to_csv("/Users/kimheeji/Documents/데잇걸즈/gamedata/dataframe_output/pcs3_match_participants.csv")
