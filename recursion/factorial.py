def factorial(n):
    assert n>=0 and int(n)==n ,"Number should be a positive integer only"
    if n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(10))