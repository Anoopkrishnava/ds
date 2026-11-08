# Write a Python program to predict house prices using Multiple Linear Regression
# based on area and number of bedrooms. Display coefficients, intercept, 
# MSE, R² score, actual vs predicted graph, and predict price for a new house.

import json
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load JSON dataset
with open("multiple_regression_house_price.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data["houses"])

# 2. Separate features and target
X = df[["area", "bedrooms"]]
y = df["price"]

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 4. Create and train Multiple Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predict test data
y_pred = model.predict(X_test)

# 6. Display coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# 7. Evaluate model
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# 8. Compare actual and predicted prices
print("\nActual vs Predicted Prices:")
print(pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": y_pred
}))

# 9. Plot actual vs predicted prices
plt.scatter(y_test, y_pred, color="blue")

plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("Actual vs Predicted House Prices")
plt.show()

# 10. Predict price for a new house
area = float(input("Enter house area: "))
bedrooms = int(input("Enter number of bedrooms: "))

new_house = pd.DataFrame(
    [[area, bedrooms]],
    columns=["area", "bedrooms"]
)

prediction = model.predict(new_house)

print("Predicted House Price:", prediction[0])
