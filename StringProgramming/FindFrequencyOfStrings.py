
def length_of_words():

    s = "This is a new world for me"
    s1 = s.split()
    print(s1)
    for x in s1:
        print(x,"-",len(x))

length_of_words()
