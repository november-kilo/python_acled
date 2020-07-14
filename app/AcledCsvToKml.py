import pandas as pd

from kml.Folder import Folder


class AcledCsvToKml:
    def __init__(self, options):
        self.df = pd.read_csv(options['data_filename'], usecols=AcledCsvToKml.columns(), dtype={'fatalities': int})
        self.folders = self.df.event_type.unique()
        self.options = options

    @staticmethod
    def columns():
        return ['event_type', 'sub_event_type', 'latitude', 'longitude', 'fatalities', 'notes', 'source',
                'source_scale', 'region']

    def build_kml(self):
        xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<kml xmlns="http://www.opengis.net/kml/2.2">', '<Document>']
        for folder in self.folders:
            xml.append(Folder(self.df, folder, self.options).build_folder())
        xml.append('</Document>\n</kml>')
        return '\n'.join(xml)
