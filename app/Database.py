import pandas as pd

from app import engine, Constants


class Database:
    @staticmethod
    def write(data_frame: pd.DataFrame):
        data_frame.to_sql(con=engine, name=Constants.TABLENAME, if_exists='append', index=False)
