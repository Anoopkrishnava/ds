
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X = diabetes_X[:, [0, 2]]

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

plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
plt.scatter(diabetes_X_test[:, 0], diabetes_y_test,
            color='red', marker='o', label='Actual', alpha=0.7)
plt.scatter(diabetes_X_test[:, 0], diabetes_y_pred,
            color='blue', marker='^', label='Predicted', alpha=0.7)
plt.xlabel('Feature 0 (Age)')
plt.ylabel('Diabetes Progression')
plt.title('Feature 0 vs Target')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(diabetes_X_test[:, 1], diabetes_y_test,
            color='red', marker='s', label='Actual', alpha=0.7)
plt.scatter(diabetes_X_test[:, 1], diabetes_y_pred,
            color='green', marker='D', label='Predicted', alpha=0.7)
plt.xlabel('Feature 2 (BMI)')
plt.ylabel('Diabetes Progression')
plt.title('Feature 2 vs Target')
plt.legend()

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(diabetes_y_test, diabetes_y_pred,
            color='purple', marker='^',
            label='Predicted vs Actual', alpha=0.7)
plt.plot([diabetes_y_test.min(), diabetes_y_test.max()],
         [diabetes_y_test.min(), diabetes_y_test.max()],
         'r--', label='Ideal Fit')
plt.xlabel("Actual Diabetes Progression")
plt.ylabel("Predicted Diabetes Progression")
plt.title("Actual vs Predicted Diabetes Progression")
plt.legend()
plt.show()
