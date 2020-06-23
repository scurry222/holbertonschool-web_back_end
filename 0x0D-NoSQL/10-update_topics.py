#!/usr/bin/env python3
""" 10. Change school topics
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """ Change all topics of a school document based on name """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
