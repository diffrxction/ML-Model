**_NOTE:_** I have taken most of the lines in this file from Codecademy's ML track but have added notes for myself at the end as my pro subscription ends soon.
## Evaluating the Model's Accuracy

When trying to evaluate the accuracy of our multiple linear regression model, one technique we can use is Residual Analysis.

The difference between the actual value y, and the predicted value ŷ is the residual e. The equation is:

e=y−y^e = y - \hat{y}e=y−y^​

In the StreetEasy dataset, y is the actual rent and the ŷ is the predicted rent. The real y values should be pretty close to these predicted y values.

sklearn‘s linear_model.LinearRegression comes with a .score() method that returns the coefficient of determination R² of the prediction.
The coefficient R² is defined as:

  1-(u/v)

where,
u is equal to
```python
((y - y_predict) ** 2).sum()
```
and v is equal to
```python
((y - y.mean()) ** 2).sum()
```
For example, say we are trying to predict rent based on the size_sqft and the bedrooms in the apartment and the R² for our model is 0.72 — that means that all the x variables (square feet and number of bedrooms) together explain 72% variation in y (rent).

Now let’s say we add another x variable, building’s age, to our model. By adding this third relevant x variable, the R² is expected to go up. Let say the new R² is 0.95. 
This means that square feet, number of bedrooms and age of the building together explain 95% of the variation in the rent.

The best possible R² is 1.00 (and it can be negative because the model can be arbitrarily worse). Usually, a R² of 0.70 is considered good.

In my code, to evaluate the accuracy, I can add the following lines after creating an object for the LinearRegression() model (mlr in my case).

```python

print(mlr.score(x_train, y_train))

print(mlr.score(x_test, y_test))

```
