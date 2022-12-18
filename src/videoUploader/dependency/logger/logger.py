class Logger:
    def __init__(self,logger_instance,db) -> None:
        self.logger_instance=logger_instance
        self.db=db
    
    def dispatchLog(self,data):
        self.db.insert(collection=self.logger_instance,data=data)
