
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# 4. Create and train Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# 5. Predict test data
y_pred = model.predict(X_test)

# 6. Calculate evaluation metrics
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

# 7. Confusion Matrix
cm = confusion_matrix(y_test, y_pred,
                     labels=["Rejected", "Approved"])
print("\nConfusion Matrix:\n", cm)

# 8. Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred,
                            zero_division=0))

# 9. Plot Confusion Matrix
plt.figure(figsize=(5, 4))

sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Rejected", "Approved"],
            yticklabels=["Rejected", "Approved"])

plt.xlabel("Predicted Decision")
plt.ylabel("Actual Decision")
plt.title("Confusion Matrix")

plt.show()

# 10. Predict loan approval for new applicant
print("\n--- NEW APPLICANT PREDICTION ---")

income = float(input("Enter income: "))
credit_score = float(input("Enter credit score: "))
existing_loan = float(input("Enter existing loan: "))

new_applicant = pd.DataFrame(
    [[income, credit_score, existing_loan]],
    columns=["income", "credit_score", "existing_loan"]
)

prediction = model.predict(new_applicant)

print("Naive Bayes Loan Decision:", prediction[0])
