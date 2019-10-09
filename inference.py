import os
import datetime
import argparse
import numpy as np
import pandas as pd

from sklearn.externals import joblib
from sftp.inference_sftp import InferenceSFTP
from model.classifier import CustomLogisticRegression
from dataloader.inference_dataloader import InferenceDataLoader

from repo.sql_repo import SQLRepo
from repo.data_writer import DataFrameWriter

from utils.json import get_config
from utils.directories import get_latest_file
from utils.helper import get_current_date


def get_args():
    argparser = argparse.ArgumentParser(
        description=__doc__)
    argparser.add_argument(
        '-d', '--dataset',
        help='Path directory of the datasets')
    argparser.add_argument(
        '-m', '--model',
        help='Path directory of the model')
    argparser.add_argument(
        '-out',
        '--output_dir',
        help='Directory for output file')
    argparser.add_argument(
        '-c',
        '--config',
        help='The Configuration file')
    args = argparser.parse_args()
    return args


def main():
    args = get_args()
    config = get_config(args)
    repo = SQLRepo()

    # sftp = InferenceSFTP(config)
    # latest_dataset = sftp.download_inference_dataset(
    #     config.remote_dataset,
    #     args.dataset)
    # latest_model = sftp.download_inference_model(
    #     config.remote_model,
    #     args.model)

    latest_dataset = get_latest_file(args.dataset)
    latest_model = get_latest_file(args.model)

    dataloader = InferenceDataLoader(
        latest_dataset,
        chunk_size=config.chunk_size)

    model = CustomLogisticRegression()
    model = model.load(latest_model)

    predictions = model.predict(dataloader.get_norm_x())

    result = pd.concat(
        [dataloader.users, pd.DataFrame(predictions, columns=['prediction'])],
        axis=1)

    writer = DataFrameWriter(result, repo.sql_engine)
    writer.insert_to_sql('churn_prediction_result_1', get_current_date())


if __name__ == '__main__':
    print('Run main arguments')
    main()
