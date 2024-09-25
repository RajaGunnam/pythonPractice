class First_Class:

#inti method
    def __init__(self, name, age):

        self.name=name
        self.age=age

obj1 = First_Class("Raja Gunnam", "26")

print(f'My name is {obj1.name} and I am {obj1.age} years old')

print("Name of the candidate -",obj1.name)
print("Name of the candidate -",obj1.age)




#str function - is a way to control what gets printed when you display an object.

#without str function:

print(obj1)

#with str function

class Employee_Data:

    def __init__(self, eName, eId):
        self.eName = eName
        self.eId = eId

    def __str__(self):
        return f"Employee Name -{self.eName}\nEmployee ID{self.eId}"
emp = Employee_Data("Raja Gunnam", "AHX1235")
print(emp)

