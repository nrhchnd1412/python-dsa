def element_wise_sum(t1,t2):
    if len(t1)!=len(t2):
        return "length is not equal"
    return tuple(x+y for x,y in zip(t1,t2))