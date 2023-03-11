import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

data = pd.read_csv('C:/Users/SAM/Python for DS/train-chennai-sale.csv')
print(data)