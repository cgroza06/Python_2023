def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key not in dictionary.keys():
            continue

        if not dictionary[key].startswith(prefix):
            return False

        if not dictionary[key].endswith(suffix):
            return False

        if not middle in dictionary[key]:
            return False

        if prefix == "":
            if dictionary[key].startswith(middle):
                return False
        if suffix == "":
            if dictionary[key].endswith(middle):
                return False

        #am ajuns aici, deci am trecut de toate testele
        #verificam ca middle sa nu se gaseasca nici la inceputul cuvantului, nici la final
        if dictionary[key].startswith(middle) or dictionary[key].endswith(middle):
            return False

        #verificam sa nu fie alte chei in dictionar
        rule_keys = {rule[0] for rule in rules}
        if set(dictionary.keys()) - rule_keys !=0 : #raman valorile din dictionary care nu se gasesc in rule_keys
            return False

        return True

s={("key1", "come", "inside", ""), ("key2", "start", "white", "winter")}
d={"key1": "come , it's too cold out"}

print(validate_dict(s,d))