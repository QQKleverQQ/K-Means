import numpy as np

def assign_clusters(data_points, means): # принимает точки
    clusters = {i: [] for i in range(len(means))}
    for point in data_points:
        distances = np.linalg.norm(point - means, axis=1)
        closest_cluster = np.argmin(distances) # находит ближайшее центр
        clusters[closest_cluster].append(point) # добавляет  его в кластеры
    return clusters
