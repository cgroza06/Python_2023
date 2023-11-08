def loop(mapping):
    visited = set()
    current_key = "start"
    result = []
    while current_key not in visited:
        visited.add(current_key)
        value = mapping[current_key]
        if value in visited:
           break
        result.append(value)
        current_key = value

    return result

mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
print(loop(mapping))