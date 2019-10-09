import pandas as pd
from collections import Counter
from utils.helper import get_current_date
from repo.data_writer import DataFrameWriter


class Exploration():
    def __init__(self, dataloader, label, repo):
        self.X = dataloader.get_norm_x_dataset()
        self.y = dataloader.y_label
        self.columns = dataloader.get_columns()
        self.label = label
        self.repo = repo
        self.__initializer()

    def __initializer(self):
        X_df = pd.DataFrame(data=self.X, columns=self.columns)
        y_df = pd.DataFrame(data=self.y, columns=[self.label])
        self.df = pd.concat([X_df, y_df], axis=1)

    def class_composition(self):
        composition = pd.DataFrame({'count': self.df.groupby(
            [self.label]).size()}).reset_index()
        return composition

    def correlation_matrix(self):
        correlation_matrix = self.df.corr(method='pearson', min_periods=1)
        return correlation_matrix

    def export(self):
        self.distribution = self.class_composition()
        writer_1 = DataFrameWriter(
            self.distribution, engine=self.repo.sql_engine)
        writer_1.insert_to_sql(
            'churn_data_composition_1', get_current_date())

        self.correlation_matrix = self.correlation_matrix()
        self.correlation_matrix.rename(
            columns={'reg_site_Reservasi.com': 'reg_site_Reservasi'},
            inplace=True)
        writer_2 = DataFrameWriter(
            self.correlation_matrix, engine=self.repo.sql_engine)
        writer_2.insert_to_sql(
            'churn_correlation_matrix_1', get_current_date())
