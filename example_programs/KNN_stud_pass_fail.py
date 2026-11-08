# Write a Python program to predict whether a student passes or fails 
# using the K-Nearest Neighbors (KNN) classifier based on exam marks, 
# attendance, and internal marks. Calculate accuracy, precision, recall, 
# F1 score, confusion matrix, classification report, and predict the result for a new student.


import json
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# 1. Load JSON dataset
with open("knn_student_pass_fail.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data["students"])

# 2. Separate features and target
X = df[["attendance", "internal", "exam"]]
y = df["result"]

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 4. Standardize features
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. Create and train KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# 6. Predict test data
y_pred = model.predict(X_test)

# 7. Calculate evaluation metrics
print("Accuracy:", accuracy_score(y_test, y_pred))

print("Precision:", precision_score(
    y_test, y_pred, pos_label="Pass", zero_division=0
))

print("Recall:", recall_score(
    y_test, y_pred, pos_label="Pass", zero_division=0
))

print("F1 Score:", f1_score(
    y_test, y_pred, pos_label="Pass", zero_division=0
))

# 8. Confusion Matrix
cm = confusion_matrix(y_test, y_pred, labels=["Fail", "Pass"])
print("\nConfusion Matrix:\n", cm)

# 9. Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, zero_division=0))

# 10. Predict result for a new student
print("\n--- NEW STUDENT PREDICTION ---")

attendance = float(input("Enter attendance percentage: "))
internal = float(input("Enter internal marks: "))
exam = float(input("Enter exam marks: "))

new_student = pd.DataFrame(
    [[attendance, internal, exam]],
    columns=["attendance", "internal", "exam"]
)

new_student = scaler.transform(new_student)

prediction = model.predict(new_student)

print("KNN Predicted Result:", prediction[0])

