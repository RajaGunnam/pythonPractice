t1 = ("Honda", "Kia", "BMW", "Audi")
#convert tuple to a list and again tuple
l1 = list(t1)
l1[2] = "Volkswagon"
x=tuple(l1)
print(x)

#add tuple to a tuple
t2 = ("Java", "Python", ".Net", "React")
t3 = ("Go",)
t2 +=t3
print(t2)


