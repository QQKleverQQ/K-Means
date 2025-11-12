import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


def plot_clusters(data, clusters, means, iteration):
    colors = ['red', 'green', 'blue', 'purple', 'orange'] # Цвета точек.
    plt.figure(figsize=(6, 5))
    for idx, points in clusters.items():
        points = np.array(points)
        if len(points) > 0:
            plt.scatter(points[:, 0], points[:, 1], color=colors[idx % len(colors)], label=f"Cluster {idx}")
    plt.scatter(means[:, 0], means[:, 1], color='black', marker='x', s=100, label='Means')
    plt.title(f"Iteration {iteration}")
    plt.legend()
    plt.show()
