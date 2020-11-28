import pandas as pd

from chicken_dinner.models.tournament import Tournament
from chicken_dinner.pubgapi import PUBG
from chicken_dinner.pubgapi import PUBGCore

api_key = 'PERSONAL API KEY'
PUBG = PUBG(api_key=api_key, shard='pc-tournament', gzip=True)
PUBGCore = PUBGCore(api_key=api_key, shard='pc-tournament', gzip=True)

id = pd.read_csv("tournaments_list.csv")
id = id['tournament_id']
id

# ''안에 아이디 하나씩 넣기
id_tor = 'kr-bsc20'

# 괄호에 아이디 하나씩 넣기 *22
tor = PUBG.tournament(id_tor)
matchlist = tor.match_ids

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


# EXTRACTING 'FOR'
#for i in matchid_list :
for i in matchlist :
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
#match_pariticpant
match_participant = pd.DataFrame({'match_id': match_id_2, 'player_id': player_id, 'team_roster_id': team_roster_id, 'team_id': team_id, 'team_rank': team_rank})

#match_participant_stats
match_participant_stats = pd.DataFrame(participant_stats).drop(columns='player_id')
match_participant_stats['team_name'] = match_participant.player_id.str.split('_').str[0]
match_participant_stats['player_name'] = match_participant.player_id.str.split('_').str[1]
match_participant_stats['player_name'] = [i.upper() for i in match_participant_stats['player_name']]

match_participant_stats = match_participant_stats.rename(columns={'name':'player_id'})

#인덱스 기준으로 join
match_participant_all = pd.merge(match_participant, match_participant_stats, how='inner', left_index=True, right_index=True)
match_participant_all = match_participant_all.rename(columns={'player_id_x': 'player_id'})

#[최종]matches_info
match_info = pd.DataFrame({'match_id': match_id, 'created_at': created_at, 'map_name' : map_name, 'duration': duration})

#[최종] result
tournament_id = pd.DataFrame({'tournament_id': [id_tor for i in range(len(match_participant_all))]})

match_participant_all = pd.merge(match_participant_all, tournament_id, how = "left", left_index=True, right_index=True)
result = pd.merge(match_participant_all, match_info, on = 'match_id', how='left').drop_duplicates()

result = result[['tournament_id', 'match_id', 'created_at', 'map_name', 'duration','team_rank', 'team_name', 'player_id', 'player_name', 'time_survived', 'death_type', 'kill_place', 'kills', 'dbnos', 'assists','damage_dealt', 'headshot_kills','longest_kill', 'road_kills', 'vehicle_destroys', 'weapons_acquired', 'boosts', 'heals', 'revives','ride_distance', 'swim_distance', 'walk_distance']].sort_values('created_at')

import pymysql
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()
import MySQLdb

# DB 연결정보 넣기
engine = create_engine("mysql+mysqldb://{User}:{Password}@{Host}:3306/{Database}}", encoding='utf-8')
conn = engine.connect()

tournament_id = result.loc[0, "tournament_id"]
table_name = f"matches_{tournament_id}"

result.to_sql(name=table_name, con=engine, if_exists='append', index=False)