from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression


def grid_search_params(classifier, X, y):
    grid_params = {
        'penalty': ['l1', 'l2'],
        'C': [0.1, 0.01, 1.0, 10.0],
        'solver': ['liblinear']
    }

    grid_search = GridSearchCV(
        estimator=classifier,
        param_grid=grid_params,
        scoring='accuracy',
        cv=3, n_jobs=-1)

    print('Begin grid search validation to find best parameters')
    grid_search.fit(
        X, y.values)
    print('Grid search validation done')

    best_params = grid_search.best_params_
    print('Best parameters: {0}'.format(best_params))

    return best_params
