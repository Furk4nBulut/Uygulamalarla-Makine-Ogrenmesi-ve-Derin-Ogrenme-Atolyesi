import config
from dataset import DataLoader
from data_preprocessing import DataPreprocessing
from models import ModelEvaluator

import config
from dataset import DataLoader
from data_preprocessing import DataPreprocessing
from models import ModelEvaluator

def main():
    data_loader = DataLoader(config.TRAINING_DATA_PATH, config.TESTING_DATA_PATH)
    combined_df = data_loader.get_data()

    preprocessor = DataPreprocessing(combined_df)

    # 1) Eğitim/validation için
    X_train, X_val, y_train, y_val = preprocessor.preprocess()

    # 2) Sadece gerçek test (submission) verisi için
    X_test_submission, test_ids = preprocessor.preprocess(is_test_only=True)
    # → preprocess() içinde id zaten drop edildi, burada tekrar DROP ETME

    evaluator = ModelEvaluator(output_dir="predictions")
    evaluator.evaluate_models(X_train, y_train)

    # 3) Final modelini eğit ve tahminleri üret
    evaluator.train_and_predict(
        X_train,
        y_train,
        X_test_submission,
        test_ids,
        output_file="submission.csv"
    )

if __name__ == "__main__":
    main()