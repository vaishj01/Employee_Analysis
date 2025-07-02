'''To create a custom exception we will inherit from exception class
then we write custom exception handling function


To invoke custom exception we have to raise invoke keyword

IF no constructor is define a default constructor will be called'''


'''class MyCustomError(Exception):
    pass  # You can customize this further if needed

def check_age(age):
    if age < 18:
        raise MyCustomError("Age must be 18 or older")
    else:
        print("Age is valid.")

try:
    check_age(21)
except MyCustomError as e:
    print(f"Custom Exception Caught: {e}")'''


class InvalidAgeError(Exception):
    def __init__(self, age, message="Invalid age provided"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.age}"
    
def register_user(age):
    if age < 18:
        raise InvalidAgeError(age, "User is underage")

try:
    register_user(15)
except InvalidAgeError as e:
    print(e)
