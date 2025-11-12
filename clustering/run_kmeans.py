import numpy as np
from sklearn.datasets import load_iris
from .assign_clusters import assign_clusters
from .update_means import update_means
from .check_convergence import check_convergence
from visualization.plot_clusters import plot_clusters

def run_kmeans(k=3, max_iters=100):
    iris = load_iris()
    data = iris.data

    means = data[np.random.choice(data.shape[0], k, replace=False)] # Random

    for i in range(max_iters): # проверяет сходимость
        clusters = assign_clusters(data, means)
        new_means = update_means(clusters)

        plot_clusters(data, clusters, means, i)  # рисуем каждый шаг

        if check_convergence(means, new_means):
            print(f"Algorithm converged after {i+1} iterations.")
            break
        means = new_means

    return clusters, means
