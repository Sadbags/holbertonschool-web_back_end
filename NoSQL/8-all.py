#!/usr/bin/env python3

"""This file contains list_all function"""


import pymongo


def list_all(mongo_collection):
    """lists all documents in collection"""
    return list(mongo_collection.find())
