import pandas as pd
# import requests
from chicken_dinner.models.tournament import Tournament
from chicken_dinner.pubgapi import PUBG
from chicken_dinner.pubgapi import PUBGCore

api_key = "PERSONAL API"

PUBG = PUBG(api_key=api_key, shard='pc-tournament', gzip=True)
PUBGCore = PUBGCore(api_key=api_key, shard='pc-tournament', gzip=True)

id = pd.read_csv("tournaments_list.csv")
id = id['tournament_id']
id
# ''안에 아이디 하나씩 넣기
id_tor = 'as-pcs3as'

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

## EXTRACTING 'FOR'
# for i in matchid_list :
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

#[최종]match_info
match_info = pd.DataFrame({'match_id': match_id, 'created_at': created_at, 'map_name' : map_name, 'duration': duration, 'telemetry_link': telemetry_link})
match_toprank = match_participant_all.query('team_rank == 1')
match_toprank_list = match_toprank[['match_id', 'team_name']].rename(columns={'team_name':'winner'})
match_info = pd.merge(match_info, match_toprank_list, how = 'left', on = 'match_id')
tournament_id = pd.DataFrame({'tournament_id': [id_tor for i in range(len(match_info))]})
match_info = pd.merge(match_info, tournament_id, how = "left", left_index=True, right_index=True)
match_info = match_info[['tournament_id', 'match_id', 'created_at', 'map_name', 'duration', 'winner', 'telemetry_link', 'winner']]


#[최종]match_participant_all
tournament_id = pd.DataFrame({'tournament_id': [id_tor for i in range(len(match_participant_all))]})

match_participant_all = pd.merge(match_participant_all, tournament_id, how = "left", left_index=True, right_index=True)
match_participant_all = match_participant_all[['tournament_id','match_id', 'team_name', 'team_rank', 'player_id', 'player_name', 'kill_place', 'kills', 'dbnos', 'assists', 'damage_dealt', 'longest_kill', 'headshot_kills', 'road_kills','vehicle_destroys',  'boosts',  'death_type',  'heals',  'revives', 'ride_distance', 'walk_distance', 'swim_distance',  'weapons_acquired', 'team_kills', 'kill_streaks']]

# pip install SQLAlchemy
# pip install PyMySQL
import pymysql
from sqlalchemy import create_engine

# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

engine = create_engine("PERSONAL DB INFO", encoding='utf-8')
conn = engine.connect()

# MySQL에 저장하기
# pandas의 to_sql() 함수 사용 저장
tournament_id = match_info.loc[0, "tournament_id"]
table_name_1 = f"{tournament_id}_matches_info"
table_name_2 = f"{tournament_id}_matches_stats"

match_info.to_sql(name=table_name_1, con=engine, if_exists='append', index=False)
match_participant_all.to_sql(name=table_name_2, con=engine, if_exists='append', index=False)

