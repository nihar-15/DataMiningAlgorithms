import random
import matplotlib.pyplot as plt

# Take parameter 1 values for different items
pointX = []
while True:
    user_input = input("Enter a value for pointX (or type 'stop' to finish): ")
    if user_input.lower() == "stop":
        break
    try:
        value = float(user_input)
        pointX.append(value)
    except ValueError:
        print("Please enter a valid number or 'stop' to finish.")

# Take parameter 2 values for different items
pointY = []
while True:
    user_input = input("Enter a value for pointY (or type 'stop' to finish): ")
    if user_input.lower() == "stop":
        break
    try:
        value = float(user_input)
        pointY.append(value)
    except ValueError:
        print("Please enter a valid number or 'stop' to finish.")

# Ensure pointX and pointY have the same length
if len(pointX) != len(pointY):
    raise ValueError("pointX and pointY must have the same number of elements.")

# Number of clusters
k = int(input("Enter the number of clusters you want to make: "))

# Initialize centroids randomly
positions = set()
listOfCentroid = []
while len(listOfCentroid) < k:
    n = random.randint(0, len(pointX) - 1)
    if n not in positions:
        positions.add(n)
        listC = [pointX[n], pointY[n]]
        listOfCentroid.append(listC)

# Number of iterations
iterations = int(input("Enter the number of iterations: "))

# Function to calculate the Euclidean distance
def euclidean_distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

# Perform K-means clustering
for _ in range(iterations):
    clusters = {i: [] for i in range(k)}

    # Assign points to the nearest centroid
    for i in range(len(pointX)):
        distances = [euclidean_distance([pointX[i], pointY[i]], centroid) for centroid in listOfCentroid]
        min_distance_index = distances.index(min(distances))
        clusters[min_distance_index].append((pointX[i], pointY[i]))

    # Update centroids
    new_centroids = []
    for i in range(k):
        if len(clusters[i]) > 0:
            avg_x = sum([point[0] for point in clusters[i]]) / len(clusters[i])
            avg_y = sum([point[1] for point in clusters[i]]) / len(clusters[i])
            new_centroids.append([avg_x, avg_y])
        else:
            new_centroids.append(listOfCentroid[i])  # No change if cluster is empty
    listOfCentroid = new_centroids

# Plot the final clusters
colors = ['r', 'g', 'b', 'y', 'c', 'm'] 
for i in range(k):
    cluster_points = clusters[i]
    cluster_x = [point[0] for point in cluster_points]
    cluster_y = [point[1] for point in cluster_points]
    plt.scatter(cluster_x, cluster_y, color=colors[i % len(colors)], label=f'Cluster {i+1}')
    plt.scatter(listOfCentroid[i][0], listOfCentroid[i][1], color=colors[i % len(colors)], marker='x')

plt.xlabel('pointX')
plt.ylabel('pointY')
plt.legend()
plt.title('K-means Clustering')
plt.show()
