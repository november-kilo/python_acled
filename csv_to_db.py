import argparse
import os.path

import pandas as pd

from app.Database import Database

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-r', '--replace', action='store_true')
    arg_parser.add_argument('-s', '--source', default='./data/data.csv')
    args = arg_parser.parse_args()

    if os.path.isfile(args.source):
        with open(args.source, 'r') as csv_source_file:
            data_frame = pd.read_csv(csv_source_file)
            data_frame['event_date'] = pd.to_datetime(data_frame['event_date'], format='%d %B %Y')
            Database.write(data_frame, args.replace)
            print('Done.')
    else:
        print(f'File {args.source} not found.')
