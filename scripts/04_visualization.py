# 04_visualization.py
import pandas as pd
import matplotlib.pyplot as plt

def visualize_results(eval_path, plot_output_dir):
    with open(eval_path, 'r') as f:
        eval_data = f.read()
    
    print("Evaluation Results:")
    print(eval_data)
    
    # Example placeholder visualization
    plt.bar(["MSE"], [float(eval_data.split(": ")[1])])
    plt.title("Model Evaluation Metric")
    plt.savefig(f"{plot_output_dir}/model_evaluation_metric.png")
    plt.close()

if __name__ == "__main__":
    visualize_results("outputs/evaluation.txt", "outputs/plots")
