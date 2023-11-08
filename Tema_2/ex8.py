def filter_strings(x=1, strings=[], flag= True):
    result = []
    for s in strings:
        res_string = []
        for c in s:
            if flag == True:
                if ord(c) % x == 0: # ord transforma caracterul in ascii
                    res_string.append(c)
            else:
                if ord(c) % x != 0:
                    res_string.append(c)
        result.append(res_string)
    return result

print(filter_strings(2,["test", "hello", "lab002"],False))
