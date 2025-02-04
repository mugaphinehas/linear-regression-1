# -*- coding: utf-8 -*-
"""DATASCIENCEASSIGNMENT 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hZeMxVNzlWzp6ebyq2NXeCDps4pkvclL
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("/content/road_accidents_updated.csv")

# Checking the dataset
# The target variable 'Accident_Happened' should be assigned to 'y'
y = df['Accident_Happened']
# The rest of the features should be assigned to 'X'
X = df.drop('Accident_Happened', axis=1)

# Transforming categorical features in X using OneHotEncoder
# (Assuming some features in X are categorical)
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
X_transformed = encoder.fit_transform(X)

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

# Initializing the Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)

# X_train is already a dense array after OneHotEncoding, no need for toarray()
model.fit(X_train, y_train)

# Predicting the answers for the test set
# X_test should also be transformed using the same encoder
y_pred = model.predict(X_test)
# Evaluating the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

conditions = ["10/1/2024", "6:15", "Snow", "Urban Road", "50km/h", "Bicycle", "28", "No"]

# Transform the conditions using the SAME OneHotEncoder used for training
# Create a DataFrame for the conditions to match the training data format
conditions_df = pd.DataFrame([conditions], columns=X.columns)  # Assuming 'X' still has the original column names
conditions_enc = encoder.transform(conditions_df)  # Use the fitted encoder to transform

predictions = model.predict(conditions_enc)  # Pass the transformed conditions to the model

# The prediction will be the raw class label (0 or 1 for Accident_Happened)
if predictions[0] ==1:
   print ("accident will happen")
else:
  print("accident will not happen")
print(f"Predicted Answer: {predictions[0]}")