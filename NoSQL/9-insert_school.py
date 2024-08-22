#!/usr/bin/env python3

"""This file contains insert_school function"""


def insert_school(mongo_collection, **kwargs):
    """inserts and returns the inserted id"""
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
