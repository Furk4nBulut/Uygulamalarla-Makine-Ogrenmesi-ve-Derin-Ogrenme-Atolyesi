import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import helpers


class DataPreprocessing:
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def preprocess(self):
        self.handle_outliers()  # Aykırı değerlerle başa çıkma
        self.handle_missing_values()  # Eksik verilerle başa çıkma
        self.feature_engineering()  # Özellik mühendisliği
        self.drop_unnecessary_columns()  # Gereksiz sütunları silme
        self.encode_features()  # Özellikleri kodlama
        return self.split_data()  # Veriyi eğitim ve test olarak ayırma

    def handle_outliers(self):
        """
        Aykırı değerler ile başa çıkma. Bu örnekte, IQR (Interquartile Range) kullanarak aykırı
        değerleri tespit edebiliriz. Ancak, kullanımınıza göre farklı metotlar eklenebilir.
        """
        Q1 = self.df.quantile(0.25)
        Q3 = self.df.quantile(0.75)
        IQR = Q3 - Q1

        # Aykırı değerleri tespit et
        condition = ~((self.df < (Q1 - 1.5 * IQR)) | (self.df > (Q3 + 1.5 * IQR))).any(axis=1)
        self.df = self.df[condition]

    def handle_missing_values(self):
        """
        Eksik verilerle başa çıkma. Bu örnekte, sayısal sütunlar için ortalama, kategorik sütunlar
        için ise en yaygın değeri kullanacağız.
        """
        # Sayısal sütunlar için eksik değerleri doldurma
        num_cols = self.df.select_dtypes(include=np.number).columns
        self.df[num_cols] = self.df[num_cols].fillna(self.df[num_cols].mean())

        # Kategorik sütunlar için eksik değerleri doldurma
        cat_cols = self.df.select_dtypes(include='object').columns
        for col in cat_cols:
            self.df[col] = self.df[col].fillna(self.df[col].mode()[0])

    def feature_engineering(self):
        """
        Özellik mühendisliği işlemleri. Burada bazı örnekler eklenebilir. Örneğin,
        yeni özellikler türetilebilir ya da dönüşüm yapılabilir.
        """
        # Örnek: Fiyatın yaşla ilişkisini incelemek için 'age' adlı yeni bir sütun ekleyebiliriz.
        self.df['age'] = 2023 - self.df['model_year']  # Bu, model yılına göre yaş hesaplama

    def drop_unnecessary_columns(self):
        """
        Gereksiz sütunları kaldırma.
        """
        drop_cols = ['id', 'engine', 'accident', 'transmission', 'ext_col', 'int_col', 'brand_model']
        for col in drop_cols:
            if col in self.df.columns:
                self.df.drop(columns=[col], inplace=True)

    def encode_features(self):
        """
        Kategorik verileri encode etme.
        """
        cat_cols, cat_but_car, num_cols = helpers.grab_col_names(self.df)

        binary_cols = [col for col in cat_cols if self.df[col].nunique() == 2]
        for col in binary_cols:
            self.df = helpers.label_encoder(self.df, col)

        cat_cols = [col for col in cat_cols if col not in binary_cols]

        # One hot encoding
        self.df = helpers.one_hot_encoder(self.df, cat_cols, drop_first=True)

        # Kalan object türündeki sütunlar varsa ek encode yap
        remaining_object_cols = self.df.select_dtypes(include='object').columns.tolist()
        if remaining_object_cols:
            print(f"Ekstra encoding uygulanıyor: {remaining_object_cols}")
            self.df = helpers.one_hot_encoder(self.df, remaining_object_cols, drop_first=True)

        # Son kontrol: Eğer hala object sütunlar varsa hata fırlat
        remaining_object_cols = self.df.select_dtypes(include='object').columns.tolist()
        if remaining_object_cols:
            raise ValueError(f"Kategorik sütunlar tam encode edilmedi: {remaining_object_cols}")

    def split_data(self):
        """
        Veriyi eğitim ve test olarak ayırma.
        Hedef değişkenin 'price' olduğundan emin olunmalı.
        """
        if 'price' not in self.df.columns:
            raise ValueError("Hedef değişken 'price' eksik.")

        X = self.df.drop('price', axis=1)
        y = self.df['price']

        # Eğitim ve test verilerini ayır
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test
