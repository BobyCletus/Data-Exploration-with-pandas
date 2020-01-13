import pandas as pd
housing_data = pd.read_csv('melb_data.csv')

import numpy as np

new_width=300

pd.set_option('display.width', new_width)

np.set_printoptions(linewidth=new_width)

pd.set_option('display.max_columns',21)

# checking all the variables in the data set

print(housing_data.columns)

# drop houses with missing values from the data set
# easiest option to handle missing values

housing_data = housing_data.dropna(axis = 0)
print(housing_data.head(50))

# Selecting the prediction target (Y)

Y = housing_data.Price
print(Y)

# selecting important variables that determine house price(Y)

housing_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
print(housing_features)
X = housing_data[housing_features]

# quick review of some statistical features of the data

print(X.describe())
print(X.head(10))
print(X.tail(10))

# Model building with Scipy

import sklearn
from sklearn.tree import DecisionTreeRegressor

# Define model and specify a number for random_state to ensure same result each run

housing_model = DecisionTreeRegressor(random_state = 1)
print(housing_model)  # MSE (mean square error)

# Fit Model

housing_model.fit(X,Y)
print('making predictions for the first 10 houses:')
print(X.head(10))   # actual
print('The predictions are')
print(housing_model.predict(X.head(10)))


