import json
with open("task5.json","r") as file:
    data=json.load(file)
list1=[]
for i in data:
    if "director" in i:
        list1.append(i["director"])
i=0
b=[]
dict={}
while i<len(list1):
    if list1[i] not in b:
        b.append(list1[i])
        x=list1.count(list1[i])
        dict[list1[i]]=x
    i=i+1
with open("7_task.json","w") as f:
    json.dump(dict,f,indent=8)