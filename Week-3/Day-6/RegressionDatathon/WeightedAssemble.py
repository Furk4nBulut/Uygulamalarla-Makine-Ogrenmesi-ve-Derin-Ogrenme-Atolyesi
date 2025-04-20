import numpy as np
import pandas as pd
import os
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.base import BaseEstimator, RegressorMixin
from HyperTuner import HyperTuner

class WeightedEnsemble(BaseEstimator, RegressorMixin):
    def __init__(self, models, weights):
        """
        Initialize the weighted ensemble model.

        Args:
            models (list): List of trained models.
            weights (list): Weights for each model's predictions.
        """
        self.models = models
        self.weights = weights

    def fit(self, X, y):
        """
        Fit all models in the ensemble.

        Args:
            X (pd.DataFrame): Feature matrix.
            y (pd.Series): Target variable.
        """
        for model in self.models:
            model.fit(X, y)
        return self

    def predict(self, X):
        """
        Predict using weighted average of model predictions.

        Args:
            X (pd.DataFrame): Feature matrix.

        Returns:
            np.ndarray: Weighted average predictions.
        """
        predictions = np.column_stack([model.predict(X) for model in self.models])
        return np.average(predictions, axis=1, weights=self.weights)