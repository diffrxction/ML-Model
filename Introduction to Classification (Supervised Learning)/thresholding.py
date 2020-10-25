import numpy as np
from exam import hours_studied, calculated_coefficients, intercept

def log_odds(features, coefficients,intercept):
  return np.dot(features,coefficients) + intercept

def sigmoid(z):
    denominator = 1 + np.exp(-z)
    return 1/denominator

def predict_class(features, coefficients,intercept,threshold):
  calculated_log_odds = log_odds(features, coefficients, intercept)
  #return calculated_log_odds
  probabilities = sigmoid(calculated_log_odds)
  #return probabilities
  return np.where(probabilities >= threshold, 1, 0)
  
final_results = predict_class(hours_studied, calculated_coefficients, intercept, 0.5)
print(final_results)
