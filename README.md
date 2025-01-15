# data-science-student-exam-performance

## Project Overview
This project analyzes and models student performance data to explore the relationships between various demographic and academic factors. The dataset provides scores for math, reading, and writing, along with demographic and preparation details. The analysis includes data preprocessing, exploratory data analysis (EDA), predictive modeling, and result visualization.

## Folder Structure
```
project-directory/
├── data/
│   ├── StudentsPerformance.csv        # Raw dataset
│   ├── cleaned_dataset.csv            # Processed dataset
├── scripts/
│   ├── 01_preprocessing.py            # Data preprocessing script
│   ├── 02_eda.py                      # EDA and visualizations script
│   ├── 03_modeling.py                 # Modeling and prediction script
│   ├── 04_visualization.py            # Visualization of results
├── outputs/
│   ├── eda_summary.txt                # EDA summary results
│   ├── plots/                         # Visualizations directory
│   ├── model.pkl                      # Trained model file
│   ├── evaluation.txt                 # Model evaluation metrics
├── README.md                          # Project documentation
```

## Usage
1. Clone the repository and navigate to the project directory.
2. Ensure all dependencies are installed (see the Requirements section).
3. Run the scripts in the following order:
    - `python scripts/01_preprocessing.py`: Cleans and preprocesses the dataset.
    - `python scripts/02_eda.py`: Performs exploratory data analysis and generates visualizations.
    - `python scripts/03_modeling.py`: Trains a model and evaluates its performance.
    - `python scripts/04_visualization.py`: Visualizes model results.
4. View the outputs in the `outputs/` folder.

## Requirements
- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- joblib

Install dependencies using the following command:
```bash
pip install -r requirements.txt
```

## Acknowledgments
- **Dataset Name**: Students Performance in Exams
- **Dataset Author**: Jakki Seshapanpu
- **Dataset Source**: [Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)