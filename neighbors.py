import operator

from eucledeanDistance import euclidean_distance


def get_neighbors(trainingSet, testSet, k):
    distances = []
    length = len(testSet) - 1
    for x in range(len(trainingSet)):
        distance = euclidean_distance(testSet, trainingSet[x], length)
        distances.append((trainingSet[x], distance))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

#
# def getNeighbors(trainingSet, testInstance, k):
#     distances = []
#     length = len(testInstance) - 1
#     for x in range(len(trainingSet)):
#         dist = euclidean_distance(testInstance, trainingSet[x], length)
#         distances.append((trainingSet[x], dist))
#     distances.sort(key=operator.itemgetter(1))
#     neighbors = []
#     for x in range(k):
#         neighbors.append(distances[x][0])
#     return neighbors
