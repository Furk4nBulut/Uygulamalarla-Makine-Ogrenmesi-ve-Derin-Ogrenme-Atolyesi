import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
import seaborn as sns
import matplotlib.pyplot as plt
from helpers import grab_col_names, one_hot_encoder

class DataPreprocessing:
    def __init__(self, dataframe):
        self.df = dataframe.copy()
        self.encoded_columns = None

    def handle_missing_values(self):
        if 'Embarked' in self.df.columns:
            self.df['Embarked'] = self.df['Embarked'].fillna(self.df['Embarked'].mode()[0])
        if 'Age' in self.df.columns:
            self.df['Age'] = self.df['Age'].fillna(self.df['Age'].median())
        if 'Fare' in self.df.columns:
            self.df['Fare'] = self.df['Fare'].fillna(self.df['Fare'].median())

    def feature_engineering(self):
        if 'Name' in self.df.columns:
            self.df['Title'] = self.df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
            self.df['Title'] = self.df['Title'].replace(
                ['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
            self.df['Title'] = self.df['Title'].replace({'Mlle': 'Miss', 'Ms': 'Miss', 'Mme': 'Mrs'})
        if 'Cabin' in self.df.columns:
            self.df['CabinKnown'] = self.df['Cabin'].notnull().astype(int)
        if 'FamilySize' not in self.df.columns and 'SibSp' in self.df.columns and 'Parch' in self.df.columns:
            self.df['FamilySize'] = self.df['SibSp'] + self.df['Parch'] + 1

    def drop_unnecessary_columns(self):
        cols_to_drop = ['Name', 'Ticket', 'Cabin', 'PassengerId']
        for col in cols_to_drop:
            if col in self.df.columns:
                self.df.drop(col, axis=1, inplace=True)

    def encode_features(self):
        cat_cols, _, _ = grab_col_names(self.df)
        binary_cols = [col for col in cat_cols if self.df[col].nunique() == 2]

        for col in binary_cols:
            # LabelEncoder'ı doğru kullanarak
            le = LabelEncoder()
            self.df[col] = le.fit_transform(self.df[col])

        cat_cols = [col for col in cat_cols if col not in binary_cols]
        self.df = one_hot_encoder(self.df, cat_cols, drop_first=True)

        remaining_object_cols = self.df.select_dtypes(include='object').columns.tolist()
        if remaining_object_cols:
            raise ValueError(f"Categorical columns not fully encoded: {remaining_object_cols}")

        if self.encoded_columns is None:
            self.encoded_columns = self.df.columns.tolist()

    def preprocess(self):
        self.handle_missing_values()
        self.feature_engineering()
        self.drop_unnecessary_columns()
        self.encode_features()

        if 'Survived' not in self.df.columns:
            raise ValueError("Target column 'Survived' is missing in the dataset.")

        X = self.df.drop('Survived', axis=1)
        y = self.df['Survived']
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def preprocess_test(self, encoded_columns):
        self.handle_missing_values()
        self.feature_engineering()
        self.drop_unnecessary_columns()
        self.encode_features()

        for col in encoded_columns:
            if col not in self.df.columns:
                self.df[col] = 0

        self.df = self.df[encoded_columns]
        return self.df
