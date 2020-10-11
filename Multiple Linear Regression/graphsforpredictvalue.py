import codecademylib3_seaborn
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]

y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

lm = LinearRegression()

model=lm.fit(x_train, y_train)

y_predict = lm.predict(x_test)

#To find the coefficients of the Linear Regression plot, we use :
print(lm.coef_)
# This is the new part after predict.py
# alpha represents the opacity of scattered points (Maximum value = 1).
# Tip to self: Format for graph s is (x, y, alpha(optional))
plt.scatter(y_test, y_predict, alpha=0.2)

# These are methods to add labels to the graph.
plt.xlabel("Actual Rent Cost: Yi")
plt.ylabel("Predicted Rent: Y")

# Adds title to graph
plt.title("Actual Rent vs Predicted Rent in Manhattan")

# Essential method for displaying graph.
plt.show()
