'''
Created on Apr 7, 2013

@author: dorisip
'''


class BaseCollection(object):
    '''
    Base database collection class
    '''

    def __init__(self, mongoOperationManager, name):
        self.__mongoOperationManager = mongoOperationManager
        self.__collection_name = name

    def insert(self, *args, **kwargs):
            doc_id = self.__mongoOperationManager.insert(self.__collection_name, *args, **kwargs)
            # TODO: error check?
            return {'_id': doc_id}

    def remove_by_id(self, doc_id, *args, **kwargs):
        return self.__mongoOperationManager.remove(self.__collection_name, {'_id': doc_id}, *args, **kwargs)

    def remove(self, *args, **kwargs):
        return self.__mongoOperationManager.remove(self.__collection_name,*args, **kwargs)

    def update_by_id(self, doc_id, doc, upsert=True, *args, **kwargs):
        result = self.__mongoOperationManager.update(self.__collection_name, {'_id': doc_id}, {'$set': doc}, upsert=upsert, *args, **kwargs)
        if result and result['ok']:
            return {'_id': doc_id}
        else:
            return None

    def update(self, *args, **kwargs):
        return self.__mongoOperationManager.update(self.__collection_name, *args, **kwargs)

    def find_by_id(self, doc_id, *args, **kwargs):
        return self.__mongoOperationManager.find_one(self.__collection_name, {'_id': doc_id}, *args, **kwargs)

    def find(self, *args, **kwargs):
        return self.__mongoOperationManager.find(self.__collection_name, *args, **kwargs)

    def find_one_by_id(self, doc_id, *args, **kwargs):
        return self.__mongoOperationManager.find_one(self.__collection_name, {'_id': doc_id}, *args, **kwargs)

    def find_one(self, *args, **kwargs):
        return self.__mongoOperationManager.find_one(self.__collection_name, *args, **kwargs)

    def save(self, *args, **kwargs):
        return {'_id': self.__mongoOperationManager.save(self.__collection_name, *args, **kwargs)}
