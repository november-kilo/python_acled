import re
import numpy as np

from app.AcledCsvToPlot import AcledCsvToPlot


class BattleFatalitiesPlot(AcledCsvToPlot):
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

    def build_plot(self, **kwargs):
        date_data, battles_data, fatalities_data = self.build_data()

        _, ax = self.plt.subplots()
        ax.plot(date_data, battles_data, label='Battles')
        ax.plot(date_data, fatalities_data, label='Fatalities')

        battles_mean = [np.mean(battles_data)] * len(date_data)
        ax.plot(date_data, battles_mean, label='Battles mean', linestyle='--')
        fatalities_mean = [np.mean(fatalities_data)] * len(date_data)
        ax.plot(date_data, fatalities_mean, label='Fatalities mean', linestyle='--')

        self.plt.legend(bbox_to_anchor=(1, 1.3), loc='upper right', ncol=2)

        for tick in ax.xaxis.get_major_ticks()[1::2]:
            tick.set_pad(15)

        self.plt.title(self.title)
        self.plt.grid(b=True)

        if 'with_summary' in kwargs and kwargs.get('with_summary'):
            print(f'Battles: {np.sum(battles_data)}, fatalities: {np.sum(fatalities_data)}')
