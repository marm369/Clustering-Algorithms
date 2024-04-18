import numpy as np


# Fonction pour calculer la distance minimale entre les clusters
def min_distance(distances, cluster1, cluster2):
    min_distance = float('inf')
    for node1 in cluster1:
        for node2 in cluster2:
            if distances[node1][node2] < min_distance:
                min_distance = distances[node1][node2]
    return min_distance


# Fonction pour calculer la distance maximale entre les clusters
def max_distance(distances, cluster1, cluster2):
    max_distance = float('-inf')
    for node1 in cluster1:
        for node2 in cluster2:
            if distances[node1][node2] > max_distance:
                max_distance = distances[node1][node2]
    return max_distance


# Fonction pour calculer la distance moyenne entre les clusters
def moyenne_distance(distances, cluster1, cluster2):
    total = 0
    count = 0
    for node1 in cluster1:
        for node2 in cluster2:
            total += distances[node1][node2]
            count += 1
    return total / count if count != 0 else 0


# Fonction pour calculer la distance en spécifiant la distance intergroupe
def calculer_distance(distances, cluster1, cluster2, intergroupe):
    if intergroupe == 'min':
        return min_distance(distances, cluster1, cluster2)
    elif intergroupe == 'max':
        return max_distance(distances, cluster1, cluster2)
    elif intergroupe == 'moy':
        return moyenne_distance(distances, cluster1, cluster2)


# Fonction pour afficher la matrice des distances
def afficher_matrice(clusters, distances, intergroupe):
    print("\t", end="")
    for i in range(len(clusters)):
        print("Cluster{}".format(i + 1), end="  ")
    print()
    for i, cluster1 in enumerate(clusters):
        print("Cluster{}".format(i + 1), end="  ")
        for j, cluster2 in enumerate(clusters):
            if j >= i:
                print("{:.2f}".format(calculer_distance(distances, cluster1, cluster2, intergroupe)), end="\t")
            else:
                print("\t", end="\t")
        print()


# Fonction de l'algorithme AGNES
def AGNES(distances, n_clusters=2, intergroupe='min'):

    n_nodes = len(distances)
    labels = np.arange(n_nodes)

    # En initialisant chaque nœud comme un cluster
    clusters = [[i] for i in range(n_nodes)]

    iteration = 1
    # Une boucle while pour s'arrêter lorsque on atteint le nombre de clusters souhaité
    while len(clusters) > n_clusters:
        print("Iteration", iteration)
        # Afficher la matrice des distances
        afficher_matrice(clusters, distances, intergroupe)

        min_distance = float('inf')
        min_i = min_j = 0
        # Parcours de toutes les paires de clusters pour trouver la paire avec la distance minimale
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                distance = calculer_distance(distances, clusters[i], clusters[j], intergroupe)
                if distance < min_distance:
                    min_distance = distance
                    min_i = i
                    min_j = j

        # un tuple d'inforamtion contient la distance min et les deux clusters qui ont cette distance
        min_distance_info = (min_distance, min_i, min_j)

        min_dist, merge_indices = min_distance_info[0], (min_distance_info[1], min_distance_info[2])

        # Rassembler les clusters les plus proches
        clusters[merge_indices[0]].extend(clusters[merge_indices[1]])
        del clusters[merge_indices[1]]

        iteration += 1

    print("Résultat final :")
    afficher_matrice(clusters, distances, intergroupe)
    return labels


if __name__ == "__main__":
    # Entrer la matrice de distance entre chaque nœud
    distances = [
        [0.00, 6.00, 5.00, 10.00, 7.50],
        [6.00, 0.00, 11.00, 4.00, 1.50],
        [5.00, 11.00, 0.00, 15.00, 12.50],
        [10.00, 4.00, 15.00, 0.00, 2.50],
        [7.50, 1.50, 12.50, 2.50, 0.00]
    ]

    # Demander à l'utilisateur le nombre de clusters et le type de distance intergroupe
    n_clusters = int(input("Entrez le nombre de clusters souhaités : "))
    intergroupe = input("Entrez le type de distance intergroupe (min, max, moy) : ")

    # Utiliser l'algorithme AGNES
    labels = AGNES(distances, n_clusters, intergroupe)
