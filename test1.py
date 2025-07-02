nos=[1,2,3,4]
try : 
    total = 900
    nos[100]=99
    result = 10/0
    print(total)

except (Exception) as e:
    print("Error",e)
finally:
    print("closing all connection")
    

'''handling multiple exception if there are more than errors 
we can use exception class'''