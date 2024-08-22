#!/usr/bin/env python3

"""
this module writes a script that
provides some stats about Nginx
"""

from pymongo import MongoClient

def nginx_stats():
    # Connect to the MongoDB server (assuming it's running locally)
    client = MongoClient('mongodb://localhost:27017/')

    # Access the 'logs' database and the 'nginx' collection
    db = client.logs
    nginx_collection = db.nginx

    # Count the total number of documents in the collection
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # List of HTTP methods to check
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("Methods:")
    for method in methods:
        # Count documents for each HTTP method
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Count the number of documents with method=GET and path=/status
    status_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

if __name__ == "__main__":
    nginx_stats()
