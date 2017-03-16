from calulateWithK import calculateWithK, recieveTestDataInputByUser
from graph import createGraph

def main():
    # user input
    print('1 - Input K and calculate')
    print('2 - Input your own test data raw')
    user_input = raw_input("Please enter something: ")
    if user_input == '1':
        calculateWithK(-1)
    if user_input == '2':
        recieveTestDataInputByUser()
    if user_input == '3':
        createGraph()


main()
