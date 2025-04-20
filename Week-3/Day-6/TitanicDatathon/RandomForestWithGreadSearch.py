from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score


class RandomForestModelWithGridSearch:
    def __init__(self):
        self.best_model = None
        self.best_params = None

    def train_with_grid_search(self, X_train, y_train):
        rf_model = RandomForestClassifier(random_state=42)

        # Hyperparameter grid for tuning
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 5, 10],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4],
            'max_features': ['auto', 'sqrt', 'log2']
        }

        grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
        grid_search.fit(X_train, y_train)

        self.best_model = grid_search.best_estimator_
        self.best_params = grid_search.best_params_

    def evaluate(self, X_test, y_test):
        if not self.best_model:
            raise ValueError("Model is not trained yet. Please call train_with_grid_search() first.")

        predictions = self.best_model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)
        f1 = f1_score(y_test, predictions)
        precision = precision_score(y_test, predictions)
        recall = recall_score(y_test, predictions)
        roc_auc = roc_auc_score(y_test, predictions)

        print(f"Best Parameters: {self.best_params}")
        print(f"Accuracy: {accuracy}")
        print(f"F1 Score: {f1}")
        print(f"Precision: {precision}")
        print(f"Recall: {recall}")
        print(f"ROC-AUC: {roc_auc}")

    def predict(self, X_test):
        if not self.best_model:
            raise ValueError("Model is not trained yet. Please call train_with_grid_search() first.")
        return self.best_model.predict(X_test)
