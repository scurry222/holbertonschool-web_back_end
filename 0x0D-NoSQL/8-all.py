#!/usr/bin/env python3
""" 8. List all documents in Python
"""
import pymongo


def list_all(mongo_collection):
    """ Lists all documents in a collection """
    return list(mongo_collection.find({})) if mongo_collection else []
