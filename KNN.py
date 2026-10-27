from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25
)

model = KNeighborsClassifier(n_neighbors=5)              #Creates the KNN classifier with \(K=5\).
model.fit(x_train, y_train)                     #Trains the model using the training data.

y_prediction = model.predict(x_test)          # Predicts classes for the test data.

print("Accuracy = ", metrics.accuracy_score(y_test, y_prediction))   #Calculates the proportion of correct predictions.

sample = [[2, 2, 2, 2]]
pred = model.predict(sample)[0]

print("New Sample belongs to ", iris.target_names[pred])

plt.subplot(1,2,1)
plt.scatter(x_test[:,0],x_test[:,1],c=y_prediction)
plt.title("Predicted classification")
plt.xlabel("Petal length")
plt.ylabel("Petal width")
plt.subplot(1,2,2)
plt.scatter(x_test[:,0],x_test[:,1],c=y_test)
plt.title("Actual classification")
plt.xlabel("Petal length")
plt.ylabel("Petal width")
plt.show()