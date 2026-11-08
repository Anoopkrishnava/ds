
# Write a Python program to perform customer segmentation using K-Means clustering
#  based on annual income and spending score. 
#  Display cluster assignments, cluster centers, and visualize the clusters 
#  using a scatter plot.

import json
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

# 1. Load JSON dataset
with open("kmeans_shopping_customers.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data["customers"])

# 2. Select features
X = df[["annual_income", "spending_score"]]

# 3. Create and train K-Means model
model = KMeans(n_clusters=3, random_state=42)
model.fit(X)

# 4. Assign cluster labels
df["Cluster"] = model.labels_

# 5. Display customer cluster assignments
print("Customer Cluster Assignments:")
print(df)

# 6. Display cluster centers
print("\nCluster Centers:")
print(model.cluster_centers_)

# 7. Visualize clusters
plt.scatter(
    X["annual_income"],
    X["spending_score"],
    c=df["Cluster"],
    cmap="viridis",
    marker="o"
)

# Plot cluster centers
plt.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    color="red",
    marker="X",
    s=200,
    label="Cluster Centers"
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("K-Means Customer Segmentation")
plt.legend()
plt.show()
