# Trains a simple model and saves it to a file
# Dataset is the Iris dataset from sklearn
# Model is a random forest classifier

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report, confusion_matrix

# Load the iris dataset
iris = load_iris()
print(iris.feature_names)

X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the model
clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X_train, y_train)

# Save the model
import pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)
    
# Print some metrics
y_pred = clf.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))