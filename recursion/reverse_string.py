'''
reverse a string
'''

def reverse_string(string):
    if not string:
        return ''
    return string[-1]+reverse_string(string[:-1])

print(reverse_string('neeraj chand'))