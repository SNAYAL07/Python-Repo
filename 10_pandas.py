import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load the data from the CSV file
data = pd.read_csv('C:/Users/SAM/Python for DS/train-chennai-sale.csv')

# Split the data into training and test sets
train_data, test_data, train_target, test_target = train_test_split(data.drop(columns=['SALES_PRICE']), data['SALES_PRICE'], test_size=0.2)

# Create a Random Forest model
model = RandomForestRegressor(n_estimators=100)

# Train the model using the training data
model.fit(train_data, train_target)

# Make predictions on the test data
predictions = model.predict(test_data)

# Calculate the mean absolute error of the predictions
mae = mean_absolute_error(test_target, predictions)

print("Mean Absolute Error:", mae)

# Get the feature importances
importances = model.feature_importances_

# Get the column names
feature_names = train_data.columns

# Create a dataframe of feature importances
feature_importances = pd.DataFrame({'feature': feature_names, 'importance': importances})

# Sort the dataframe by feature importances
feature_importances.sort_values(by='importance', ascending=False, inplace=True)

# Print the feature importances
print(feature_importances)