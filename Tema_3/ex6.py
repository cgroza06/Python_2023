def count_unique_and_duplicates(input_list):
    unique_set = set()
    duplicates = set()

    for item in input_list:
        if item in unique_set:
            duplicates.add(item)
        else:
            unique_set.add(item)

    return len(unique_set), len(duplicates)

my_list = [1, 2, 2, 3, 4, 4, 5]
result = count_unique_and_duplicates(my_list)
print(result)
