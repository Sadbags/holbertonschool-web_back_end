#!/usr/bin/env python3

"""
this module writes a script that
provides some stats about Nginx
"""

from pymongo import MongoClient

def nginx_stats():
    # Connect to the MongoDB server (assuming default host and port)
    client = MongoClient('mongodb://localhost:27017/')

    # Access the 'logs' database and the 'nginx' collection
    db = client.logs
    nginx_collection = db.nginx

    # Total number of logs (documents)
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count documents for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Count documents where method is GET and path is /status
    status_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

if __name__ == "__main__":
    nginx_stats()
