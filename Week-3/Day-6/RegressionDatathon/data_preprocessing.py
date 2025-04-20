import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import helpers


class DataPreprocessing:
    def __init__(self, dataframe):
        """
        Initialize with a combined DataFrame (train + test).

        Args:
            dataframe (pd.DataFrame): Combined DataFrame with train (Age non-null) and test (Age null) data.
        """
        self.df = dataframe.copy()

    def preprocess(self, is_test_only=False):
        self.handle_outliers()
        self.handle_missing_values()
        self.feature_engineering()
        self.drop_unnecessary_columns()
        self.encode_features()

        if is_test_only:
            # Test verisini al ve 'id'yi düşürmeden önce sakla
            test_data = self.df[self.df['Age'].isnull()].drop('Age', axis=1)
            test_ids = test_data["id"].copy()  # 'id'yi sakla
            test_data = test_data.drop(columns=['id'])  # 'id'yi test verisinden çıkar
            return test_data, test_ids  # 'test_ids' ile birlikte döndür
        else:
            # Eğitim verisini al ve 'id'yi düşür
            train_data = self.df[self.df['Age'].notnull()]
            train_data = train_data.drop(columns=['id'])  # 'id'yi düşür

            X = train_data.drop('Age', axis=1)
            y = train_data['Age']
            X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
            return X_train, X_val, y_train, y_val

    def handle_outliers(self):
        """
        Handle outliers using IQR method for numerical columns (excluding Age).
        """
        num_cols = self.df.select_dtypes(include=np.number).columns
        num_cols = [col for col in num_cols if col != 'Age']
        for col in num_cols:
            if helpers.check_outlier(self.df, col):
                self.df = helpers.replace_with_thresholds(self.df, col)

    def handle_missing_values(self):
        """
        Handle missing values: mean for numerical (excluding Age), mode for categorical.
        """
        num_cols = self.df.select_dtypes(include=np.number).columns
        num_cols = [col for col in num_cols if col != 'Age']
        self.df[num_cols] = self.df[num_cols].fillna(self.df[num_cols].mean())
        cat_cols = self.df.select_dtypes(include='object').columns
        for col in cat_cols:
            self.df[col] = self.df[col].fillna(self.df[col].mode()[0])

    def feature_engineering(self):
        """
        Create new features for abalone dataset.
        """
        self.df['Shell_Weight_Ratio'] = self.df['Shell Weight'] / self.df['Weight']
        self.df['Shucked_Weight_Ratio'] = self.df['Shucked Weight'] / self.df['Weight']
        self.df['Viscera_Weight_Ratio'] = self.df['Viscera Weight'] / self.df['Weight']
        self.df['Volume'] = self.df['Length'] * self.df['Diameter'] * self.df['Height']
        for col in ['Weight', 'Shucked Weight', 'Viscera Weight', 'Shell Weight']:
            self.df[f'Log_{col}'] = np.log1p(self.df[col])

    def drop_unnecessary_columns(self):
        columns_to_drop = ["some_other_column"]  # "id" burada olmamalı
        self.df.drop(columns=[col for col in columns_to_drop if col in self.df.columns], inplace=True)

    def encode_features(self):
        """
        Encode categorical features (Sex).
        """
        cat_cols, cat_but_car, num_cols = helpers.grab_col_names(self.df)
        binary_cols = [col for col in cat_cols if self.df[col].nunique() <= 3]
        for col in binary_cols:
            self.df = helpers.label_encoder(self.df, col)
        cat_cols = [col for col in cat_cols if col not in binary_cols]
        if cat_cols:
            self.df = helpers.one_hot_encoder(self.df, cat_cols, drop_first=True)
        remaining_object_cols = self.df.select_dtypes(include='object').columns.tolist()
        if remaining_object_cols:
            raise ValueError(f"Categorical columns not fully encoded: {remaining_object_cols}")