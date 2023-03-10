import pymongo

from dependency.database.database import DatabaseWrapper
import bson
import uuid

def generateUniqueId():
    return bson.Binary.from_uuid(uuid.uuid1())

def getDatabaseWrapperInstance(table_name):
    username="sujan079"
    password="hswOC3XWnnWMYJe0"
    database=table_name
    url=f"mongodb+srv://{username}:{password}@databasecluster.svz8u.mongodb.net/"
    client=pymongo.MongoClient(url)
    db=client[database]
    DATABASE_WRAPPER_INSTANCE = DatabaseWrapper(db=db,getUniqueId=generateUniqueId)
    return DATABASE_WRAPPER_INSTANCE
