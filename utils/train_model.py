"""
    Simple file to create a sklearn model for deployment in our API

    Author: Explore Data Science Academy

    Description: This script is responsible for training a simple linear
    regression model which is used within the API for initial demonstration
    purposes.

"""

# Dependencies
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Fetch training data and preprocess for modeling
train = pd.read_csv('./data/df_train.csv')

y_train = train[['load_shortfall_3h']]
X_train = train[['Madrid_temp', 'Barcelona_temp_min', 'Bilbao_pressure', 'Seville_temp', 'Valencia_wind_speed']]
X_train.fillna(0,inplace=True)

# Fit model
lm_regression = LinearRegression(normalize=True)
print ("Training Model...")
lm_regression.fit(X_train, y_train)
lm_regression.predict(X_train.loc[:5,])


# Pickle model for use within our API
save_path = '../assets/trained-models/linear_model.pkl'
print (f"Training completed. Saving model to: {save_path}")
pickle.dump(lm_regression, open(save_path,'wb'))
