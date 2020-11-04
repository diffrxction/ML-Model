### Gini Impurity
To find the Gini impurity, start at 1 and subtract the squared percentage of each label in the set. 
For example, if a data set had three items of class A and one item of class B, the Gini impurity of the set would be

  - 1 - (3/4)^2 - (1/4)^2
  
```python
from collections import Counter

labels = ["unacc", "unacc", "acc", "acc", "good", "good"]

impurity = 1
label_counts = Counter(labels)
print(label_counts)

for label in label_counts:
  probability_of_label = label_counts[label] / len(labels)
  impurity -= (probability_of_label ** 2)

print(impurity)
```
### As a function:
```python

def gini(dataset):
  impurity = 1
  label_counts = Counter(dataset)
  for label in label_counts:
    prob_of_label = label_counts[label] / len(dataset)
    impurity -= prob_of_label ** 2
  return impurity

```

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Weighted Information Gain

Concept : 
- A set of cases with 3 good (pure, correct) cases and 3 impure cases has an impurity of 0.5.
- Similarly, a set with one good case and one impure case also has an impurity of 0.5.
- Cleaning first case requires more effort, as the 3 impure cases may affect more than the one impure case.
- Hence, we can say that the size of set is also relevant in decision trees. So to implement this, instead of simply subtracting the impurity of each set, we’ll subtract the weighted impurity of each of the split sets. If the data before the split contained 20 items and one of the resulting splits contained 2 items, then the weighted impurity of that subset would be 2/20 * impurity. We’re lowering the importance of the impurity of sets with few elements.

```python
from collections import Counter

cars = [['med', 'low', '3', '4', 'med', 'med'], ['med', 'vhigh', '4', 'more', 'small', 'high'], ['high', 'med', '3', '2', 'med', 'low'], ['med', 'low', '4', '4', 'med', 'low'], ['med', 'low', '5more', '2', 'big', 'med'], ['med', 'med', '2', 'more', 'big', 'high'], ['med', 'med', '2', 'more', 'med', 'med'], ['vhigh', 'vhigh', '2', '2', 'med', 'low'], ['high', 'med', '4', '2', 'big', 'low'], ['low', 'low', '2', '4', 'big', 'med']]

car_labels = ['acc', 'acc', 'unacc', 'unacc', 'unacc', 'vgood', 'acc', 'unacc', 'unacc', 'good']

def split(dataset, labels, column):
    data_subsets = []
    label_subsets = []
    counts = list(set([data[column] for data in dataset]))
    counts.sort()
    for k in counts:
        new_data_subset = []
        new_label_subset = []
        for i in range(len(dataset)):
            if dataset[i][column] == k:
                new_data_subset.append(dataset[i])
                new_label_subset.append(labels[i])
        data_subsets.append(new_data_subset)
        label_subsets.append(new_label_subset)
    return data_subsets, label_subsets

def gini(dataset):
  impurity = 1
  label_counts = Counter(dataset)
  for label in label_counts:
    prob_of_label = label_counts[label] / len(dataset)
    impurity -= prob_of_label ** 2
  return impurity

def information_gain(starting_labels, split_labels):
  info_gain = gini(starting_labels)
  for subset in split_labels:
    info_gain -= gini(subset) * len(subset) / len(starting_labels)
  return info_gain

for i in range(6):
  split_data, split_labels = split(cars, car_labels, i)
  print(information_gain(car_labels, split_labels))
```
The Counter function isn't mentioned in the Codecademy skill path.

