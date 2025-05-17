def sum_diagonal_primary_diagonal(lst):
    sum =0
    n = len(lst)
    for i in range(n):
        sum+=lst[i][i]
    return sum

def sum_diagonal_secondary_diagonal(lst):
    sum =0
    n = len(lst)
    for i in range(n):
        sum+=lst[i][n-i-1]
    return sum