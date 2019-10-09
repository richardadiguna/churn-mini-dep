import os
import argparse
import pandas as pd

from sftp.train_sftp import TrainSFTP
from artifacts.artifacts import Artifact
from exploration.exploration import Exploration

from repo.sql_repo import SQLRepo

from trainer.simple_train import Trainer
from model.classifier import CustomLogisticRegression
from dataloader.train_dataloader import TrainDataLoader

from utils.json import get_config
from utils.helper import get_current_date
from utils.directories import get_latest_file


def get_args():
    argparser = argparse.ArgumentParser(
        description=__doc__)
    argparser.add_argument(
        '-d', '--dataset',
        default=None,
        help='Path directory of the datasets')
    argparser.add_argument(
        '-out',
        '--output_dir',
        default=None,
        help='Directory for output file')
    argparser.add_argument(
        '-c',
        '--config',
        default=None,
        help='The Configuration file')
    argparser.add_argument(
        '-v', '--version',
        default=None,
        help='Version of the saved model')
    args = argparser.parse_args()
    return args


def main():
    args = get_args()
    config = get_config(args)
    repo = SQLRepo()

    # sftp = TrainSFTP(config)
    # train_dataset = sftp.download_train_dataset(
    #     config.remote_dataset,
    #     args.dataset)

    train_dataset = get_latest_file(args.dataset)

    dataloader = TrainDataLoader(
        train_dataset,
        chunk_size=config.chunk_size,
        split=config.split)

    model = CustomLogisticRegression(
        config, dataloader, grid_search=False)

    trainer = Trainer(model, config, dataloader, repo)
    trainer.train()

    exploration = Exploration(
        dataloader, label='churn', repo=repo)
    exploration.export()


if __name__ == '__main__':
    print('Run main arguments')
    main()
