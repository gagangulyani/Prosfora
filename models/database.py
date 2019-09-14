import pymongo
from bson.json_util import dumps

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize(datab):
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client[datab]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return dumps(Database.DATABASE[collection].find(query))

    @staticmethod
    def count(collection, query={}):
        return Database.DATABASE[collection].count_documents(query)

    @staticmethod
    def delete(collection, query):
        return Database.DATABASE[collection].delete_one(query).deleted_count

    @staticmethod
    def delete_all(collection, query={}):
        return Database.DATABASE[collection].delete_many(query).deleted_count

    @staticmethod
    def update(collection, query, update_query):
        return Database.DATABASE[collection].update(query,
                                                    {"$set": update_query})

    @staticmethod
    def updateMany(collection, query, update_query):
        if update_query.get('$inc'):
            return Database.DATABASE[collection].update(query, update_query)

        return Database.DATABASE[collection].update_many(query,
                                                         {"$set": update_query})

    @staticmethod
    def created_at(_id):
        return _id.generation_time