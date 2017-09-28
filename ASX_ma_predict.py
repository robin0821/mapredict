# The code intents to using Scikit-Learn to predict whether a transaction will happen based on machine learning from past transactions
# Random Forest Classification is used for machine learning, and Pandas was used for preparing the data.

import pandas as pd


# Import and prepare the data

raw = pd.read_excel(r"FY18_Features.xlsx", sheetname="Sheet1", na_values=['NM', '(Invalid Identifier)'], index_col='Ticker')
raw_data = pd.read_excel(r"ml_raw_data.xlsx", sheetname="Sheet1")
raw_data = raw_data.replace(to_replace=['BUY', 'SELL', 'BUY&SELL'], value='DEAL')
X = raw_data.iloc[:,1:12].values
X_test = raw.iloc[:,0:11].values
y = raw_data.iloc[:,12].values
ticker = raw.index
col = raw.columns

# Get shape informaiton of the feature_matrix
X_test.shape, X.shape

# Converting categorical data into numerical
from sklearn.preprocessing import LabelEncoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X = sc_X.fit_transform(X)
X_test = sc_X.transform(X_test)

# Training the machine learning
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 0)
classifier.fit(X, y)

# Predict based on machine learning
y_pred = classifier.predict(X_test)

# Combine the Feature matrix and Prediction result and write to excel format.
result = pd.DataFrame(data=X_test, index=ticker, columns=col)
result['Predict'] = y_pred
result.to_excel(r"C:\EY\Industry Concentration\ASX-Financials\result.xlsx")




