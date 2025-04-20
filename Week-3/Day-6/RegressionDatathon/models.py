import numpy as np
import pandas as pd
from catboost import CatBoostRegressor
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor


class ModelEvaluator:
    def __init__(self, best_model_name="LightGBM"):
        """
        Initialize with a list of regression models and specify the best model for final predictions.

        Args:
            best_model_name (str): Name of the model to use for final predictions (default: "LightGBM").
        """
        self.models = [
            ("LinearRegression", LinearRegression()),
            ("Ridge", Ridge()),
            ("Lasso", Lasso()),
            ("ElasticNet", ElasticNet()),
            ("KNN", KNeighborsRegressor()),
            ("DecisionTree", DecisionTreeRegressor()),
           # ("RandomForest", RandomForestRegressor(random_state=17)),
           # ("GradientBoosting", GradientBoostingRegressor(random_state=17)),
            ("XGBoost", XGBRegressor(objective='reg:squarederror', random_state=17)),
            ("LightGBM", LGBMRegressor(random_state=17)),
            ("CatBoost", CatBoostRegressor(silent=True, random_state=17))
        ]
        self.best_model_name = best_model_name
        self.rmse_scores = {}
        self.mae_scores = {}

    def evaluate_models(self, X, y):
        """
        Evaluate all models using 5-fold cross-validation with RMSE and MAE scores.

        Args:
            X (pd.DataFrame): Feature matrix.
            y (pd.Series): Target variable (Age).

        Returns:
            tuple: X_train, X_test, y_train, y_test from the last train-test split.
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=17)

        print("Evaluating models...")
        for name, regressor in self.models:
            # Calculate RMSE
            rmse = np.mean(np.sqrt(-cross_val_score(regressor, X, y, cv=5, scoring="neg_mean_squared_error")))
            self.rmse_scores[name] = rmse

            # Calculate MAE
            mae = np.mean(-cross_val_score(regressor, X, y, cv=5, scoring="neg_mean_absolute_error"))
            self.mae_scores[name] = mae

            print(f"RMSE: {round(rmse, 4)} | MAE: {round(mae, 4)} ({name})")

        # Print the best model based on MAE
        best_model_mae = min(self.mae_scores, key=self.mae_scores.get)
        print(f"\nBest model based on MAE: {best_model_mae} (MAE: {round(self.mae_scores[best_model_mae], 4)})")

        # Print the best model based on RMSE for reference
        best_model_rmse = min(self.rmse_scores, key=self.rmse_scores.get)
        print(f"Best model based on RMSE: {best_model_rmse} (RMSE: {round(self.rmse_scores[best_model_rmse], 4)})")

        return X_train, X_test, y_train, y_test

    def train_and_predict(self, X_train, y_train, X_test, test_ids):
        """
        Train the specified best model and predict for test data.

        Args:
            X_train (pd.DataFrame): Training feature matrix.
            y_train (pd.Series): Training target variable.
            X_test (pd.DataFrame): Test feature matrix.
            test_ids (pd.Series): IDs for test data submission.

        Returns:
            pd.DataFrame: Submission DataFrame with 'id' and 'Age' columns.
        """
        # Find the specified best model
        for name, regressor in self.models:
            if name == self.best_model_name:
                model = regressor
                break
        else:
            raise ValueError(f"Model {self.best_model_name} not found in models list.")

        # Train the model
        model.fit(X_train, y_train)

        # Predict and round to integers
        predictions = model.predict(X_test)
        predictions = np.round(predictions).astype(int)

        # Create submission DataFrame
        submission = pd.DataFrame({'id': test_ids, 'Age': predictions})
        return submission

    def get_rmse_scores(self):
        """
        Return the RMSE scores for all evaluated models.

        Returns:
            dict: Dictionary of model names and their RMSE scores.
        """
        return self.rmse_scores

    def get_mae_scores(self):
        """
        Return the MAE scores for all evaluated models.

        Returns:
            dict: Dictionary of model names and their MAE scores.
        """
        return self.mae_scores