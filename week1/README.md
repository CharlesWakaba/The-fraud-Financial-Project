
# Virtual environment creation

python -m venv venv
source venv/bin/activate

# Install required packages

pip install pandas numpy scikit-learn tensorflow matplotlib seaborn jupyter
pip freeze > requirements.txt

# Git repository setup

git init
git add .
git commit -m "Initial project setup"
git branch -M main
git remote add origin https://github.com/yourUsername/financial-fraud-detection.git
git push -u origin main
