'''
is palindrome approach 1
'''
def is_palindrome(original):
    def reverse_string(string):
        if not string:
            return ''
        return string[-1]+reverse_string(string[:-1])
    return original==reverse_string(original)

print(is_palindrome('non'))

'''
is palindrome approach 1
'''

def is_palindrome_2(original):
    if len(original)==0:
        return True
    if original[0]!=original[-1]:
        return False
    return is_palindrome(original[1:-1])

print(is_palindrome_2('non'))
