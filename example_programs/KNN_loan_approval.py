# To implement K-Nearest Neighbors (KNN) classification to predict whether a loan applicant 
# will be Approved or Rejected based on income, credit score, and existing loan.

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
with open("knn_loan_approval.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data["applicants"])

# 2. Separate features and target
X = df[["income", "credit_score", "existing_loan"]]
y = df["decision"]

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
print("Precision:", precision_score(y_test, y_pred,
                                   pos_label="Approved",
                                   zero_division=0))
print("Recall:", recall_score(y_test, y_pred,
                              pos_label="Approved",
                              zero_division=0))
print("F1 Score:", f1_score(y_test, y_pred,
                             pos_label="Approved",
                             zero_division=0))

# 8. Confusion Matrix
cm = confusion_matrix(y_test, y_pred,
                     labels=["Rejected", "Approved"])
print("\nConfusion Matrix:\n", cm)

# 9. Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred,
                            zero_division=0))

# 10. Predict loan approval for new applicant
print("\n--- NEW APPLICANT PREDICTION ---")

income = float(input("Enter income: "))
credit_score = float(input("Enter credit score: "))
existing_loan = float(input("Enter existing loan: "))

new_applicant = pd.DataFrame(
    [[income, credit_score, existing_loan]],
    columns=["income", "credit_score", "existing_loan"]
)

new_applicant = scaler.transform(new_applicant)

prediction = model.predict(new_applicant)

print("KNN Loan Decision:", prediction[0])
