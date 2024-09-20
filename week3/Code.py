echo "import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def explore_data(data_path):
    df = pd.read_csv(data_path)
    
    # Basic information
    print(df.info())
    print(df.describe())
    
    # Class distribution
    fraud_dist = df['Class'].value_counts(normalize=True)
    print('Class distribution:')
    print(fraud_dist)
    
    # Visualize transaction amounts
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Amount'], kde=True, log_scale=True)
    plt.title('Distribution of Transaction Amounts (Log Scale)')
    plt.xlabel('Amount')
    plt.ylabel('Frequency')
    plt.savefig('amount_distribution.png')
    plt.close()
    
    # Correlation matrix
    corr_matrix = df.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, cmap='coolwarm', annot=False)
    plt.title('Correlation Matrix of Features')
    plt.savefig('correlation_matrix.png')
    plt.close()

if __name__ == '__main__':
    explore_data('creditcard.csv')" > week3/data_exploration.py
