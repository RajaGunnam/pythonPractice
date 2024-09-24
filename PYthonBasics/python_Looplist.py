
#loop lists
l1=[12, 32, 56, 5, 10]
for i in l1:
    print(i)

#loop through the index numbers
for i in range(len(l1)):
    print(l1[i])

#while loop

i=0
while i<len(l1):
    print("While loop results", l1[i])
    i = i+1

#List Comprehension

#without - List Comprehension
dogs = ["Pomerian", "Great Dane", "husky", "Lab", "German Shephard"]
# newlist=[]
# for x in dogs :
#     if 'h' in x:
#         newlist.append(x)
# print(newlist)

#with-List Comprehension
newlist=[x for x in dogs if "D" in x]
print(newlist)

#Print Caps list
newlist1=[x.upper() for x in dogs]
print(newlist1)

#Condition with expression
newlist2=[x if x!="LAB" else "Pug" for x in newlist1]
print(newlist2)


#Removing Pug from the list
newlist2.remove(newlist2[3])
print(newlist2)






