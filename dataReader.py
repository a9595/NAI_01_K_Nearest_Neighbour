import csv

COLUMNS_COUNT = 4


def get_training_set():
    return get_set("train.txt")


def get_test_set():
    return get_set("test.txt")


def get_set(filename):
    result = []
    with open(filename, 'r') as csvFile:
        lines = csv.reader(csvFile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            result.append(dataset[x])
        return result
