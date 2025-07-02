
#class MyClass:
    #constructors
    #data members(variables/fields)
    #member functions(getters,setters)

class MyClass:
    def __init__(self,data):
        self.data=data
        print("initialize the object...")
    def show(self):
        print("heyy,SCOE!!!!",self.data)


ob1=MyClass(900)
ob2=MyClass(100)
 
ob1.show()  #ob1 is invoking -self
ob2.show()  #ob2 is invoking -self

    

'''Python OOP:

1.Constructors are used to initialize the objects
2.They are automatically invoked 
3.In python we have to used self pointer

more than one constructor is called constructor overloading'''
