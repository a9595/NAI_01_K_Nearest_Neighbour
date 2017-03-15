from dataReader import get_training_set, get_test_set

# data preparation
from neighbors import get_neighbors

trainingSet = get_training_set()
testSet = get_test_set()

print trainingSet
print testSet

# predictions
predictions = []
k = 3

for x in range(len(testSet)):
    neighbors = get_neighbors(trainingSet, testSet[x], k)

