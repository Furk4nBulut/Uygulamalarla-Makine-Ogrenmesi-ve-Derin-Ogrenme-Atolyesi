import config
from dataset import DataLoader
from data_preprocessing import DataPreprocessing
from models import ModelEvaluator

def main():
    # Load data
    data_loader = DataLoader(config.TRAINING_DATA_PATH, config.TESTING_DATA_PATH)
    train_data, test_data = data_loader.get_data()

    # Preprocess training data
    train_preprocessor = DataPreprocessing(train_data)
    X_train, X_test, y_train, y_test = train_preprocessor.preprocess()
    encoded_columns = train_preprocessor.encoded_columns

    # Preprocess test data
    test_preprocessor = DataPreprocessing(test_data)
    X_test_processed = test_preprocessor.preprocess_test(encoded_columns)

    # Get PassengerId for submission
    passenger_ids = test_data["PassengerId"] if "PassengerId" in test_data.columns else range(1, len(test_data) + 1)

    # Evaluate models on training data
    evaluator = ModelEvaluator()
    results_df = evaluator.evaluate_models(X_train, y_train, problem_type="classification")

    # 1️⃣ En iyi modeli seç (F1 Score'a göre) ve submission.csv olarak kaydet
    best_model_row = results_df.sort_values(by="F1 Score", ascending=False).iloc[0]
    best_model_name = best_model_row["Model"]
    best_model_score = best_model_row["F1 Score"]

    print(f"\n🏆 Best model based on F1 Score: {best_model_name} ({best_model_score:.4f})")

    # Skoru dosyaya yaz
    with open("best_model_score.txt", "w") as f:
        f.write(f"Best Model: {best_model_name}\n")
        f.write(f"F1 Score: {best_model_score:.4f}\n")
    # Güvenlik için tekrar test verisinden 'Survived' at
    if 'Survived' in X_test_processed.columns:
        X_test_processed.drop(columns=['Survived'], inplace=True)

    # Tahmin ve submission.csv oluştur
    evaluator.train_and_predict(
        X_train=X_train,
        y_train=y_train,
        X_test=X_test_processed,
        passenger_ids=passenger_ids,
        model_name=best_model_name,
        output_file="submission.csv",
        problem_type="classification"
    )

    # 2️⃣ Tüm modellerin çıktısını ayrı ayrı dosyalara kaydet
    for model_name, _ in evaluator.models:
        filename = f"submission_{model_name}.csv"
        print(f"\n📝 Generating submission for: {model_name}")
        evaluator.train_and_predict(
            X_train=X_train,
            y_train=y_train,
            X_test=X_test_processed,
            passenger_ids=passenger_ids,
            model_name=model_name,
            output_file=filename,
            problem_type="classification"
        )

if __name__ == "__main__":
    main()
