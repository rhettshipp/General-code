"""
test whether a number is a palindrome
"""
def is_palindrome(num):
    numstring = str(num)
    numlist = list(numstring)
    if numlist == numlist[::-1]:
        return True
    return False


