def power(base,n):
    assert n>=0 and int(n)==n,"positive integers only"
    if n<1:
        return 1
    return base*power(base,n-1)

print(power(4,3))