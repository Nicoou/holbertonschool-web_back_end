#!/usr/bin/env python3
"""task 8"""

def list_all(mongo_collection):
  """list all"""
  return [n for n in mongo_collection.find()]
