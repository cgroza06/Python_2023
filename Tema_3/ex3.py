def are_obiectele_egale(obj1, obj2):
    if type(obj1) != type(obj2):
        return False

    # Dacă este un dicționar
    if isinstance(obj1, dict):
        # Verificăm dacă au aceleași chei
        if set(obj1.keys()) != set(obj2.keys()):
            return False

        for key in obj1.keys(): # Verificăm fiecare valoare recursiv
            if not are_obiectele_egale(obj1[key], obj2[key]):
                return False

    elif isinstance(obj1, (list, set)):
        if len(obj1) != len(obj2):
            return False

        for item1, item2 in zip(obj1, obj2):
            if not are_obiectele_egale(item1, item2):
                return False
    else:
        if obj1 != obj2:
            return False

    return True

dict1 = {"a": 1, "b": [1, 2, {"c": 3}], "d": {"e": [4, 5]}}
dict2 = {"a": 1, "b": [1, 2, {"c": 3}], "d": {"e": [4, 5]}}

if are_obiectele_egale(dict1, dict2):
    print("Obiectele sunt egale.")
else:
    print("Obiectele nu sunt egale.")
