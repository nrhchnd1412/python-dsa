def capitalize_first(array_string):
    if len(array_string)==0:
        return []
    capitalized = array_string[0].capitalize()
    return [capitalized]+ capitalize_first(array_string[1:])

print(capitalize_first(['tom','god']))