# Step 1: Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Step 2: Generate a sample dataset
# Generating a dataset with 300 samples, 2 features, and 4 centers (clusters)
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Step 3: Perform K-means clustering
# Setting the number of clusters to 4
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# Predict the cluster for each data point
y_kmeans = kmeans.predict(X)

# Step 4: Plot the results
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

# Plotting the cluster centers
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-means Clustering')
plt.show()
