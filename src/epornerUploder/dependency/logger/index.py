
from dependency.database.index import getDatabaseWrapperInstance
from dependency.logger.logger import Logger

def getLoggerInstance(instance):
    db=getDatabaseWrapperInstance()
    return Logger(db=db,logger_instance=instance)