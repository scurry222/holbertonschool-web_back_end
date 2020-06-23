#!/usr/bin/env python3
""" 9. Insert a document in Python
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ Lists all documents in a collection """
    return mongo_collection.insert_one(kwargs).inserted_id
