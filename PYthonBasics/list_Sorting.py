# z = [129, 23, 50, 645, 3, 1.23]
# #Ascnding Order
# z.sort()
# print(z)
# #Decending order
# z.sort(reverse=True)
# print(z)

#Customize sort function

# def myFunction(n):
#     return (n-50)
# z = [129, 23, 50, 645, 3, 1.23]
# z.sort(key = myFunction)
# print(z)

#Case-Insensitive Sort

fruits = ["banana", "Kiwi", "Orange", "cherry"]
fruits.sort(key=str.lower)
print(fruits)

#revese order
fruits.reverse()
print(fruits)