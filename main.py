import argparse
import os.path

from app.AcledCsvToKml import AcledCsvToKml
from summaries.BattleFatalitiesSummary import BattleFatalitiesSummary
from summaries.EventTypeCountSummary import EventTypeCountSummary

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-d', '--data', default='./data/data.kml')
    arg_parser.add_argument('-f', '--fatalities', default='0', required=False)
    arg_parser.add_argument('-k', '--kml', action='store_true', required=False)
    arg_parser.add_argument('-s', '--summaries', nargs='+', required=False)
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
            if arg_name == 'summaries':
                summaries = []

                if 'event_type_count' in value:
                    summaries.append(EventTypeCountSummary(args))

                if 'battle_fatalities' in value:
                    summaries.append(BattleFatalitiesSummary(args))

                for summary in summaries:
                    print(summary.build_summary())
    else:
        print(f'File {args.data} not found.')
