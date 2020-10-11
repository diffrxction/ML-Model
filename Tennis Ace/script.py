import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:

df = pd.read_csv("tennis_stats.csv")
#print(df.head())

# perform exploratory analysis here:

x = df[['BreakPointsOpportunities']]
y = df[['Winnings']]

#plt.scatter(y,x, alpha=0.2)
#plt.show()

x = df[['BreakPointsFaced']]
y = df[['Winnings']]

#plt.scatter(y,x, alpha=0.4)
#plt.show()

x = df[['FirstServeReturnPointsWon']]
y = df[['Winnings']]

#plt.scatter(y,x, alpha=0.2)
#plt.show()

## perform single feature linear regressions here:

features = df[['FirstServeReturnPointsWon']]
outcome = df[['Winnings']]

features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8)

model = LinearRegression()
model.fit(features_train,outcome_train)

#print(model.score(features_test,outcome_test))

prediction = model.predict(features_test)

#plt.scatter(outcome_test,prediction, alpha=0.5)
#plt.show()

features = df[['BreakPointsOpportunities']]
outcome = df[['Winnings']]

features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8)

model = LinearRegression()
model.fit(features_train,outcome_train)

#print(model.score(features_test,outcome_test))

prediction = model.predict(features_test)

#plt.scatter(outcome_test,prediction, alpha=0.5)
#plt.show()

## perform two feature linear regressions here:


features = df[['BreakPointsOpportunities', 'FirstServeReturnPointsWon']]
outcome = df[['Winnings']]

features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8)

model = LinearRegression()
model.fit(features_train,outcome_train)

print(model.score(features_test,outcome_test))

prediction = model.predict(features_test)

plt.scatter(outcome_test,prediction, alpha=0.2)
plt.show()

## perform multiple feature linear regressions here:

features = df[['BreakPointsOpportunities', 'FirstServeReturnPointsWon']]
outcome = df[['Winnings']]

features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8)

model = LinearRegression()
model.fit(features_train,outcome_train)

print(model.score(features_test,outcome_test))

prediction = model.predict(features_test)

plt.scatter(outcome_test,prediction, alpha=0.2)
plt.show()

# Most efficient model

features = df[['FirstServe','FirstServePointsWon','FirstServeReturnPointsWon',
'SecondServePointsWon','SecondServeReturnPointsWon','Aces',
'BreakPointsConverted','BreakPointsFaced','BreakPointsOpportunities',
'BreakPointsSaved','DoubleFaults','ReturnGamesPlayed','ReturnGamesWon',
'ReturnPointsWon','ServiceGamesPlayed','ServiceGamesWon','TotalPointsWon',
'TotalServicePointsWon']]
outcome = df[['Winnings']]

features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8)

model = LinearRegression()
model.fit(features_train,outcome_train)

print(model.score(features_test,outcome_test))

prediction = model.predict(features_test)

plt.scatter(outcome_test,prediction, alpha=0.2)
plt.show()
