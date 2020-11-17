#!/usr/bin/env python
# coding: utf-8

# # 선수 데이터 뽑아오기 / GRF 선수 ID : 2tap

# ## player 정보 불러오기

# In[1]:


import pandas as pd 
import requests

url = "https://api.pubg.com/shards/steam/players?filter[playerNames]=GRF_2tap"

header = {
  "Authorization": "your ip",
  "Accept": "application/vnd.api+json"
}

p = requests.get(url, headers=header)
player_GRF_2tap = p.json()
player_GRF_2tap


# ## matches 정보 불러오기

# In[2]:


import requests
url = "https://api.pubg.com/shards/kakao/matches/ae1c96e4-8f39-4025-a926-ddf227045919"   # 첫 번째 match

header = {
  "Authorization": "your ip",
  "Accept": "application/vnd.api+json"
}

m = requests.get(url, headers=header)
matches_GRF_2tap = m.json()
matches_GRF_2tap 


# 출력된 모습이 딕셔너리 안에 딕셔너리가 있는 구조. 이런걸 서브 딕셔너리라고 한다 
# 
# ## 서브 딕셔너리 출력해서 데이터프레임 만들기

# In[3]:


# 딕셔너리 키 값 모두 출력하는 코드  
# links랑 meta는 필요없음 

print(matches_GRF_2tap.keys())


# In[4]:


# 특정 서브 딕셔너리 키 값 출력 - data 는 경기 id를 의미한다. 

matches_GRF_2tap_data = matches_GRF_2tap['data']
df = pd.DataFrame(matches_GRF_2tap_data)
df


# In[5]:


# 특정 서브 딕셔너리 키 값 출력 - included는 경기 세부 데이터 
matches_GRF_2tap = matches_GRF_2tap['included']
df1 = pd.DataFrame(matches_GRF_2tap)
df1


# In[ ]:




