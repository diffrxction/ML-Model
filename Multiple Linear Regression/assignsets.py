import codecademylib3_seaborn
import pandas as pd

# import train_test_split
from sklearn.model_selection import train_test_split

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

x = df[[
    'bedrooms',
    'bathrooms',
    'size_sqft',
    'min_to_subway',
    'floor',
    'building_age_yrs',
    'no_fee',
    'has_roofdeck',
    'has_washer_dryer',
    'has_doorman',
    'has_elevator',
    'has_dishwasher',
    'has_patio',
    'has_gym',
]]

y = df[['rent']]

# x_train, y_train, x_test, y_test are split and fromed from the dataframe elements x and y. 
# train_size = 0.8 associates 80% of total data to training sets. (Max can be 1)
# test_size = 0.2 associates 20% of the data to 

x_train, x_test, y_train, y_test = train_test_split(x,y, train_size = 0.8, test_size = 0.2, random_state=6)

# To print shapes of each set, we use function .shape

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

# Output

#(2831, 14)
#(708, 14)
#(2831, 1)
#(708, 1)

