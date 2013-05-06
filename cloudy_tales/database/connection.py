'''
Created on Apr 7, 2013

@author: dorisip
'''
from zope import component
from cloudy_tales.database.client import IDbClient
from pymongo.mongo_client import MongoClient


class DbConnection(object):

    def __init__(self, db_name):
        self.__client = component.queryUtility(IDbClient).get_client()
        self.__db_name = db_name

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        # In memory mongo connection doesn't support close()
        if isinstance(self.__client, MongoClient):
            self.__client.close()

    def get_client(self):
        return self.__client

    def get_db(self):
        return self.get_client()[self.__db_name]

    def get_collection(self, collection_name):
        return self.get_db()[collection_name]
