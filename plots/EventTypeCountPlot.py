import pandas as pd

from app.AcledCsvToPlot import AcledCsvToPlot


class EventTypeCountPlot(AcledCsvToPlot):
    def build_plot(self, **kwargs):
        event_type_count = self.df.pivot_table(index=['event_type'], aggfunc='size')
        event_type_count.plot.bar()
        if 'with_summary' in kwargs and kwargs.get('with_summary'):
            summary = pd.DataFrame({'Event type': event_type_count.index, 'Reported count': event_type_count.values})
            print(summary.to_string(index=False))
