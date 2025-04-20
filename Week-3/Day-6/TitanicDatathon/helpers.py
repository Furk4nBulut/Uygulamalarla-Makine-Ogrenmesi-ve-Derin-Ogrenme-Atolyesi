# helpers.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

LOW_QUANTILE = 0.05
UP_QUANTILE = 0.95
CAT_THRESHOLD = 10
CAR_THRESHOLD = 20
CORRELATION_THRESHOLD = 0.90
CAT_LENGTH = 10
NUM_METHOD = "median"
TARGET_COL = "Survived"

def check_df(dataframe):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(3))
    print("##################### Tail #####################")
    print(dataframe.tail(3))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.select_dtypes(include=np.number).quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

def grab_col_names(dataframe, cat_th=CAT_THRESHOLD, car_th=CAR_THRESHOLD):
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtype == "O"]
    num_but_cat = [col for col in dataframe.columns if
                   dataframe[col].nunique() < cat_th and dataframe[col].dtype != "O"]
    cat_but_car = [col for col in dataframe.columns if
                   dataframe[col].nunique() > car_th and dataframe[col].dtype == "O"]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in dataframe.columns if dataframe[col].dtype != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat and col != 'Survived']
    return cat_cols, cat_but_car, num_cols

def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({
        col_name: dataframe[col_name].value_counts(),
        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)
    }))
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.xticks(rotation=45)
        plt.show()

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.50, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)
    if plot:
        dataframe[numerical_col].hist(bins=50)
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show()
    print("#####################################")

def target_summary_with_cat(dataframe, target=TARGET_COL, categorical_col=None):
    if categorical_col:
        print(pd.DataFrame({
            "TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()
        }), end="\n\n\n")

def high_correlated_cols(dataframe, plot=False, corr_th=CORRELATION_THRESHOLD):
    corr = dataframe.select_dtypes(include=np.number).corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, cmap="RdBu", annot=True, fmt=".2f")
        plt.title("Feature Correlation Matrix")
        plt.show()
    return drop_list

def outlier_thresholds(dataframe, variable, low_quantile=LOW_QUANTILE, up_quantile=UP_QUANTILE):
    q1 = dataframe[variable].quantile(low_quantile)
    q3 = dataframe[variable].quantile(up_quantile)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return lower_bound, upper_bound

def check_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    return dataframe[(dataframe[col_name] > up_limit) | (dataframe[col_name] < low_limit)].any(axis=None)

def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    if dataframe[variable].dtype in ['int64', 'int32']:
        low_limit = round(low_limit)
        up_limit = round(up_limit)
    dataframe.loc[dataframe[variable] < low_limit, variable] = low_limit
    dataframe.loc[dataframe[variable] > up_limit, variable] = up_limit
    return dataframe

def missing_values_table(dataframe, na_name=False):
    na_columns = [col for col in dataframe.columns if dataframe[col].isnull().sum() > 0]
    n_miss = dataframe[na_columns].isnull().sum().sort_values(ascending=False)
    ratio = (dataframe[na_columns].isnull().sum() / dataframe.shape[0] * 100).sort_values(ascending=False)
    missing_df = pd.concat([n_miss, np.round(ratio, 2)], axis=1, keys=['n_miss', 'ratio'])
    print(missing_df, end="\n")
    if na_name:
        return na_columns

def rare_analyser(dataframe, target=TARGET_COL, cat_cols=None):
    if cat_cols is None:
        cat_cols = [col for col in dataframe.columns if dataframe[col].dtype == "O"]
    for col in cat_cols:
        print(col, ":", len(dataframe[col].value_counts()))
        print(pd.DataFrame({
            "COUNT": dataframe[col].value_counts(),
            "RATIO": dataframe[col].value_counts() / len(dataframe),
            "TARGET_MEAN": dataframe.groupby(col)[target].mean()
        }), end="\n\n\n")

def rare_encoder(dataframe, rare_perc):
    temp_df = dataframe.copy()
    rare_columns = [col for col in temp_df.columns if temp_df[col].dtype == 'O'
                    and (temp_df[col].value_counts() / len(temp_df) < rare_perc).any(axis=None)]
    for var in rare_columns:
        tmp = temp_df[var].value_counts() / len(temp_df)
        rare_labels = tmp[tmp < rare_perc].index
        temp_df[var] = np.where(temp_df[var].isin(rare_labels), 'Rare', temp_df[var])
    return temp_df

def label_encoder(dataframe, binary_col):
    labelencoder = LabelEncoder()
    dataframe[binary_col] = labelencoder.fit_transform(dataframe[binary_col])
    return dataframe

def one_hot_encoder(dataframe, categorical_cols, drop_first=False):
    return pd.get_dummies(dataframe, columns=categorical_cols, drop_first=drop_first)

def quick_missing_imp(dataframe, num_method="median", cat_length=CAT_LENGTH, target=TARGET_COL):
    num_cols = [col for col in dataframe.columns if dataframe[col].dtype != "O" and col != target]
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtype == "O"]
    for col in num_cols:
        if dataframe[col].isnull().sum() > 0:
            if num_method == "median":
                dataframe[col].fillna(dataframe[col].median(), inplace=True)
            elif num_method == "mean":
                dataframe[col].fillna(dataframe[col].mean(), inplace=True)
    for col in cat_cols:
        if dataframe[col].isnull().sum() > 0:
            dataframe[col].fillna(dataframe[col].mode()[0], inplace=True)
    return dataframe