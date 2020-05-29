import pandas as pd

from app.AcledCsvToSummary import AcledCsvToSummary
from app.Constants import Constants


class EventTypeCountSummary(AcledCsvToSummary):
    def build_summary(self):
        event_type_count = self.df.pivot_table(index=['event_type'], aggfunc='size')
        summary = pd.DataFrame({'Event type': event_type_count.index, 'Reported count': event_type_count.values})
        return '\n'.join([summary.to_string(index=False), Constants.DATA_SOURCE])
