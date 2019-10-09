import os
import pandas as pd
from sklearn import metrics
from utils.helper import get_current_date
from repo.data_writer import DataFrameWriter


class Trainer():
    def __init__(self, classifier, config,
                 dataloader, repo=None, logger=None):
        self.classifier = classifier
        self.config = config
        self.dataloader = dataloader
        self.repo = repo
        self.logger = logger

    def train(self):
        X = self.dataloader.get_norm_x_train()
        y = self.dataloader.y_train
        self.classifier.model.fit(X, y)
        self.eval()
        self.export_eval()
        self.classifier.save()

    def eval(self):
        X = self.dataloader.get_norm_x_test()
        y = self.dataloader.y_test
        predictions = self.classifier.model.predict(X)

        self.accuracy = metrics.accuracy_score(predictions, y)
        self.confusion_matrix = metrics.confusion_matrix(y, predictions)

        print('Accuracy of predicting the test set: {0}'.format(self.accuracy))

    def export_eval(self):
        confusion_matrix = pd.DataFrame(self.confusion_matrix)
        confusion_matrix.rename(
            columns={0: 'non_churn', 1: 'churn'},
            inplace=True)
        writer = DataFrameWriter(confusion_matrix, engine=self.repo.sql_engine)
        writer.insert_to_sql('churn_confusion_matrix_1', get_current_date())
