import numpy as np

# Делает проверку старых и новых точек
def check_convergence(old_means, new_means, threshold=0.001):
    differences = np.linalg.norm(old_means - new_means, axis=1)
    return np.all(differences < threshold)
