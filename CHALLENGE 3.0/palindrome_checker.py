def is_palindrome(string):
    # Converting the string to lowercase and remove whitespace
    string = string.lower().replace(" ", "")

    # Reversing the string using slicing
    reversed_string = string[::-1]

    # Comparing the original and reversed strings
    if string == reversed_string:
        return True
    else:
        return False


print(is_palindrome('dominion'))
