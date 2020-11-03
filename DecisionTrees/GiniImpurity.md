### Gini Impurity\
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
