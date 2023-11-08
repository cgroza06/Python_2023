def op_on_sets(*sets):
    dictionary = {}
    for i in range(len(sets)):
        for j in range(len(sets)):
            if i == j:
                continue
            a, b = sets[i], sets[j]
            dictionary[f"{a} | {b}"] = a | b
            dictionary[f"{a} & {b}"] = a & b
            dictionary[f"{a} - {b}"] = a - b
            dictionary[f"{b} - {a}"] = b - a
            dictionary[f"{a} ^ {b}"] = a ^ b
    return dictionary

print(op_on_sets({1,2},{2,3}))
print(op_on_sets({1,2},{2,3},{4,5}))