
class DatabaseWrapper:
    def __init__(self,db,getUniqueId) -> None:
        self.db=db
        self.getUniqueId=getUniqueId
        
    def insert(self,collection,data):
        data["_id"]=self.getUniqueId()
        collection=self.db[collection]
        return collection.insert_one(data)

    def find_one(self,collection,filter={}):
        collection=self.db[collection]
        return collection.find_one(filter)
    
    def find_all(self,collection,filter={}):
        collection=self.db[collection]
        return [item for item in collection.find(filter)]
    
    def get_distinct(self,collection,field_name):
        collection=self.db[collection]
        return [item for item in collection.distinct(field_name)]
    
    def update_by_id(self,collection,id,value):
        collection=self.db[collection]
        return collection.update_one({"_id":id},{"$set":value})
    
    def delete_by_id(self,collection,id):
        collection=self.db[collection]
        return collection.delete_one({"_id":id})
    
    def delete_by_username(self,collection,username):
        collection=self.db[collection]
        return collection.delete_one({"username":username})