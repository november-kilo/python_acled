import unittest


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.options = {
            'data_filename': 'test/data/test_data.csv',
            'fatalities_at_least': 0
        }

    def xml_compare(self, filename, actual):
        f = open(filename, 'r')
        expected = f.read()
        f.close()
        msg = f'expected\n{expected}\n\ngot\n{actual}'
        self.assertEqual(actual, expected, msg)
