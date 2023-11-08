def apparitions(lists,x):
    all_lists = []
    for i in lists:
        all_lists.extend(i) # adaug elementele dintr-o lista la alta lista

    result = set()
    for i in all_lists:
        if all_lists.count(i) == x:
            result.add(i)

    return result


n = int(input("Introduceti numarul de liste :"))
lists = []
for i in range (0,n):
    list = input(f"Introduceti elementele listei {i + 1}:")
    list = list.split()
    list_i = []
    for j in list:
        list_i.append(j)
    lists.append(list_i)

x = int(input("Introduceti numarul de aparitii ale elementelor : "))
result = apparitions(lists,x)
print(f"Elementulele {result}, apare de exact {x} ori ")
