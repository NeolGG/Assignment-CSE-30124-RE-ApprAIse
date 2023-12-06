#!/usr/bin/env python

# predictor

import sys
import csv
import pandas as pd
from joblib import load

if len(sys.argv) < 2:
    print("Usage: ./predict.py input_file.csv ")
    sys.exit(1)

input_filename = sys.argv[1]

def load_model(filename):
    return load(filename)

def predict_price(model, input_data):
    return model.predict(input_data )

if __name__ == "__main__":
    model = load_model('../models/kc_housingmodel.pkl')
    # Features and corresponding values for prediction

    values = []
    
    with open(input_filename, 'r') as file:
        reader = csv.reader(file)
        features = next(reader)
        for row in reader:
            values.append(row)

    data = [dict(zip(features, v)) for v in values]

    print(values)
    input_df = pd.DataFrame(data)
    
    predicted_prices = predict_price(model, input_df)

    for idx, price in enumerate(predicted_prices):
        print(f"Predicted Price for Property {idx+1}: ${price:,.2f}")

