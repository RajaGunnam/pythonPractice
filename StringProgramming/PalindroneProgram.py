palindrome_string = "Madam"

def check_palindrome():
    rev = palindrome_string.lower()[::-1]

    if(rev==palindrome_string.lower()):
        print("Given string is a palindrome")
    else:
        print("Given string is not a palindrome string")
check_palindrome()