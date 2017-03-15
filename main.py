from accuracy import get_accuracy
from neighbors import get_neighbors

# trainingSet = get_training_set()
# testSet = get_test_set()

# neighbors:
from response import get_response

trainingSetDemo = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
testSetDemo = [5, 5, 5]
k = 1
neighbors = get_neighbors(trainingSetDemo, testSetDemo, k)
print neighbors

# response:
neighborsDemo = [[1, 1, 1, 'a'], [2, 2, 2, 'a'], [3, 3, 3, 'b']]
response = get_response(neighbors)
print(response)

# accuracy:
testSetAccuracy = [[1, 1, 1, 'a'], [2, 2, 2, 'a'], [3, 3, 3, 'b']]
predictions = ['a', 'a,', 'a']

accuracy = get_accuracy(testSetAccuracy, predictions)
print(accuracy)
