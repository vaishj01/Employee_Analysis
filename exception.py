'''
Read a text file and throw a exception if file not found
'''

#Errors are compilation errors and runtime error are handled by compiler#
#eg:syntax error

#Runtime error-errors during runtime are runtime error and they are exceptions
#exception leads to abnormal termination of the program and this leads to loss of data


try:
    with open("data.csv", mode="r") as file:
        print("File opened successfully")
except FileNotFoundError:
    print("File not found")


#BaseException
#      Exception
#          ArithmeticError
#                ZeroDivisionError
#                      OverflowError