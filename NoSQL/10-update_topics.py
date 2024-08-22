#!/usr/bin/env python3

"""The file update_topics"""


def update_topics(mongo_collection, name, topics):
    """updates the document"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
