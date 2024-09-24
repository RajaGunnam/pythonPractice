l1=[12, "ahex", 23, "a"]
print("Length of the list is", len(l1))
print(l1[1])
#add value to the list
l1.append(19)
print(l1)
#remove value from the list
l1.remove(l1[3])
l1.remove(19)
print(l1)
print("Length of the list is", len(l1))

#negative indexing
l2 = ["Raja", "Boss", "help", "help"]
print(l2)
print(l2[-1])
#Range of indexes
print(l2[1:3])#Range of negative indexes
print(l2[-4:-1])

#Change list
l3=["RE","Honda", "yamaha", "Hero", "Ola", "trumph"]
print("The list before chnaging", l3)
l3[1] = "kawasaki"
print("The list after changing", l3)
# #change a range of item values
# l3[2:4] = ["harly D", "BMW"]
# l4 = print(l3)

#insert - add an items at a specified index

l3.insert(2, "Tata Safari")
print(l3)

#Append - Insert item at the last loc
l3.append("Range Rover")
print(l3)

l4 = [12, 32, 54, "Range Rover"]
l3.extend(l4)
print(l3)
# l3.remove(l3[10])
# print(l3)

#Pop - Pop menthod used to remove item a specified index
l3.pop(11)
print("Printing for pop method", l3)

#Remove items from list usinf del keyword
del l3[0]
print(l3)

#Delete complete list
# del l3;
# print(l3)

#Clear() - This mentod is used to clear the list

l3.clear()





