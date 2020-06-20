import pandas as pd

from app.AcledCsvToKml import AcledCsvToKml
from kml.Folder import Folder
from test.base_test import BaseTest


class FolderTest(BaseTest):
    def setUp(self):
        super().setUp()
        try:
            self.df = pd.read_csv(self.options['data_filename'], usecols=AcledCsvToKml.columns(),
                                  dtype={'fatalities': int})
        except IOError:
            print('Failed to open test data.')

    def test_build_folder(self):
        f = Folder(self.df, 'Protests', self.options)

        self.compare_actual_to_expected('test/expected/FolderTest_expected.xml', f.build_folder())

    def test_build_folder_with_fatalities_filter(self):
        self.options['fatalities_at_least'] = 6
        f = Folder(self.df, 'Protests', self.options)

        self.compare_actual_to_expected('test/expected/FolderTest_withFatalities_expected.xml', f.build_folder())

        self.options['fatalities_at_least'] = 5
        f = Folder(self.df, 'Protests', self.options)

        self.compare_actual_to_expected('test/expected/FolderTest_withFatalities_expected.xml', f.build_folder())
