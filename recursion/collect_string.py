def collectStrings(obj):
    result = []
    for k,v in obj.items():
        if isinstance(v,str):
            result.append(v)
        elif isinstance(v,dict):
            result = result + collectStrings(v)
    return result

obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}
 
print(collectStrings(obj))