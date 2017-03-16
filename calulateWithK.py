from accuracy import get_accuracy
from dataReader import get_test_set, get_training_set
from neighbors import get_neighbors
from response import get_response

def calculateWithKFofGraph(test_set_by_user=[], trainingSet=[], k = 1):
    global neighbors, accuracy

    testSet = test_set_by_user
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
    return accuracy


def calculateWithK(test_set_by_user=[], k=-1, trainingSet=[]):
    if (k == -1):
        k = raw_input("Please input K: ")
        k = int(k)

    global neighbors, accuracy

    # data preparation
    if (test_set_by_user == -1):
        testSet = get_test_set()
    else:
        testSet = test_set_by_user

    trainingSet = get_training_set()
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


def receiveTestDataInputByUser():
    testSet = []
    var1, var2, var3, var4, varClass = raw_input('Type in data (for ex. "4 3 1 0 Iris-setosa"):  ').split(' ')
    testSet.append([float(var1), float(var2), float(var3), float(var4), varClass])
    calculateWithK(testSet)