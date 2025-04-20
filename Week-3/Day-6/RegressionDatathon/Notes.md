RMSE: 2.0474 | MAE: 1.406 (CatBoost)
Best parameters: {'bagging_temperature': np.float64(0.7583992428505223), 'depth': 10, 'iterations': 163, 'l2_leaf_reg': np.float64(6.124924170327478), 'learning_rate': np.float64(0.09343371732694564)}
Fitting 5 folds for each of 10 candidates, totalling 50 fits



Initializing DataLoader...
Loading data...
Data loaded successfully.
Observations: 123419
Variables: 18
cat_cols: 1
num_cols: 17
cat_but_car: 0
num_but_cat: 0
Observations: 123419
Variables: 18
cat_cols: 1
num_cols: 17
cat_but_car: 0
num_but_cat: 1
Evaluating models with hyperparameter tuning...
Fitting 2 folds for each of 10 candidates, totalling 20 fits
RMSE: 2.1058 | MAE: 1.3838 (SVR)
Best parameters: {'C': np.float64(1.3274488960140944), 'epsilon': np.float64(0.1292094872094053), 'gamma': np.float64(0.023232830772238453), 'kernel': 'rbf'}
RMSE: 2.1058 | MAE: 1.3838 (WeightedEnsemble)
Best parameters: {'weights': [1.0]}

Best model based on MAE: SVR (MAE: 1.3838)
Best parameters for SVR: {'C': np.float64(1.3274488960140944), 'epsilon': np.float64(0.1292094872094053), 'gamma': np.float64(0.023232830772238453), 'kernel': 'rbf'}
Best model based on RMSE: SVR (RMSE: 2.1058)

🔧 Training model: WeightedEnsemble

📁 Predictions saved to 'predictions/submission.csv'.

Process finished with exit code 0