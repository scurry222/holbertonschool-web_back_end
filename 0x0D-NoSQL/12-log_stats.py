#!/usr/bin/env python3
""" 12. Log stats
"""

from pymongo import MongoClient


def log_stats():
    """ Provide stats about nginx logs stored in MongoDB """
    m_client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = m_client.logs.nginx
    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    print("\tmethod GET: {}".format(
        nginx_collection.count_documents({"method": "GET"})
    ))
    print("\tmethod POST: {}".format(
        nginx_collection.count_documents({"method": "POST"})
    ))
    print("\tmethod PUT: {}".format(
        nginx_collection.count_documents({"method": "PUT"})
    ))
    print("\tmethod PATCH: {}".format(
        nginx_collection.count_documents({"method": "PATCH"})
    ))
    print("\tmethod DELETE: {}".format(
        nginx_collection.count_documents({"method": "DELETE"})
    ))
    print("{} status check".format(
        nginx_collection.count_documents({"method": "GET", "path": "/status"})
    ))

if __name__ == "__main__":
    log_stats()
