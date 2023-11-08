def ordered_tuples(tuple_list):
    sorted_list = sorted(tuple_list,key=lambda x:x[1][2])
    return sorted_list

n = int(input("Introduceti numarul de tumple: "))
tuple_list = []
for i in range (0,n):
    input_string = input("Introduceti elementele tuplei, separate printr-un spatiu: ")
    input_string=input_string.split()
    tuple_list.append(tuple(input_string))
print(ordered_tuples(tuple_list))
