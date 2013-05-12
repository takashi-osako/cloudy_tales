'''
Created on May 11, 2013

@author: dorisip
'''
import unittest
from cloudy_tales.data_fusion.translate import generate_templated_json,\
    combine_template_with_data
from cloudy_tales.database.tests.UnitTestWithMongoDB import UnitTestWithMongoDB
from cloudy_tales.database.connectionManager import DbConnectionManager
from cloudy_tales.database.collections.base import BaseCollection


class TestTranslate(UnitTestWithMongoDB):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generate_templated_json(self):
        template = "{{{name}}} is here"
        data = {'name': 'foo'}
        results = generate_templated_json(template, data)
        self.assertEqual(results, 'foo is here')

    def test_generate_templated_json_with_no_match(self):
        template = "{{{name}}} is here"
        data = {'bar': 'foo'}
        results = generate_templated_json(template, data)
        self.assertEqual(results, ' is here')

    def test_generate_templated_json_with_array_index(self):
        template = "{{student.1.name}} is absent"
        data = {'student': [{'name': 'foo'}, {'name': 'bar'}]}
        results = generate_templated_json(template, data)
        self.assertEqual(results, 'bar is absent')

    def test_combine_template_with_data(self):
        data_name = 'flower'
        flat_id = '123'
        template = "Flower {{name}} is {{color}}"
        with DbConnectionManager('windy') as connection:
            # prepopulate test data
            col = BaseCollection(connection, data_name)
            data = {'_id': flat_id, 'metadata': {'color': 'red', 'name': 'rose'}}
            col.save(data)

            results = combine_template_with_data(template, flat_id, data_name, write_to_file=False)
            self.assertEquals(results, 'Flower rose is red')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()