# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BrjxOimvCdtfuYbY-Bi9bUkLmiHmlTFa
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/content/drive/MyDrive/bank-additional-full.csv'
data = pd.read_csv(file_path)

# Check for missing values
print(data.isnull().sum())

# Perform one-hot encoding for categorical variables
data_encoded = pd.get_dummies(data, drop_first=True)

# Obtain the column names after one-hot encoding
column_names = data_encoded.columns

print(column_names)

# Split each column name by semicolon and extract the last element as the actual column name
column_names = [col.split(';')[-1] for col in column_names]

# Remove any leading or trailing whitespaces from column names
column_names = [col.strip() for col in column_names]

print(data_encoded.columns)

# Assuming the target variable name is 'y'
data_encoded = data_encoded.rename(columns={data_encoded.columns[0]: 'y'})

# Define the feature matrix X (excluding the target variable column)
X = data_encoded.drop('y', axis=1)

# Define the target vector y
y = data_encoded['y']

# Assuming 'data_encoded' is your DataFrame containing the dataset
# Extract the target variable column
y = data_encoded['y']

# Ensure the target variable is encoded as 0s and 1s (if not already)
# For example, if 'yes' and 'no' are the labels, we can encode 'yes' as 1 and 'no' as 0
y_binary = y.map({'yes': 1, 'no': 0})

# Convert the target variable column into a 1-dimensional array
y_train = y_binary.values

# Verify the shape of y_train
print(y_train.shape)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Split the data into features (X) and target variable (y)
X = data_encoded.drop('y', axis=1)
y = data_encoded['y']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the logistic regression model
model = LogisticRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Example: Predict on the test set
y_pred = model.predict(X_test)

# Example: Evaluate the model
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)