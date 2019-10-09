import os
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from utils.directories import get_latest_file


class Artifact():
    def __init__(self, model=None, exploration=None,
                 evaluations=None, inferences=None,
                 sftp=None, config='', current_date=''):
        self.model = model
        self.exploration = exploration
        self.evaluations = evaluations
        self.inferences = inferences
        self.sftp = sftp
        self.config = config
        self.current_date = current_date

    def __save_model(self):
        if self.model is not None:
            joblib.dump(self.model, '{0}{1}'.format(
                self.config.model_dir,
                'churn_model_' + self.current_date + '.joblib'))

            if self.model.coef_ is not None:
                np.save('{0}{1}'.format(
                    self.config.model_var_dir,
                    'coeficient_' + self.current_date + '.npy'),
                    self.model.coef_)

            if self.model.intercept_ is not None:
                np.save('{0}{1}'.format(
                    self.config.model_var_dir,
                    'intercept_' + self.current_date + '.npy'),
                    self.model.intercept_)

    def __save_to_csv(self, dataframe, base_path, filename, index=False):
        dataframe.to_csv(
            '{0}{1}'.format(base_path, filename),
            index=index)

    def __save_exploration(self):
        if self.exploration is not None:
            class_composition = self.exploration.composition_2_classes()
            correlation_matrix = self.exploration.correlation_matrix()

            self.__save_to_csv(
                class_composition,
                self.config.composition_dir,
                'churn_composition_' + self.current_date + '.csv')

            self.__save_to_csv(
                correlation_matrix,
                self.config.corr_matrix_dir,
                'correlation_matrix_' + self.current_date + '.csv')

    def __save_evaluations(self):
        if self.evaluations is not None:
            if self.evaluations['confusion_matrix'] is not None:
                confusion_matrix = pd.DataFrame(
                    self.evaluations['confusion_matrix'])
                self.__save_to_csv(
                    confusion_matrix,
                    self.config.conf_matrix_dir,
                    'confusion_matrix_' + self.current_date + '.csv',
                    index=True)

    def __save_prediction_result(self):
        if self.inferences is not None:
            preds = self.inferences['preds']
            users = self.inferences['users']

            result = pd.concat(
                [users, pd.DataFrame(preds, columns=['prediction'])],
                axis=1)

            self.__save_to_csv(
                result,
                self.config.result_dir,
                'prediction_result_' + self.current_date + '.csv')

    def __save_all_artifacts(self, source):
        if source == 'train':
            self.__save_model()
            self.__save_exploration()
            self.__save_evaluations()
        elif source == 'inference':
            self.__save_prediction_result()
        print('Successfuly save all artifacts')

    def upload_all_artifacts(self, source):
        self.__save_all_artifacts(source)

        for directory in os.listdir(self.artifact_path):
            if source == 'train':
                if directory == 'prediction_result':
                    continue
            elif source == 'inference':
                if directory != 'prediction_result':
                    continue

            path = os.path.join(self.artifact_path, directory)

            if os.path.isdir(path):
                latest_file = get_latest_file(path)

                remotepath = os.path.join(
                    filepath,
                    directory,
                    latest_file.split('/')[-1])

                self.sftp.upload_file(latest_file, self.config.remote_path)

                print('Upload ' + remotepath + ' success')
