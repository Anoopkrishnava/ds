# Write a Python program to group students
# into three clusters based on study hours and 
# attendance using K-Means clustering.

import json
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

# 1. Load JSON dataset
with open("kmeans_student_groups.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data["students"])

# 2. Select features
X = df[["study_hours", "attendance"]]

# 3. Create and train K-Means model
model = KMeans(n_clusters=3, random_state=42)
model.fit(X)

# 4. Assign cluster labels
df["Cluster"] = model.labels_

# 5. Display cluster labels
print("Student Cluster Assignments:")
print(df)

# 6. Display cluster centers
print("\nCluster Centers:")
print(model.cluster_centers_)

# 7. Plot clusters
plt.scatter(
    X["study_hours"],
    X["attendance"],
    c=df["Cluster"],
    cmap="viridis",
    marker="o"
)

plt.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    color="red",
    marker="X",
    s=200,
    label="Cluster Centers"
)

plt.xlabel("Study Hours")
plt.ylabel("Attendance")
plt.title("K-Means Student Clustering")
plt.legend()
plt.show()