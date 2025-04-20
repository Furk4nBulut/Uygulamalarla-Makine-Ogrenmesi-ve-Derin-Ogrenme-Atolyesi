import config
from dataset import DataLoader
from data_preprocessing import DataPreprocessing
from models import ModelEvaluator

def main():
    data_loader = DataLoader(config.TRAINING_DATA_PATH, config.TESTING_DATA_PATH)
    combined_df = data_loader.get_data()

    preprocessor = DataPreprocessing(combined_df)
    X_train, X_test, y_train, test_ids = preprocessor.preprocess()

    evaluator = ModelEvaluator(output_dir="predictions") # Specify the output directory
    X_train_split, X_test_split, y_train_split, y_test_split = evaluator.evaluate_models(X_train, y_train)

    # Train the best model and generate predictions on the actual test set
    evaluator.train_and_predict(X_train, y_train, X_test, test_ids, output_file="submission.csv")

if __name__ == "__main__":
    main()