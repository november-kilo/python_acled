import pandas as pd
import matplotlib.pyplot as plt


class AcledCsvToPlot:
    def __init__(self, args):
        self.df = pd.read_csv(args.data, usecols=AcledCsvToPlot.columns())
        self.plt = plt
        self.title = args.title

    @staticmethod
    def columns():
        return ['event_type', 'fatalities', 'event_date']

    def build_plot(self, **kwargs):
        pass

    def show(self):
        plt.show()
