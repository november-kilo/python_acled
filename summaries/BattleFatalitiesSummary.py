import re

import numpy as np

from app.AcledCsvToSummary import AcledCsvToSummary
from app.Constants import Constants


class BattleFatalitiesSummary(AcledCsvToSummary):
    def build_data(self):
        date_data = []
        battles_data = []
        fatalities_data = []
        battles = self.df[(self.df['event_type'] == 'Battles')]
        dates = battles.event_date.unique()

        for date in dates[::-1]:
            date_data.append(re.findall(r'\d+', date)[0])
            battles_data.append(np.sum(battles['event_date'].values == date))
            fatalities_data.append(battles.loc[battles['event_date'] == date, 'fatalities'].sum())

        return date_data, battles_data, fatalities_data

    def build_summary(self):
        date_data, battles_data, fatalities_data = self.build_data()
        summary = [f'Battles: {np.sum(battles_data)}, fatalities: {np.sum(fatalities_data)}\n', Constants.DATA_SOURCE]
        return '\n'.join(summary)
