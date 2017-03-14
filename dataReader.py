import csv


def print_dataset():
    with open('train.txt', 'rb') as csvFile:
        lines = csv.reader(csvFile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
                print dataset[x][y]
