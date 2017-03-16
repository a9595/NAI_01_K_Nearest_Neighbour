from accuracy import get_accuracy
from dataReader import get_training_set, get_test_set
from neighbors import get_neighbors
from response import get_response


def calculateWithK():
    k = raw_input("Please input K: ")
    k = int(k)
    global neighbors, accuracy
    # data preparation
    trainingSet = get_training_set()
    testSet = get_test_set()
    print trainingSet
    print testSet
    # predictions
    predictions = []
    for x in range(len(testSet)):
        neighbors = get_neighbors(trainingSet, testSet[x], k)
        responses_result = get_response(neighbors)
        predictions.append(responses_result)
        print('> predicted = ' + repr(responses_result) + ', actual = ' + repr(testSet[x][-1]))

    # accuracy:
    accuracy = get_accuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')



# user input
print('1 - Input K and calculate')
print('2 - Input your own test data raw')
print('3 - Draw a graph')
user_input = raw_input("Please enter something: ")

if user_input == '1':
    calculateWithK()