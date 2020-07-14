from app.Constants import Constants


class Placemark:
    def __init__(self, row):
        xml = ['<Placemark>',
               f'<name><![CDATA[{row.sub_event_type}]]></name>',
               f'<description><![CDATA[{row.notes}\nFatalities: {row.fatalities}\nSource: {row.source}',
               f' ({row.source_scale})\n',
               f'<p>{Constants.DATA_SOURCE}</p>]]></description>',
               '<Point>',
               f'<coordinates>{row.longitude},{row.latitude},0</coordinates>',
               '</Point>',
               '</Placemark>']
        self.xml = '\n'.join(xml)
