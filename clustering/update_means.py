import numpy as np

# Делает средние значение по каждому кластеру
def update_means(clusters):
    new_means = []
    for points in clusters.values():
        if len(points) > 0:
            new_means.append(np.mean(points, axis=0))
    return np.array(new_means)
