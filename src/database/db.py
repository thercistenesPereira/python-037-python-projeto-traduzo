from pymongo import MongoClient
from os import environ

MONGO_URI = environ.get("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = environ.get("DB_NAME", "test_db_traduzo")


def get_database(uri: str, db_name: str):
    client = MongoClient(uri)
    return client.get_database(db_name)


db = get_database(MONGO_URI, DB_NAME)
