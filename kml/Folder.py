from app.Constants import Constants
from kml.Placemark import Placemark


class Folder:
    def __init__(self, df, folder, options):
        self.df = df
        self.folder = folder
        self.options = options

    def populate_folder(self):
        xml = []
        folder_rows = self.df[(self.df['event_type'] == self.folder) & (
                    self.df['fatalities'] >= self.options['fatalities_at_least'])].drop_duplicates()
        for _, row in folder_rows.iterrows():
            xml.append(Placemark(row).xml)
        return '\n'.join(xml)

    def build_folder(self):
        xml = ['<Folder>',
               f'<name><![CDATA[{self.folder}]]></name>',
               f'<description><![CDATA[{Constants.DATA_SOURCE}]]></description>',
               self.populate_folder(),
               '</Folder>']
        return '\n'.join(xml)
