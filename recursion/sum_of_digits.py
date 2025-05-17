def sum_of_digits(n):
    assert n>=0 and int(n)==n,"Positive integers only"
    if n==0:
        return 0
    return n%10 + sum_of_digits(n//10)

print(sum_of_digits(1))