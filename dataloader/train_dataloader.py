import pandas as pd
from abc import ABC
from dataloader.dataloader import DataLoader
from sklearn.model_selection import train_test_split


class TrainDataLoader(DataLoader):
    def __init__(self, dataset_path, chunk_size, split):
        super(TrainDataLoader, self).__init__(dataset_path, chunk_size)
        self.split = split
        self.__initializer()

    def __initializer(self):
        if self.dataset is not None:
            self.X_data, self.y_label = self.__cleaning_data()

            train_test_res = train_test_split(
                self.X_data,
                self.y_label,
                test_size=self.split)

            self.X_train = train_test_res[0]
            self.X_test = train_test_res[1]
            self.y_train = train_test_res[2]
            self.y_test = train_test_res[3]
        else:
            raise ValueError('Train data loader failed to init')

    def get_norm_x_train(self):
        return self.normalize_data(data=self.X_train)

    def get_norm_x_test(self):
        return self.normalize_data(data=self.X_test)

    def get_norm_x_dataset(self):
        return self.normalize_data(data=self.X_data)

    def get_columns(self):
        return self.X_data.columns

    def __cleaning_data(self):
        features = self.dataset.copy()
        features = features.drop_duplicates(
            keep='first')

        features['issue_rate'].fillna(
            0.0, inplace=True)
        features['redeem_rate'].fillna(
            0.0, inplace=True)

        features.dropna(
            subset=['ios_user', 'android_user'],
            inplace=True)

        features['reg_site'] = features['reg_site'].astype('category')

        features = pd.get_dummies(
            features,
            columns=['reg_site'])

        features.drop(
            ['user_id'],
            axis=1,
            inplace=True)

        y_target = features['churn']
        features.drop(
            ['churn'], axis=1, inplace=True)

        return features, y_target
