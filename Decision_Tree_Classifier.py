from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import metrics

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3
)

clf = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=4,
    min_samples_leaf=2
)

clf = clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)

report = metrics.classification_report(
    y_test, y_pred, target_names=iris.target_names
)
print(report)

from sklearn import tree
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(25, 20))
_ = tree.plot_tree(
    clf,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True
)

plt.show()