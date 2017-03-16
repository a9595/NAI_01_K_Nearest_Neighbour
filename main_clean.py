from calulateWithK import calculateWithK, receiveTestDataInputByUser
from graph import createGraph

def main():
    # user input
    print('1 - Input K and calculate')
    print('2 - Input your own test data raw')
    # print('3 - Draw graph")
    user_input = raw_input("Please enter k for calulation: ")
    if user_input == '1':
        calculateWithK(-1)
    if user_input == '2':
        receiveTestDataInputByUser()
    if user_input == '3':
        createGraph()


main()