import pandas as pd
from dataloader.dataloader import DataLoader


class InferenceDataLoader(DataLoader):
    def __init__(self, dataset_path, chunk_size):
        super(InferenceDataLoader, self).__init__(dataset_path, chunk_size)
        self.__initializer()

    def __initializer(self):
        if self.dataset is not None:
            self.X_data, self.users = self.__cleaning_data()
        else:
            raise ValueError('Train data loader failed to init')

    def get_norm_x(self):
        return self.normalize_data(self.X_data)

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

        users = features['user_id']
        users.reset_index(drop=True, inplace=True)

        features.drop(
            ['user_id'],
            axis=1,
            inplace=True)

        features.drop(
            ['churn'], axis=1, inplace=True)

        return features, users
