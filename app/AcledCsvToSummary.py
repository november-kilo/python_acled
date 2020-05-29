import pandas as pd


class AcledCsvToSummary:
    def __init__(self, args):
        self.df = pd.read_csv(args.data, usecols=AcledCsvToSummary.columns())

    @staticmethod
    def columns():
        return ['event_type', 'fatalities', 'event_date']

    def build_summary(self):
        return ''
