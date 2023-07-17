# import requests
# import json
# from bs4 import BeautifulSoup
# rel=requests.get("https://www.imdb.com/title/tt0066763/")
# soup=BeautifulSoup(rel.text,"html.parser")
# con=soup.find('script',type='application/ld+json').text
# a=json.loads(con)
# dic={}
# for i in a:
#     if i=="url":
#         dic['id']=a[i]
# with open ("8_task.json","w") as file:
#     json.dump(dic,file,indent=8)