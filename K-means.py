import numpy as np

class KMeans:
    def __init__(self, n_clusters=3, max_iter=300):
        self.n_clusters = n_clusters
        self.max_iter = max_iter

    def initialiser_centroides(self, X):
        indices = np.random.choice(X.shape[0], self.n_clusters, replace=False)
        return X[indices]

    def affecter_clusters(self, X, centroides):
        distances = np.sqrt(((X - centroides[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)

    def mettre_a_jour_centroides(self, X, clusters):
        centroides = np.zeros((self.n_clusters, X.shape[1]))
        for i in range(self.n_clusters):
            centroides[i] = np.mean(X[clusters == i], axis=0)
        return centroides

    def ajuster(self, X):
        centroides = self.initialiser_centroides(X)
        for _ in range(self.max_iter):
            clusters = self.affecter_clusters(X, centroides)
            nouveaux_centroides = self.mettre_a_jour_centroides(X, clusters)
            if np.allclose(centroides, nouveaux_centroides):
                break
            centroides = nouveaux_centroides
        return clusters, centroides

magasins = np.array([
    [33.5731, -7.5898],  
    [33.5734, -7.6035],  
    [33.5658, -7.6113], 
    [33.5756, -7.6171],  
    [33.5722, -7.5937],  
    [33.5699, -7.6045],  
    [33.5761, -7.6098],  
    [33.5705, -7.6201],  
    [33.5743, -7.5999], 
    [33.5676, -7.6076]   
])


kmeans = KMeans(n_clusters=3)
clusters, centroides = kmeans.ajuster(magasins)

print("Centroides finaux :\n", centroides)
print("Clusters finaux :\n", clusters)
