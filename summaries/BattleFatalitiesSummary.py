import re

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from app.AcledCsvToSummary import AcledCsvToSummary
from app.Constants import Constants
from app.GeometricMean import GeometricMean


class BattleFatalitiesSummary(AcledCsvToSummary):
    def __init__(self, args):
        super().__init__(args)
        self.fatalities_data = []
        self.battles_data = []
        self.date_data = []

    def reset(self):
        self.fatalities_data = []
        self.battles_data = []
        self.date_data = []

    def build_data(self):
        battles = self.df[(self.df['event_type'] == 'Battles')]
        dates = battles.event_date.unique()

        for date in dates[::-1]:
            self.date_data.append(re.findall(r'\d+', date)[0])
            self.battles_data.append(np.sum(battles['event_date'].values == date))
            self.fatalities_data.append(battles.loc[battles['event_date'] == date, 'fatalities'].sum())

        return self.date_data, self.battles_data, self.fatalities_data

    def build_summary(self):
        self.reset()
        self.build_data()
        summary = [f'Battles: {np.sum(self.battles_data)}, fatalities: {np.sum(self.fatalities_data)}\n', Constants.DATA_SOURCE]
        return '\n'.join(summary)

    def display_plot(self):
        df = pd.DataFrame({
            'Date': self.date_data,
            'battles': self.battles_data,
            'battles_mean': [GeometricMean.get(self.battles_data)] * len(self.battles_data),
            'fatalities': self.fatalities_data,
            'fatalities_mean': [GeometricMean.get(self.fatalities_data)] * len(self.fatalities_data)
        })

        ax = plt.gca()
        df.plot(kind='line', x='Date', color='blue', y='battles', label='Battles', ax=ax)
        df.plot(kind='line', x='Date', color='blue', y='battles_mean', linewidth=1, label='Battles mean', linestyle='--', ax=ax)
        df.plot(kind='line', x='Date', color='red', y='fatalities', label='Fatalities', ax=ax)
        df.plot(kind='line', x='Date', color='red', y='fatalities_mean', linewidth=1, label='Fatalities mean', linestyle='--', ax=ax)
        plt.text(0, 12, Constants.DATA_SOURCE_NAME)
        plt.text(0, 0, Constants.DATA_SOURCE_URL)
        plt.show()
