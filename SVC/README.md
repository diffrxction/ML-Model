Here are some of the major takeaways from this lesson on SVMs:

- SVMs are supervised machine learning models used for classification.
- An SVM uses support vectors to define a decision boundary. Classifications are made by comparing unlabeled points to that decision boundary.
- Support vectors are the points of each class closest to the decision boundary. The distance between the support vectors and the decision boundary is called the margin.
- SVMs attempt to create the largest margin possible while staying within an acceptable amount of error.
- The C parameter controls how much error is allowed. A large C allows for little error and creates a hard margin. A small C allows for more error and creates a soft margin.
- SVMs use kernels to classify points that aren’t linearly separable.
- Kernels transform points into higher dimensional space. A polynomial kernel transforms points into three dimensions while an rbf kernel transforms points into infinite dimensions.
- An rbf kernel has a gamma parameter. If gamma is large, the training data is more relevant, and as a result overfitting can occur.
