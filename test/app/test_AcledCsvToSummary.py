from app.AcledCsvToSummary import AcledCsvToSummary
from test.base_test import BaseTest


class AcledCsvToPlotTest(BaseTest):
    def test_constants(self):
        self.assertEqual(AcledCsvToSummary.columns(), ['event_type', 'fatalities', 'event_date'], 'Wrong columns.')
