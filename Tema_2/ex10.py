def apparition_tuples(lists):
    max_length = max(len(l) for l in lists)
    tuple_list = []
    for i in range(max_length):
        build_tuple =[]
        for l in lists:
            if i < len(l):
                build_tuple.append(l[i])
            else:
                build_tuple.append(None)
        tuple_list.append(tuple(build_tuple))
    return tuple_list

n = int(input("Introduceti numarul de liste: "))
lists = []
for i in range(n):
    input_string = input(f"Introduceti elementele listei {i} separate printr-un spatiu:  ")
    input_string = input_string.split()
    lists.append(input_string)

print(apparition_tuples(lists))
