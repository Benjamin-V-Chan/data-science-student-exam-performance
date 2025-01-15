# 01_preprocessing.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(input_path, output_path):
    data = pd.read_csv(input_path)
    
    # Handle missing values
    data = data.dropna()
    
    # Encode categorical variables
    label_enc = LabelEncoder()
    for col in ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']:
        data[col] = label_enc.fit_transform(data[col])
    
    # Save cleaned dataset
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess_data("data/StudentsPerformance.csv", "data/cleaned_dataset.csv")
