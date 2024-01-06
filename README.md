DLS Project

Project to improve upon the predictive capability of DL method (2002 tables) using machine and deep learning methods and extending the definition of "resources" to include cricketer "value" as well as grounds data.


Data used:

ODI cricket mens matches from Jan 2002 - Dec 2022

Cricketer data 

Grounds data


Code:

1.Data.ipynb 
Importing and formatting the data for the project (Match data, cricketer data and grounds data)

1a.Cricketer_Wiki.ipynb
Code to import the cricketer wiki data

2.Visualisation_preprocessing
Visualisation of the data, splitting into train val and test, processing target variable into categories and scaling and SMOTE data

data_formatting.py
Code to take in train, val and test datasets and return X and y values.  Also can perform sampling.

3.RF_model.ipynb
Random Forest model

4.SVM_model.ipynb
Support Vector Machine model

5.NN_mode.ipynb
Feedforward Neural Network model