#!/usr/bin/env python3
"""task 12"""
from pymongo import MongoClient
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school

if __name__ == "__main__":
  client = MongoClient("mongodb://127.9.9.1:27017")
  nginx_collection = client.logs.nginx
  print(f"{nginx_collection.count_documents({})} logs")
  print('Methods:')
  get = nginx_collection.count_documents({"method": "GET"})
  print(f"\tmethod GET: {get}")
  get = nginx_collection.count_documents({"method": "POST"})
  print(f"\tmethod POST: {get}")
  get = nginx_collection.count_documents({"method": "PUT"})
  print(f"\tmethod PUT: {get}")
  get = nginx_collection.count_documents({"method": "PATCH"})
  print(f"\tmethod PATCH: {get}")
  get = nginx_collection.count_documents({"method": "DELETE"})
  print(f"\tmethod DELETE: {get}")
  get = nginx_collection.count_documents({"method": "GET", "path": "/status"})
  print(f"{get} status check")
