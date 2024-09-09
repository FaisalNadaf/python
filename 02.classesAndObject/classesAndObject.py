# Define a class named MyClass
class MyClass:
    # Constructor method to initialize the object
    def __init__(self, name, age):
        # Set the name attribute
        self.name = name
        # Set the age attribute
        self.age = age

    # Method to display the name and age of the object
    def myMethod(self):
        # Print the name attribute
        print(f"Name: {self.name}")
        # Print the age attribute
        print(f"Age: {self.age}")

# Create an instance of MyClass with name "faisal" and age 20
callingClass = MyClass("faisal", 20)

# Call the myMethod() on the created instance to print name and age
callingClass.myMethod()
