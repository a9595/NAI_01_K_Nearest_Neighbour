import math


def euclidean_distance(testSet, trainingSet, length):
    distance = 0
    for x in range(length):
        distance += pow((testSet[x] - trainingSet[x]), 2)
    return math.sqrt(distance)