from clustering.run_kmeans import run_kmeans

if __name__ == "__main__":
    clusters, means = run_kmeans(k=3)


#The following websites were used to create the code:
# 1) https://www.w3schools.com/python/python_ml_k-means.asp
# 2) https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris
# 3) https://datasciencelab.wordpress.com/2013/12/12/clustering-with-k-means-in-python/
# 4) https://www.geeksforgeeks.org/machine-learning/k-means-clustering-introduction/
# 5) https://pypi.org/project/scikit-learn/