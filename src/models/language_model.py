from .abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, dict):
        self.data = dict

    def to_dict(self):
        return {
            "name": self.data.get("name"),
            "acronym": self.data.get("acronym"),
        }

    @classmethod
    def list_dicts(clas):
        data = clas._collection.find()

        if not data:
            return []

        dicts_data = [
            {
                "name": dt.get("name"),
                "acronym": dt.get("acronym"),
                "_id": dt.get("_id"),
            }
            for dt in data
        ]

        return dicts_data
