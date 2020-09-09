from gradient_descent_funcs import gradient_descent
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heights.csv")

X = df["height"]
y = df["weight"]

b, m = gradient_descent(X,y,num_iterations=1000,learning_rate=0.0001)
y_predictions = [m*x + b for x in X]
new_y = [element * m + b for element in y]
plt.plot(X, y, 'o')
#plot your line here:
plt.plot(X, y_predictions)
plt.show()
