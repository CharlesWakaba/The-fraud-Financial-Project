import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('creditcard.csv')

# Basic information
print(df.info())

# Summary statistics
print(df.describe())

# Class distribution
fraud_dist = df['Class'].value_counts(normalize=True)
print("Class distribution:")
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

# Compare features for fraudulent and non-fraudulent transactions
for feature in ['V1', 'V2', 'V3', 'V4']:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Class', y=feature, data=df)
    plt.title(f'Distribution of {feature} by Class')
    plt.savefig(f'{feature}_distribution.png')
    plt.close()