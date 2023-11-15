#!/usr/bin/env python

#creates model

import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from joblib import dump

if len(sys.argv) < 2:
    print("Usage: ./housing_model.py input_file.csv")
    sys.exit(1)

input_filename = sys.argv[1]

df = pd.read_csv(input_filename)

# Splitting data into features and target variable
X = df.drop("price", axis=1)
y = df["price"]

# Splitting data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating a linear regression model and training
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

#printing out values
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

dump(model, 'kc_housingmodel.pkl')



