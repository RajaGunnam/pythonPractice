
class Calculator:

    def __init__(myObj):
        myObj.a=int(input("Enter the Value of A - "))
        myObj.b=int(input("Enter the value of B - "))
    def add_two_numbers(myObj):
        result = myObj.a + myObj.b
        return result

    def substraction_of_two_numbers(myObj):
        result = myObj.a -myObj.b
        return result

    def __str__(myObj):
        return f"The sum of {myObj.a} and {myObj.b} is {myObj.add_two_numbers()}"


obj1= Calculator()

print(obj1)
print(f"The difference of {obj1.a} and {obj1.b} is {obj1.substraction_of_two_numbers()}")

