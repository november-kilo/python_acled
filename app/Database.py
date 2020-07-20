import pandas as pd

from app import engine, Constants


class Database:
    @staticmethod
    def write(data_frame: pd.DataFrame, should_replace):
        if should_replace:
            if_exists = 'replace'
        else:
            if_exists = 'append'

        data_frame.to_sql(con=engine, name=Constants.TABLENAME, if_exists=if_exists, index=False)
