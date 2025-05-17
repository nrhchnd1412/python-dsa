def strigify_numbers(obj):
    result = {}
    for k,v in obj.items():
        if isinstance(v,int) and not isinstance(v, bool):
            result[k]=str(v)
        elif isinstance(v,dict):
            result[k]=strigify_numbers(v)
        else:
            result[k]=v
    return result

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

print(strigify_numbers(obj))