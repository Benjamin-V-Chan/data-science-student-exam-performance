# 03_modeling.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def model_performance(input_path, model_output, eval_output):
    data = pd.read_csv(input_path)
    features = data.drop(columns=['math score'])
    target = data['math score']
    
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    
    mse = mean_squared_error(y_test, predictions)
    with open(eval_output, 'w') as f:
        f.write(f"Mean Squared Error: {mse}\n")
    
    import joblib
    joblib.dump(model, model_output)

if __name__ == "__main__":
    model_performance("data/cleaned_dataset.csv", "outputs/model.pkl", "outputs/evaluation.txt")
