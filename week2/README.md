# Week 2: Literature Review & Data Source Identification


Literature Review Summary:

1. "Deep Learning Approaches for Credit Card Fraud Detection" (2023)
   * Key finding: Convolutional Neural Networks (CNNs) outperform traditional methods, achieving 99.6% accuracy
   * Limitation: High computational requirements
2. "Ensemble Methods for Real-time Fraud Detection" (2022)
   * Key finding: Combination of Random Forest, XGBoost, and LightGBM improves F1-score by 7%
   * Advantage: Better generalization across different types of fraud
3. "Graph Neural Networks for Anti-Money Laundering" (2024)
   * Key finding: GNNs capture complex transaction patterns, improving detection of sophisticated schemes by 25%
   * Challenge: Requires high-quality transaction network data

Selected Datasets:

1. Credit Card Fraud Detection (Kaggle)
   * 284,807 transactions, 492 frauds
   * Features: Time, Amount, 28 anonymized features (V1-V28)
   * Link: [https://www.kaggle.com/mlg-ulb/creditcardfraud](https://www.kaggle.com/mlg-ulb/creditcardfraud)
2. Synthetic Financial Datasets for Fraud Detection (Kaggle)
   * 6,362,620 transactions, 8,213 frauds
   * Features: step, type, amount, nameOrig, oldbalanceOrg, newbalanceOrig, nameDest, oldbalanceDest, newbalanceDest, isFraud, isFlaggedFraud
   * Link: [https://www.kaggle.com/ntnu-testimon/paysim1](https://www.kaggle.com/ntnu-testimon/paysim1)
