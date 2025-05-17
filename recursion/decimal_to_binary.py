def decimal_to_binary(n):
    if n<2:
        return str(n)
    return decimal_to_binary(n//2)+str(n%2)

print(decimal_to_binary(11))