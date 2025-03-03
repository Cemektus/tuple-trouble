points = [(1, 2), (3, 4), (5, 6), (7, 8)]

import math

def euclideanDistance(a, b):
    x1, y1 = a   # Extract x1, y1 from the first tuple
    x2, y2 = b    # Extract x2, y2 from the second tuple

    dx = x2 - x1  # Compute the difference in x-coordinates
    dy = y2 - y1  # Compute the difference in y-coordinates

    d = math.sqrt(dx**2 + dy**2)  # Apply the Euclidean formula
    return d  # Return the computed distance

distances = []

n = len(points)

for i in range(n):
    for j in range(i + 1, n):
        d = euclideanDistance(points[i], points[j])
        distances.append(d)

min_distance = min(distances)
print("The minimum Euclidean distance is:", min_distance)