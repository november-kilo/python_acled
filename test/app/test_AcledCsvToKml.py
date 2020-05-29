from app.AcledCsvToKml import AcledCsvToKml
from test.base_test import BaseTest


class AcledCsvToKmlTest(BaseTest):
    def test_constants(self):
        self.assertEqual(AcledCsvToKml.columns(),
                         ['event_type', 'sub_event_type', 'latitude', 'longitude', 'fatalities', 'notes', 'source', 'region'],
                         'Wrong columns.')

    def test_build_kml(self):
        self.xml_compare('test/expected/AcledCsvToKmlTest_expected.xml', AcledCsvToKml(self.options).build_kml())
