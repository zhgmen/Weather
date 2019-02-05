# encoding:utf8
from pymongo import MongoClient


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

