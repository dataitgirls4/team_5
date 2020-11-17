#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests

url = "https://api.pubg.com/shards/kakao/players?filter[playerNames]=de_javu_" 

header = {
  "Authorization": "Personal_API",
  "Accept": "application/vnd.api+json"
}

r = requests.get(url, headers=header)


# In[11]:


r.text


# In[12]:


url =  "https://api.pubg.com/shards/kakao/matches/24a26a10-ae7f-4cba-a717-f2b00465393e" 
header = {
  "Authorization": "Personal_API",
  "Accept": "application/vnd.api+json"
}

r = requests.get(url, headers=header)
json=r.json()
#df=pd.DataFrame(json)


# In[13]:


json


# In[ ]:




