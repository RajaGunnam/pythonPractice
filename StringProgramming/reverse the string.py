
#Reverse of a string
def reverse_string(s):
    print("Reverse of the string -", s[::-1])

    print("Orginal order of the string -", s[0::])

reverse_string("sun rises in the east")

#Reverse the string using loop

def reverse_string_usingLoop(s):
    reversed_str = ""
    for char in s:
        reversed_str=char+reversed_str
    return reversed_str

string = "Raja Gunnam"

reversed_string = reverse_string_usingLoop(string)

print("Reverse order ", reversed_string)
