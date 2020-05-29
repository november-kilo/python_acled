from app.AcledCsvToPlot import AcledCsvToPlot
from test.base_test import BaseTest


class AcledCsvToPlotTest(BaseTest):
    def test_constants(self):
        self.assertEqual(AcledCsvToPlot.columns(), ['event_type', 'fatalities', 'event_date'], 'Wrong columns.')
