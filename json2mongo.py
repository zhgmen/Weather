# encoding:utf8
from pymongo import MongoClient
import json

#os.chdir(os.getcwd()) #获取当前路径并设置工作目录

host = 'localhost'
port = 27017
client = MongoClient(host,port=port)
db = client['city-code']
posts = db['city']

#城市代码存入 mongopy数据库
with open('city_code.txt') as file:
  s = file.read()

select = json.loads(s)
for province in select['zone']:
  for city in province['zone']:
    for town in city['zone']:
      posts.insert_one(town)

client.close()
'''
def getcode(name):
  host = 'localhost'
  port = 27017
  client = MongoClient(host,port=port)
  db = client['city-code']
  posts = db['city']
  return posts.find_one({"name": name})['code']
  client.close()

if __name__ == "__name__":
  print getcode("北京")

'''



    


#s = json.dumps(s,ensure_ascii=False)
#selector = json.loads(s)

#data = selector['zone'][0]['zone'][0]['zone'][0]
#posts.insert_one(data)

#print posts.delete_one({"name" :u"赣榆"})

#print u"赣榆".encode('unicode')
#print unicode(u"赣榆","utf-8")

#print posts.find_one({"id":"191003"}).dumps(ensure_ascii=False)
#print json.dumps(data,ensure_ascii=False)     
        
#data = json.dumps(data,ensure_ascii=False)
