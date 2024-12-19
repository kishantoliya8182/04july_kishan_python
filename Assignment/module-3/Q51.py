# Q51. Write a Python function that checks whether a passed string is palindrome or not.

def palindrome_str(str):
    if str == str[::-1]:
        print(f'The String "{str}" is a palindrome.')
    else:
        print(f'The String "{str}" is Not palindrome.')


str=input('Enter A String: ')

palindrome_str(str)

