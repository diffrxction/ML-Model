# Review

Great work! Let’s review the concepts before you move on:

    Multiple Linear Regression uses two or more variables to make predictions about another variable:

y=b+m1x1+m2x2+...+mnxny = b + m_{1}x_{1} + m_{2}x_{2} + ... + m_{n}x_{n} y=b+m1​x1​+m2​x2​+...+mn​xn​

   - Multiple linear regression uses a set of independent variables and a dependent variable. It uses these variables to learn how to find optimal parameters. It takes a labeled dataset and learns from it. Once we confirm that it’s learned correctly, we can then use it to make predictions by plugging in new x values.
   - We can use scikit-learn’s LinearRegression() to perform multiple linear regression.
   - Residual Analysis is used to evaluate the regression model’s accuracy. In other words, it’s used to see if the model has learned the coefficients correctly.
   - Scikit-learn’s linear_model.LinearRegression comes with a .score() method that returns the coefficient of determination R² of the prediction. The best score is 1.0.

