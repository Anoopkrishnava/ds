# Write a Python program to predict sales based on advertising expenditure 
# using Linear Regression. Display coefficient, intercept,
# MSE, R² score, regression graph, and predict sales for new advertising expenditure.

import json
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load JSON dataset
with open("linear_regression_sales.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data["sales_data"])

# 2. Separate features and target
X = df[["advertising"]]
y = df["sales"]

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 4. Create and train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predict test data
y_pred = model.predict(X_test)

# 6. Display coefficient and intercept
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

# 7. Evaluate model
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# 8. Plot regression graph
plt.scatter(X, y, color="blue", label="Actual Sales")

plt.plot(
    X,
    model.predict(X),
    color="red",
    label="Regression Line"
)

plt.xlabel("Advertising Expense")
plt.ylabel("Sales")
plt.title("Sales Prediction using Linear Regression")
plt.legend()
plt.show()

# 9. Predict sales for new advertising expense
expense = float(input("Enter advertising expense: "))

new_data = pd.DataFrame(
    [[expense]],
    columns=["advertising"]
)

prediction = model.predict(new_data)

print("Predicted Sales:", prediction[0])
