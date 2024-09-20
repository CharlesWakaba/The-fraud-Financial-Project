# Create a README file

echo "# Week 3: Data Collection & Exploration

This week focused on collecting data and performing exploratory data analysis.

## Accomplishments

- Collected and consolidated datasets
- Performed detailed Exploratory Data Analysis(EDA)
- Assessed data quality
- Began feature engineering
- Documented data characteristics and challenges

## Key Files

- data_exploration.py: Script for initial data exploration
- eda_report.ipynb: Jupyter notebook with detailed EDA

" > week3/README.md


**Key Findings:**

1. Severe class imbalance: Only 0.172% of transactions are fraudulent.
2. Transaction amounts range from 0 to 25,691.16, with a mean of 88.35.
3. Strong negative correlations between V2, V4, and V11 with the Class variable.
4. V1-V4 show clear separation between fraudulent and non-fraudulent transactions.

Feature Engineering Ideas:

1. Create time-based features (hour of day, day of week)
2. Normalize transaction amounts
3. Develop aggregate features based on customer behavior

Next Steps:

1. Address class imbalance using techniques like SMOTE or class weighting
2. Scale features using StandardScaler or RobustScaler
3. Split data into training, validation, and test sets
4. Begin model selection and training process
