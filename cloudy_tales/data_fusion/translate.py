'''
Created on May 9, 2013

@author: dorisip
'''
import pystache
from cloudy_tales.database.connectionManager import DbConnectionManager
import json
from bson import json_util
from cloudy_tales.utils.exporter import export
from cloudy_tales.database.collections.base import BaseCollection


def generate_templated_json(template, data):
    '''
    Given a template, and data, Use mustache to template it
    '''
    return pystache.render(template, data)


def combine_template_with_data(template, flat_id='3d5a7389-d53f-4fa4-9802-b6db893ccf1a', data_name='customer', write_to_file=True):
    '''
    Given template data, mustache it
    '''
    with DbConnectionManager('windy') as connection:
        genericCollection = BaseCollection(connection, data_name)
        data = genericCollection.find_one_by_id(flat_id)

        # Temporary template the flat file's data and save to /tmp/template.json
        template = json.dumps(template, default=json_util.default)
        # use mustache
        generated = generate_templated_json(template, data['metadata'])
        generated = json.loads(generated)

        if write_to_file:
            # Write to /tmp/template.json
            export(generated)

    return generated
