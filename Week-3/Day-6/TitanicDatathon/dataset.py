import pandas as pd
import config


class DataLoader:
    def __init__(self, training_data_path, testing_data_path):
        self.training_data_path = training_data_path
        self.testing_data_path = testing_data_path
        print("Initializing DataLoader...")

    def get_data(self):
        print("Loading data...")
        # Eğitim ve test verilerini ayrı ayrı yükle
        train_df = pd.read_csv(self.training_data_path)
        test_df = pd.read_csv(self.testing_data_path)
        print("Data loaded successfully.")

        # Eğitim ve test verilerini ayrı ayrı döndür
        return train_df, test_df