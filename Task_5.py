import requests
import json
from bs4 import BeautifulSoup
url_list=[]
with open('1_task.json','r') as f:
    a=json.load(f)
for i in a:
    url_list.append(i['url'])
b=url_list[:50]
details=['name','director','image','description','language','genre',]
l=[]
for j in b:
    rel=requests.get(j)
    soup=BeautifulSoup(rel.content,"html.parser")
    con=soup.find('script',type='application/ld+json').text
    e=soup.find("li",attrs={"data-testid":"title-details-languages"}).a.get_text()
    h=json.loads(con)
    dic={}
    for k in h:
        dic['name']=h['name']
        dic['director']=h['director'][0]['name']
        dic['image']=h['image']
        dic['description']=h['description']
        dic["language"]=e
        dic['genre']=h['genre']
        dic['country']='india'
    l.append(dic)
with open('task5.json','w') as file:
    json.dump(l,file,indent=8)
