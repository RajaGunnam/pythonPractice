
s1 = "Strings are immutable"

#length of the string
print(len(s1))


#User can access the characters in string using index
print("Each character in string has an index - ",s1[3])

#Slicing
print("You can slice a strings to get a substring - ",s1[:12])

#looping a string

for i in s1:

    print(i)

#uppercase method

s2= s1.upper()
print(s2)

#lowercase method
s3= s1.lower()
print(s3)

if(s2.islower()):
    print("the string is in lower case")
else:
    print("The string is in Upper case")

def stringConcatination():

   global first_name

   first_name= "Raja"
   global last_name
   last_name= "Gunnam"

   global full_name
   full_name = first_name + " " + last_name
   print(full_name)

stringConcatination()

def string_repeat():
    print(full_name * 3)

string_repeat()


#String formattings

def string_formats():
    name = "Raja"
    age=26
    print("my mame is {} and I am {} years old.".format(name,age))

    #another way
    print(f"my name is {name} and I am {age} years old")

string_formats()

#write a program to remove the spaces from leading and trailing

name1 = "Raja"

print("Before removing the spaces -", name1)

print("After removing the spaces -", name1.strip())

print(name1[0:len(name1)-1]+name1[-1].upper())