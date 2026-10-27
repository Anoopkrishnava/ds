
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

diabetes_X = diabetes_X[:, np.newaxis, 2]

diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
diabetes_y_pred = regr.predict(diabetes_X_test)

print("Coefficients:", regr.coef_)
print("Intercept:", regr.intercept_)
print("Mean squared error: %.2f" %
      mean_squared_error(diabetes_y_test, diabetes_y_pred))
print("R^2 score: %.2f" %
      r2_score(diabetes_y_test, diabetes_y_pred))

plt.scatter(diabetes_X_test, diabetes_y_test, color="black")

sorted_idx = np.argsort(diabetes_X_test[:, 0])
plt.plot(diabetes_X_test[sorted_idx],
         diabetes_y_pred[sorted_idx],
         color="blue", linewidth=3)

plt.xlabel("BMI")
plt.ylabel("Diabetes progression")
plt.title("Linear Regression: BMI vs Diabetes Progression")
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()
