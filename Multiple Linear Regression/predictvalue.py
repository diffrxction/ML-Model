# Predicting apartment rent from given dataset.
import codecademylib3_seaborn
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Read csv and assign it to streeteasy.

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")
# Make a proper dataframe using pandas .Dataframe method.

df = pd.DataFrame(streeteasy)

# x includes the following parameters and their data.
x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]

# Simiarly, y includes the following parameters and their data.
y = df[['rent']]

# We use 80% of data for training and 20% data for testing.
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

# We create a LinearRegression object as mlr.
mlr = LinearRegression()

# We then fir the training sets to mlr, which is the LinearRegression object.
mlr.fit(x_train, y_train)

# y_predict stores all the predictions made by the machine.
y_predict = mlr.predict(x_test)

# Here we have the data for an apartment. We know the parameters for bedrooms, bathrooms, etc. and store it in sonny_apartment.
sonny_apartment = [[1, 1, 620, 16, 1, 98, 1, 0, 1, 0, 0, 1, 1, 0]]

# Then we use the .predict method to store the predicted value within a variable. 
# Tip to self: Remember that this variable stores the predicted value in the format `[[value]]`, therefore to get the needed value we use type conversion/casting.

predict = mlr.predict(sonny_apartment)
print("Predicted Rent: $%.2f " % predict)

#This is a mock test for an estimated rent one would pay for such an apartment in Manhattan.
trial_apartment = [[1, 1, 750, 8, 2, 20, 1, 0, 0, 0, 0, 0, 0, 0]]
predict2 = mlr.predict(trial_apartment)
print("Rent for mock apartment $%.2f" % predict2)

# Final Notes:
# This model can also use brooklyn, queens and other dataset csv files from elsewhere. This is just what I chose when learning on Codecademy.
# The steps for multiple linear regression in scikit-learn are identical to the steps for simple linear regression. 
# Just like simple linear regression, we need to import LinearRegression from the linear_model module.
# mlr = LinearRegression()
# mlr.fit(x_train, y_train) 
# The above statement finds the coefficients and the intercept value.
# y_predicted = mlr.predict(x_test)
# The above statement is how we take values calculated by `.fit()` and the `x` values, plug them into the multiple linear regression equation, and calculate the predicted y values.
