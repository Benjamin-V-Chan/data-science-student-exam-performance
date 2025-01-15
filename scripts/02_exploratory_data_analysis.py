# 02_eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(input_path, summary_output, plot_output_dir):
    data = pd.read_csv(input_path)
    
    # Summary statistics
    summary = data.describe()
    summary.to_csv(summary_output)
    
    # Visualizations
    sns.histplot(data['math score'], kde=True)
    plt.title("Math Score Distribution")
    plt.savefig(f"{plot_output_dir}/math_score_distribution.png")
    plt.close()
    
    sns.pairplot(data[['math score', 'reading score', 'writing score']])
    plt.savefig(f"{plot_output_dir}/score_pairplot.png")
    plt.close()

if __name__ == "__main__":
    perform_eda("data/cleaned_dataset.csv", "outputs/eda_summary.txt", "outputs/plots")
