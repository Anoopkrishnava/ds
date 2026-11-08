import json
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# 1. Load JSON dataset
with open("decision_tree_loan_approval.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data["applicants"])

# 2. Separate features and target
X = df[["income", "credit_score", "loan_amount"]]
y = df["decision"]

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 4. Create and train Decision Tree Classifier
model = DecisionTreeClassifier(criterion="entropy", random_state=42)
model.fit(X_train, y_train)

# 5. Predict test data
y_pred = model.predict(X_test)

# 6. Calculate evaluation metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, pos_label="Approved", zero_division=0))
print("Recall:", recall_score(y_test, y_pred, pos_label="Approved", zero_division=0))
print("F1 Score:", f1_score(y_test, y_pred, pos_label="Approved", zero_division=0))

# 7. Confusion Matrix
cm = confusion_matrix(y_test, y_pred, labels=["Rejected", "Approved"])
print("\nConfusion Matrix:\n", cm)

# 8. Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, zero_division=0))

# 9. Plot Decision Tree
plt.figure(figsize=(15, 8))
plot_tree(
    model,
    feature_names=["income", "credit_score", "loan_amount"],
    class_names=["Rejected", "Approved"],
    filled=True
)
plt.title("Decision Tree - Loan Approval")
plt.show()

# 10. Predict loan approval for a new applicant
print("\n--- NEW APPLICANT PREDICTION ---")

income = float(input("Enter income (in thousands): "))
credit_score = float(input("Enter credit score: "))
loan_amount = float(input("Enter existing loan amount (in thousands): "))

new_applicant = pd.DataFrame(
    [[income, credit_score, loan_amount]],
    columns=["income", "credit_score", "loan_amount"]
)

prediction = model.predict(new_applicant)[0]

print("Decision Tree Predicted Decision:", prediction)