# mapredict
Predict Mergers and Acquisitions by Machine Learning

The purpose of this excercise is to test whether a M&A transaction can be predicted. 

To full-fill this test, four steps are followed:

Step 1: Define variables and collect relavant data 
a. Financial data - There are c.1500+ publicly listed companies in ASX. All financial data including income statement, balance sheet, and cash flow statement were collected for the past 10 years (finanical year as end date of 30 June). Then, financial ratios are calculated based on the financial statements e.g., quick ratio, debt ratio, etc. 
b. Transaction data - Historic transaction data were collected of the publicly listed company above for the past 10 years. 

Step 2: Prepare data for analysis
a. Combining financial and transaction data - cause both financial and transaction data would be used as features for predicting. Though, in theory, other factors such as management mindset, personality, etc would also impact on transaction. However, due to the unattainability of the data. We would omit such factors.
b. Data cleansing - all missing data were omited to maximise the accuracy of the prediciton.
c. Label Encoding - there are categorical variables in the raw data such as types of transactions. By applying Scikit-learn's preprossessing 
d. Feature scaling - standardising data for more robust modelling.

Step 3: Train and test
a. Train and test split
b. Train model with historic data - Random Forest Classification is used for prediction.
c. Compare prediction with historic value
d. Test accuracy with confustion matrix. 

Step 4: Predict FY18 transaction
a. Get FY17 data from ASX - as the financial year ends on 30 Jun. We can get all financial data for FY17 now. 
b. Predict FY18 transactions

