'''
Created on May 9, 2013

@author: dorisip
'''
import pystache


def render_template(template, data):
    '''
    Given a template, and data, Use mustache to template it
    '''
    return pystache.render(template, data)


def generate_templated_json():
    template = ' {{address.phone.0.home}}' # {{address.address_line1}} {{address.city}} {{address.person.first_name}}'
    data = {"address": {"city": "New York City", "address_line1": "65 Washington St", "zip": "98007", "phone": [{"mobile": "9999999999", "home": "1234567890"}, {"mobile": "2222222222", "home": "1111111111"}], "country": "JP", "person": {"first_name": "Jack", "last_name": "Smith"}}}
    
    templated = render_template(template, data)
    print(templated)
