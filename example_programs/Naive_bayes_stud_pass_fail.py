
import json
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
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

# 4. Create and train Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# 5. Predict test data
y_pred = model.predict(X_test)

# 6. Calculate evaluation metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred,
                                   pos_label="Pass",
                                   zero_division=0))
print("Recall:", recall_score(y_test, y_pred,
                              pos_label="Pass",
                              zero_division=0))
print("F1 Score:", f1_score(y_test, y_pred,
                             pos_label="Pass",
                             zero_division=0))

# 7. Confusion Matrix
cm = confusion_matrix(y_test, y_pred,
                     labels=["Fail", "Pass"])
print("\nConfusion Matrix:\n", cm)

# 8. Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred,
                            zero_division=0))

import matplotlib.pyplot as plt
import seaborn as sns

# Plot Confusion Matrix
plt.figure(figsize=(5, 4))

sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Fail", "Pass"],
            yticklabels=["Fail", "Pass"])

plt.xlabel("Predicted Result")
plt.ylabel("Actual Result")
plt.title("Confusion Matrix")

plt.show()



# 9. Predict result for a new student
print("\n--- NEW STUDENT PREDICTION ---")

attendance = float(input("Enter attendance percentage: "))
internal = float(input("Enter internal marks: "))
exam = float(input("Enter exam marks: "))

new_student = pd.DataFrame(
    [[attendance, internal, exam]],
    columns=["attendance", "internal", "exam"]
)

prediction = model.predict(new_student)

print("Naive Bayes Predicted Result:", prediction[0])
