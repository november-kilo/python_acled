import unittest

from app.Constants import Constants


class ConstantsTest(unittest.TestCase):
    def test_data_source(self):
        self.assertEqual(Constants.DATA_SOURCE,
                         'Data source: Armed Conflict Location & Event Data Project (ACLED); https://www.acleddata.com')
        self.assertEqual(Constants.DATABASE, 'acled.sqlite')
        self.assertEqual(Constants.TABLENAME, 'acled_event')
