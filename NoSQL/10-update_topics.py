#!/usr/bin/env python3
"""task 10"""

def update_topics(mongo_collection, name, topics):
  """create document"""
  query = {"name": name}
  newquery = {"$set": {"topics": topics}}
  mongo_collection.update_many(query, newquery)
