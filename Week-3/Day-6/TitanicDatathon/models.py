from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import cross_val_score
import pandas as pd
from tabulate import tabulate
import numpy as np
from xgboost import XGBClassifier

class ModelEvaluator:
    def __init__(self):
        self.models = [
            #('CART', DecisionTreeClassifier(max_depth=5)),
            ('RF', RandomForestClassifier(n_estimators=175, max_depth=8, random_state=1)),
            #('XGBoost', XGBClassifier(objective='binary:logistic', use_label_encoder=False, eval_metric='logloss')),
            #('CatBoost', CatBoostClassifier(verbose=False, depth=6))
        ]

    def evaluate_models(self, X, y, problem_type="classification"):
        results = []
        if problem_type == "classification":
            print("\n📊 Classification Metrics (Accuracy, F1, Precision, Recall, ROC-AUC)")
            for name, model in self.models:
                accuracy = np.mean(cross_val_score(model, X, y, cv=5, scoring="accuracy"))
                f1 = np.mean(cross_val_score(model, X, y, cv=5, scoring="f1"))
                precision = np.mean(cross_val_score(model, X, y, cv=5, scoring="precision"))
                recall = np.mean(cross_val_score(model, X, y, cv=5, scoring="recall"))
                roc_auc = np.mean(cross_val_score(model, X, y, cv=5, scoring="roc_auc"))

                print(f"\nModel: {name}")
                print(f"Accuracy: {round(accuracy, 4)}")
                print(f"F1 Score: {round(f1, 4)}")
                print(f"Precision: {round(precision, 4)}")
                print(f"Recall: {round(recall, 4)}")
                print(f"ROC-AUC: {round(roc_auc, 4)}")

                results.append({
                    "Model": name,
                    "Accuracy": accuracy,
                    "F1 Score": f1,
                    "Precision": precision,
                    "Recall": recall,
                    "ROC-AUC": roc_auc
                })

            results_df = pd.DataFrame(results)
            print("\n📈 Classification Metrics Summary:")
            print(tabulate(results_df, headers="keys", tablefmt="grid", floatfmt=".4f"))

        else:
            raise ValueError("problem_type must be 'regression' or 'classification'")

        return pd.DataFrame(results)

    def train_and_predict(self, X_train, y_train, X_test, passenger_ids, model_name="RandomForest",
                          output_file="submission.csv", problem_type="classification"):
        model_dict = {name: model for name, model in self.models}
        if model_name not in model_dict:
            raise ValueError(f"{model_name} is not among the available models: {list(model_dict.keys())}")

        model = model_dict[model_name]

        # Apply GridSearchCV for RandomForest model
        if model_name == "RF":
            # Define the parameter grid
            param_grid = {
                'n_estimators': [100, 150, 200, 250],
                'max_depth': [None, 10, 20, 30],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 4],
                'max_features': ['auto', 'sqrt', 'log2']
            }

            grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=6, scoring='accuracy', n_jobs=-2, verbose=3)
            grid_search.fit(X_train, y_train)
            print(f"\nBest Parameters from GridSearchCV: {grid_search.best_params_}")

            model = grid_search.best_estimator_

        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        submission_df = pd.DataFrame({
            "PassengerId": passenger_ids,
            "Survived": predictions
        })
        submission_df.to_csv(output_file, index=False)
        print(f"\n✅ Predictions saved to '{output_file}'.")

        return predictions
