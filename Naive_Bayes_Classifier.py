from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.datasets import load_iris

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=40
)

gnb = GaussianNB()
gnb.fit(x_train, y_train)

y_pred = gnb.predict(x_test)

acc = metrics.accuracy_score(y_test, y_pred)
report = metrics.classification_report(
    y_test, y_pred, target_names=iris.target_names
)

print(acc)
print(report)