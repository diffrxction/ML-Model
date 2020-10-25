import numpy as np
from exam import hours_studied, calculated_coefficients, intercept

def log_odds(features, coefficients, intercept):
  return np.dot(features,coefficients) + intercept

calculated_log_odds = log_odds(hours_studied, calculated_coefficients, intercept)
print(calculated_log_odds)
