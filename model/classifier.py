from base.base_model import BaseModel
from utils.grid_search import grid_search_params
from sklearn.linear_model import LogisticRegression


class CustomLogisticRegression(BaseModel):
    def __init__(self, config=None, dataloader=None, grid_search=None):
        super(CustomLogisticRegression, self).__init__(config)
        self.build_model(grid_search, dataloader)

    def build_model(self, grid_search, dataloader):
        if grid_search is True:
            if dataloader is not None:

                X = self.dataloader.get_norm_x_train(),
                y = self.dataloader.y_train

                params = grid_search_params(LogisticRegression(), X, y)

                self.model = LogisticRegression(
                    penalty=params['penalty'],
                    C=params['C'],
                    solver=params['solver'],
                    verbose=1)
        else:
            self.model = LogisticRegression(
                penalty='l1',
                C=10,
                solver='liblinear',
                verbose=1)
