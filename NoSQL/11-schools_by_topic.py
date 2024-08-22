#!/usr/bin/env python3

""" The function schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """returns a list"""
    return list(mongo_collection.find({"topics": topic}))
