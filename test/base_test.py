import unittest
from argparse import Namespace


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.options = {
            'data_filename': 'test/data/test_data.csv',
            'fatalities_at_least': 0
        }
        self.args = Namespace(data=self.options['data_filename'], title='a title')

    def compare_actual_to_expected(self, filename, actual):
        f = open(filename, 'r')
        expected = f.read()
        f.close()
        msg = f'expected\n{expected}\n\ngot\n{actual}'

        self.assertEqual(actual, expected, msg)

