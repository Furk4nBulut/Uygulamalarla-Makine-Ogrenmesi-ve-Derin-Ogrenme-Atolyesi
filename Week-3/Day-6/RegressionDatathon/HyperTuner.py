import numpy as np
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from scipy.stats import uniform, randint, loguniform

class HyperTuner:
    def __init__(self):
        """
        Initialize with a dictionary of models and their hyperparameter grids.
        """
        self.param_grids = {
            "LinearRegression": {},
            "Ridge": {'alpha': [0.1, 1.0, 10.0, 100.0]},
            "Lasso": {'alpha': [0.01, 0.1, 1.0, 10.0]},
            "ElasticNet": {'alpha': [0.01, 0.1, 1.0], 'l1_ratio': [0.1, 0.3, 0.5, 0.7, 0.9]},
            "KNN": {'n_neighbors': [3, 5, 7, 9], 'weights': ['uniform', 'distance']},
            "DecisionTree": {'max_depth': [3, 5, 10, None], 'min_samples_split': [2, 5, 10]},
            "RandomForest": {
                'n_estimators': randint(50, 150),
                'max_depth': [5, 10, 15, None],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 4]
            },
            "GradientBoosting": {
                'n_estimators': randint(50, 200),
                'learning_rate': loguniform(0.005, 0.2),
                'max_depth': [3, 5, 7],
                'subsample': uniform(0.6, 0.4),
                'min_samples_split': [2, 5, 10]
            },
            "XGBoost": {
                'n_estimators': randint(50, 200),
                'learning_rate': loguniform(0.005, 0.2),
                'max_depth': [3, 5, 7, 9],
                'subsample': uniform(0.6, 0.4),
                'colsample_bytree': uniform(0.6, 0.4)
            },
            "LightGBM": {
                'n_estimators': randint(50, 200),
                'learning_rate': loguniform(0.005, 0.2),
                'num_leaves': randint(20, 50),
                'max_depth': [3, 5, 7, -1],
                'subsample': uniform(0.6, 0.4),
                'colsample_bytree': uniform(0.6, 0.4)
            },
            "CatBoost": {
                'iterations': randint(100, 300),
                'learning_rate': loguniform(0.005, 0.2),
                'depth': [4, 6, 8, 10],
                'l2_leaf_reg': uniform(1, 10),
                'bagging_temperature': uniform(0, 1)
            },
            "SVR": {
                'C': loguniform(0.1, 10),
                'epsilon': uniform(0.05, 0.2),
                'kernel': ['rbf', 'linear'],
                'gamma': loguniform(1e-4, 1e-1)
            }
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
            "CatBoost": CatBoostRegressor(silent=True, random_state=17),
            "SVR": SVR()
        }

    def tune_model(self, model_name, X, y):
        """
        Tune the specified model using GridSearchCV or RandomizedSearchCV.

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
            # Use RandomizedSearchCV for complex models
            if model_name in ["SVR"]:
                search = RandomizedSearchCV(
                    model,
                    param_distributions=param_grid,
                    n_iter=10,  # Sample 10 combinations
                    cv=2,
                    scoring='neg_mean_absolute_error',
                    n_jobs=-1,
                    verbose=1,
                    random_state=17
                )
            else:
                # Use GridSearchCV for simpler models
                search = GridSearchCV(
                    model,
                    param_grid,
                    cv=1,
                    scoring='neg_mean_absolute_error',
                    n_jobs=-1,
                    verbose=1
                )
            search.fit(X, y)
            return search.best_estimator_, search.best_params_
        else:
            model.fit(X, y)
            return model, {}