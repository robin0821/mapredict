# Using past financial indicator and transaction records of ASX listed companies to train and test the robustness of the model

import pandas as pd
import numpy as np

# Import training and testing data
raw_data = pd.read_excel(r"ml_raw_data.xlsx", sheetname="Sheet1")

# Convert the categories to ONLY two - transaction happended and not happended
raw_data = raw_data.replace(to_replace=['BUY', 'SELL', 'BUY&SELL'], value='DEAL')

# Preparing the Feature matrix input
X = raw_data.iloc[:,1:12].values

# Preparing the dependent variable
y = raw_data.iloc[:,12].values

# Converting categorical variable into numberical variable
from sklearn.preprocessing import LabelEncoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Split the data between train dataset and test dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Train the machine learning algorithum
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 300, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting on test dataset
y_pred = classifier.predict(X_test)

# Generate confusion matrix to test the robustness of the model
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm



