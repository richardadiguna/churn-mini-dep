import os
import json
from bunch import Bunch


def json_parser(json_file):
    with open(json_file, 'r') as config_file:
        config_dict = json.load(config_file)
    config = Bunch(config_dict)
    return config, config_dict


def get_config(args):
    config, _ = json_parser(args.config)
    base_path = args.output_dir

    config.model_dir = os.path.join(base_path, 'model_joblib/')
    config.model_var_dir = os.path.join(base_path, 'model_variable/')
    config.composition_dir = os.path.join(base_path, 'data_composition/')
    config.corr_matrix_dir = os.path.join(base_path, 'correlation_matrix/')
    config.conf_matrix_dir = os.path.join(base_path, 'confusion_matrix/')
    config.result_dir = os.path.join(base_path, 'prediction_result/')

    return config
