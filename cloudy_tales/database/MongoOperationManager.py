'''
Created on May 5, 2013

@author: tosako
'''

class MongoOperationManager(object):

    def __init__(self, connection):
        self.__connection = connection

    def insert(self, collection_name, *args, **kwargs):
        '''
        Given a collection name, and a python dictionary, insert it
        '''
        _id = self.__connection.get_collection(collection_name).insert(*args, **kwargs)
        return _id

    def find(self, collection_name, *args, **kwargs):
        '''
        Find based on _id
        Returns a list of json objects
        '''
        results = self.__connection.get_collection(collection_name).find(*args, **kwargs)
        return list(results)

    def find_one(self, collection_name, *args, **kwargs):
        '''
        Find_one in collection
        '''
        result = self.__connection.get_collection(collection_name).find_one(*args, **kwargs)
        return result

    def remove(self, collection_name, *args, **kwargs):
        '''
        Remove document from mongo
        '''
        return self.__connection.get_collection(collection_name).remove(*args, **kwargs)

    def update(self, collection_name, *args, **kwargs):
        '''
        Update a document with doc
        '''
        return self.__connection.get_collection(collection_name).update(*args, **kwargs)

    def save(self, collection_name, *args, **kwargs):
        '''
        Saves a document (update and/or inserts)
        '''
        return self.__connection.get_collection(collection_name).save(*args, **kwargs)
