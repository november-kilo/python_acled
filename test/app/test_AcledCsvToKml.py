from app.AcledCsvToKml import AcledCsvToKml
from test.base_test import BaseTest


class AcledCsvToKmlTest(BaseTest):
    def test_constants(self):
        self.assertEqual(AcledCsvToKml.columns(),
                         ['event_type', 'sub_event_type', 'latitude', 'longitude', 'fatalities', 'notes', 'source',
                          'source_scale', 'region'],
                         'Wrong columns.')

    def test_build_kml(self):
        self.compare_actual_to_expected('test/expected/AcledCsvToKmlTest_expected.xml',
                                        AcledCsvToKml(self.options).build_kml())
