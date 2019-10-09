import pandas as pd
import sqlalchemy


class DataFrameWriter():
    def __init__(self, dataframe=None, engine=None):
        self.dataframe = dataframe
        self.engine = engine

    def insert_to_sql(self, table_name, current_date):
        if current_date is None:
            raise ValueError('Missing arguments current_date')
        else:
            self.dataframe['report_date'] = current_date
            for x in self.dataframe.iterrows():
                try:
                    pd.DataFrame(x[1]).transpose().to_sql(
                        name=table_name,
                        con=self.engine,
                        if_exists='append',
                        index=False)
                except:
                    print('Failed to insert certain data')
                    continue
