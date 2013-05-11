'''
Created on May 9, 2013

@author: dorisip
'''
import pystache


def generate_templated_json(template, data):
    '''
    Given a template, and data, Use mustache to template it
    '''
    return pystache.render(template, data)
