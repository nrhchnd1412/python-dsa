def nested_sum(item):
    sum=0
    for k,v in item.items():
        if isinstance(v, dict):
            sum = sum + nested_sum(v)
        elif isinstance(v,int) and v%2==0:
            sum+=v
    return sum

o= {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}
print(nested_sum(o))