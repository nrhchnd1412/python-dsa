def first_second_max(lst):
    first = second =0
    for i,num in enumerate(lst):
        if num>first:
            second = first
            first= num
        elif num>second:
            second =num
    return first,second