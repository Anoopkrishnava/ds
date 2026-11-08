# Python program to predict student marks based on study hours using Linear Regression.
# Display the coefficient, intercept, Mean Squared Error (MSE),
# R² score, regression graph, and predict marks for a new student

import json
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load JSON dataset
with open("linear_regression_student_marks.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data["students"])

# 2. Separate features and target
X = df[["study_hours"]]
y = df["mark"]

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
plt.scatter(X, y, color="blue", label="Actual Marks")

plt.plot(
    X,
    model.predict(X),
    color="red",
    label="Regression Line"
)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Student Marks Prediction using Linear Regression")
plt.legend()
plt.show()

# 9. Predict marks for a new student
hours = float(input("Enter study hours: "))

new_student = pd.DataFrame(
    [[hours]],
    columns=["study_hours"]
)

prediction = model.predict(new_student)

print("Predicted Marks:", prediction[0])
