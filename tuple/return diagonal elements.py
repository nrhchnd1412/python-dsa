''''
Time complexity: O(n)
'''

def return_diagonal_elements(tup):
    return tuple((tup[i][i]) for i in range(len(tup)))

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = return_diagonal_elements(input_tuple)
print(output_tuple) 