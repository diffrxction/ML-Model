Review

Seen how to implement a linear regression algorithm in Python, and how to use the linear regression model from scikit-learn. Learned that:

   - We can measure how well a line fits by measuring loss.
   - The goal of linear regression is to minimize loss.
   - To find the line of best fit, we try to find the b value (intercept) and the m value (slope) that minimize loss.
   - Convergence refers to when the parameters stop changing with each iteration.
   - Learning rate refers to how much the parameters are changed on each iteration.
   - We can use Scikit-learn’s LinearRegression() model to perform linear regression on a set of points.

These are important tools to have in your toolkit as you continue your exploration of data science.

As a starter, I’ve loaded in the [Boston housing dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_boston). The X values are the nitrogen oxides concentration (parts per 10 million), and the y values the housing prices. Check if  regression is possible on these houses!
