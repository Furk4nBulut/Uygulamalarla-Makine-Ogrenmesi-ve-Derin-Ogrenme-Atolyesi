import numpy as np
import pandas as pd
import os
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.base import BaseEstimator, RegressorMixin
from HyperTuner import HyperTuner
from WeightedAssemble import WeightedEnsemble


class ModelEvaluator:
    def __init__(self, best_model_name="WeightedEnsemble", output_dir="predictions"):
        """
        Initialize with a list of regression model names and specify the best model for final predictions.

        Args:
            best_model_name (str): Name of the model to use for final predictions (default: "WeightedEnsemble").
            output_dir (str): Directory to save the output CSV file (default: "predictions").
        """
        self.model_names = [
            "SVR",
        ]
        self.best_model_name = best_model_name
        self.rmse_scores = {}
        self.mae_scores = {}
        self.best_params = {}
        self.tuner = HyperTuner()
        self.trained_models = {}
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def evaluate_models(self, X, y):
        """
        Evaluate all models with hyperparameter tuning using 5-fold cross-validation.

        Args:
            X (pd.DataFrame): Feature matrix.
            y (pd.Series): Target variable (Age).

        Returns:
            tuple: X_train, X_test, y_train, y_test from the last train-test split.
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=17)

        print("Evaluating models with hyperparameter tuning...")
        individual_models = []
        for name in self.model_names:
            if name == "WeightedEnsemble":
                continue
            # Tune and train the model
            best_model, best_params = self.tuner.tune_model(name, X_train, y_train)
            self.trained_models[name] = best_model
            self.best_params[name] = best_params

            # Calculate RMSE
            rmse = np.mean(np.sqrt(-cross_val_score(best_model, X, y, cv=5, scoring="neg_mean_squared_error")))
            self.rmse_scores[name] = rmse

            # Calculate MAE
            mae = np.mean(-cross_val_score(best_model, X, y, cv=5, scoring="neg_mean_absolute_error"))
            self.mae_scores[name] = mae

            print(f"RMSE: {round(rmse, 4)} | MAE: {round(mae, 4)} ({name})")
            if self.best_params[name]:
                print(f"Best parameters: {self.best_params[name]}")

            individual_models.append(best_model)

        # Evaluate Weighted Ensemble
        # Calculate weights as inverse of MAE (normalized)
        mae_scores = np.array([self.mae_scores[name] for name in self.model_names if name != "WeightedEnsemble"])
        weights = 1 / mae_scores
        weights = weights / weights.sum()  # Normalize to sum to 1

        ensemble = WeightedEnsemble(models=individual_models, weights=weights)
        self.trained_models["WeightedEnsemble"] = ensemble
        self.best_params["WeightedEnsemble"] = {"weights": weights.tolist()}

        # Calculate RMSE for ensemble
        rmse = np.mean(np.sqrt(-cross_val_score(ensemble, X, y, cv=5, scoring="neg_mean_squared_error")))
        self.rmse_scores["WeightedEnsemble"] = rmse

        # Calculate MAE for ensemble
        mae = np.mean(-cross_val_score(ensemble, X, y, cv=5, scoring="neg_mean_absolute_error"))
        self.mae_scores["WeightedEnsemble"] = mae

        print(f"RMSE: {round(rmse, 4)} | MAE: {round(mae, 4)} (WeightedEnsemble)")
        print(f"Best parameters: {self.best_params['WeightedEnsemble']}")

        # Print the best model based on MAE
        best_model_mae = min(self.mae_scores, key=self.mae_scores.get)
        print(f"\nBest model based on MAE: {best_model_mae} (MAE: {round(self.mae_scores[best_model_mae], 4)})")
        print(f"Best parameters for {best_model_mae}: {self.best_params[best_model_mae]}")

        # Print the best model based on RMSE for reference
        best_model_rmse = min(self.rmse_scores, key=self.rmse_scores.get)
        print(f"Best model based on RMSE: {best_model_rmse} (RMSE: {round(self.rmse_scores[best_model_rmse], 4)})")

        return X_train, X_test, y_train, y_test

    def train_and_predict(self, X_train, y_train, X_test, test_ids, output_file="submission.csv"):
        """
        Train the specified best model with its best parameters and save predictions to a CSV file
        with the format 'id,Age' followed by the predictions.

        Args:
            X_train (pd.DataFrame): Training feature matrix.
            y_train (pd.Series): Training target variable.
            X_test (pd.DataFrame): Test feature matrix.
            test_ids (pd.Series): IDs for test data submission.
            output_file (str): File name for the submission CSV (default: "submission.csv").

        Returns:
            np.ndarray: Array of predictions.
        """
        print(f"\n🔧 Training model: {self.best_model_name}")

        if self.best_model_name == "WeightedEnsemble":
            best_model = self.trained_models.get("WeightedEnsemble")
            if best_model is None:
                raise ValueError("WeightedEnsemble not trained. Run evaluate_models first.")
        else:
            best_model, best_params = self.tuner.tune_model(self.best_model_name, X_train, y_train)
            self.best_params[self.best_model_name] = best_params
            print(f"✅ Best Parameters for {self.best_model_name}: {best_params}")

        best_model.fit(X_train, y_train)
        predictions = best_model.predict(X_test)
        predictions = np.round(predictions).astype(int)

        output_path = os.path.join(self.output_dir, output_file)
        submission_df = pd.DataFrame({
            "id": test_ids,
            "Age": predictions
        })
        submission_df.to_csv(output_path, index=False)
        print(f"\n📁 Predictions saved to '{output_path}'.")

        return predictions

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

    def get_best_params(self):
        """
        Return the best parameters for all evaluated models.

        Returns:
            dict: Dictionary of model names and their best parameters.
        """
        return self.best_params