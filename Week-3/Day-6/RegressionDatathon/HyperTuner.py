import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor


class HyperTuner:
    def __init__(self):
        """
        Initialize with a dictionary of models and their hyperparameter grids.
        """
        self.param_grids = {
            "LinearRegression": {},
            "Ridge": {'alpha': [0.1, 1.0, 10.0]},
            "Lasso": {'alpha': [0.1, 1.0, 10.0]},
            "ElasticNet": {'alpha': [0.1, 1.0], 'l1_ratio': [0.1, 0.5, 0.9]},
            "KNN": {'n_neighbors': [3, 5, 7], 'weights': ['uniform', 'distance']},
            "DecisionTree": {'max_depth': [3, 5, 10, None], 'min_samples_split': [2, 5]},
            "RandomForest": {'n_estimators': [100, 200], 'max_depth': [5, 10, None]},
            "GradientBoosting": {'n_estimators': [100, 200], 'learning_rate': [0.01, 0.1], 'max_depth': [3, 5]},
            "XGBoost": {'n_estimators': [100, 200], 'learning_rate': [0.01, 0.1], 'max_depth': [3, 5]},
            "LightGBM": {'n_estimators': [100, 200], 'learning_rate': [0.01, 0.1], 'num_leaves': [31, 50]},
            "CatBoost": {'iterations': [100, 200], 'learning_rate': [0.01, 0.1], 'depth': [4, 6]}
        }
        self.models = {
            "LinearRegression": LinearRegression(),
            "Ridge": Ridge(),
            "Lasso": Lasso(),
            "ElasticNet": ElasticNet(),
            "KNN": KNeighborsRegressor(),
            "DecisionTree": DecisionTreeRegressor(),
            "RandomForest": RandomForestRegressor(random_state=17),
            "GradientBoosting": GradientBoostingRegressor(random_state=17),
            "XGBoost": XGBRegressor(objective='reg:squarederror', random_state=17),
            "LightGBM": LGBMRegressor(random_state=17),
            "CatBoost": CatBoostRegressor(silent=True, random_state=17)
        }

    def tune_model(self, model_name, X, y):
        """
        Tune the specified model using GridSearchCV.

        Args:
            model_name (str): Name of the model to tune.
            X (pd.DataFrame): Feature matrix.
            y (pd.Series): Target variable.

        Returns:
            tuple: (best_model, best_params)
        """
        if model_name not in self.models:
            raise ValueError(f"Model {model_name} not found in models list.")

        model = self.models[model_name]
        param_grid = self.param_grids[model_name]

        if param_grid:
            grid_search = GridSearchCV(
                model,
                param_grid,
                cv=5,  # Increased fold number for more robust evaluation
                scoring='neg_mean_absolute_error',
                n_jobs=-1
            )
            grid_search.fit(X, y)
            return grid_search.best_estimator_, grid_search.best_params_
        else:
            model.fit(X, y)
            return model, {}
