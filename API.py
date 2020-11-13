#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests

url = "https://api.pubg.com/shards/kakao/players?filter[playerNames]=de_javu_" 

header = {
  "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyZTUxN2M3MC0wNzhkLTAxMzktNjA3My0xM2VlZDFhM2VmZGQiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjA1MjM3NjYyLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImRhdGFpdGdpcmxzIn0.TKzOoZ4svDG-sGFbMGv-uCV51jFsPAvSO0oU3nvgve4",
  "Accept": "application/vnd.api+json"
}

r = requests.get(url, headers=header)


# In[11]:


r.text


# In[12]:


url =  "https://api.pubg.com/shards/kakao/matches/24a26a10-ae7f-4cba-a717-f2b00465393e" 
header = {
  "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyZTUxN2M3MC0wNzhkLTAxMzktNjA3My0xM2VlZDFhM2VmZGQiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjA1MjM3NjYyLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImRhdGFpdGdpcmxzIn0.TKzOoZ4svDG-sGFbMGv-uCV51jFsPAvSO0oU3nvgve4",
  "Accept": "application/vnd.api+json"
}

r = requests.get(url, headers=header)
json=r.json()
#df=pd.DataFrame(json)


# In[13]:


json


# In[ ]:




