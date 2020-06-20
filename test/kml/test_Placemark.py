import pandas as pd

from kml.Placemark import Placemark
from test.base_test import BaseTest


class PlacemarkTest(BaseTest):
    def test_construction(self):
        row = pd.Series(['a', 'b', 'c', 'd', 'e', 'f'],
                        index=['sub_event_type', 'notes', 'fatalities', 'source', 'longitude', 'latitude'])

        self.compare_actual_to_expected('test/expected/PlacemarkTest_expected.xml', Placemark(row).xml)
