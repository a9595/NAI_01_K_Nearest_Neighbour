from accuracy import get_accuracy
from dataReader import get_training_set, get_test_set

# data preparation
from neighbors import get_neighbors
from response import get_response

trainingSet = get_training_set()
testSet = get_test_set()

print trainingSet
print testSet

# predictions
predictions = []
k = 3

for x in range(len(testSet)):
    neighbors = get_neighbors(trainingSet, testSet[x], k)
    responses_result = get_response(neighbors)
    predictions.append(responses_result)
    print('> predicted = ' + repr(responses_result) + ', actual = ' + repr(testSet[x][-1]))

# accuracy:
accuracy = get_accuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy) + '%')
