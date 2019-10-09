import os
import joblib
from utils.helper import get_current_date


class BaseModel():
    def __init__(self, config):
        self.config = config
        self.model = None

    def save(self):
        current_date = get_current_date()
        joblib.dump(self.model, '{0}{1}'.format(
            self.config.model_dir,
            'churn_model_' + current_date + '.joblib'))

    def load(self, model_path):
        if os.path.exists(model_path):
            model = joblib.load(model_path)
            return model
        else:
            raise ValueError('Model path is not exists')

    def build_model(self):
        raise NotImplementedError
