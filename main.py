import os.path
import argparse

from app.AcledCsvToKml import AcledCsvToKml
from plots.BattleFatalitiesPlot import BattleFatalitiesPlot
from plots.EventTypeCountPlot import EventTypeCountPlot

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-d', '--data', default='./data/data.kml')
    arg_parser.add_argument('-f', '--fatalities', default='0', required=False)
    arg_parser.add_argument('-k', '--kml', action='store_true', required=False)
    arg_parser.add_argument('-p', '--plots', nargs='+', required=False)
    arg_parser.add_argument('-s', '--summary', action='store_true', required=False)
    arg_parser.add_argument('-t', '--title', default='', required=False)
    args = arg_parser.parse_args()
    options = {
        'data_filename': args.data,
        'fatalities_at_least': int(args.fatalities)
    }
    if os.path.isfile(args.data):
        if args.kml:
            kml = AcledCsvToKml(options).build_kml()
            with open(f'{args.data}.kml', 'w') as kml_file:
                print(f'{kml}', file=kml_file)

        for arg_name, value in arg_parser.parse_args()._get_kwargs():
            if arg_name == 'plots':
                plots = []

                if 'event_type_count' in value:
                    plots.append(EventTypeCountPlot(args))

                if 'battle_fatalities' in value:
                    plots.append(BattleFatalitiesPlot(args))

                for plot in plots:
                    plot.build_plot(with_summary=args.summary)
                    plot.show()
    else:
        print(f'File {args.data} not found.')
