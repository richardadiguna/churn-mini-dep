import os
import csv
import chunk
import numpy as np
import pandas as pd
from abc import abstractmethod
from sklearn import preprocessing


class DataLoader():
    def __init__(self, dataset_path, chunk_size):
        self.dataset_path = dataset_path
        self.chunk_size = chunk_size
        self.dataset = self.read_by_chunk()

    def read_by_chunk(self):
        if self.dataset_path is not None:
            result = pd.DataFrame([])

            csv_reader = pd.read_csv(
                self.dataset_path,
                iterator=True,
                chunksize=self.chunk_size)

            for chunk in csv_reader:
                result = pd.concat([result, chunk], axis=0)

            return result

        return None

    def standardize_data(self, data):
        standardizer = preprocessing.StandardScaler()
        std_data = standardizer.fit_transform(std_data)
        return std_data

    def normalize_data(self, data):
        normalizer = preprocessing.Normalizer()
        transformer = normalizer.fit(data)
        norm_data = transformer.transform(data)
        return norm_data

    def iter_minibatches(batch_size, num_samples):
        count = 0
        while count < num_samples:
            chunkrows = range(count, count+batch_size)
            X_chunk, y_chunk = chunkrows
            yield X_chunk, y_chunk
            count += chunksize

    @abstractmethod
    def __cleaning_data(self, data):
        return
