# Write a Python program to predict exam marks using Multiple Linear Regression
# based on study hours, attendance, and internal marks. Display coefficients, intercept, 
# MSE, R² score, actual vs predicted graph, and predict marks for a new student.


import json
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load JSON dataset
with open("multiple_regression_exam_score.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data["students"])

# 2. Separate features and target
X = df[["study_hours", "attendance", "internal"]]
y = df["exam_mark"]

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

# 8. Compare actual and predicted marks
print("\nActual vs Predicted Marks:")
print(pd.DataFrame({
    "Actual Marks": y_test.values,
    "Predicted Marks": y_pred
}))

# 9. Plot actual vs predicted marks
plt.scatter(y_test, y_pred, color="blue")

plt.xlabel("Actual Exam Marks")
plt.ylabel("Predicted Exam Marks")
plt.title("Actual vs Predicted Exam Marks")
plt.show()

# 10. Predict marks for a new student
hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance percentage: "))
internal = float(input("Enter internal marks: "))

new_student = pd.DataFrame(
    [[hours, attendance, internal]],
    columns=["study_hours", "attendance", "internal"]
)

prediction = model.predict(new_student)

print("Predicted Exam Marks:", prediction[0])
