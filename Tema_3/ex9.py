def find_args(*pos_args,**keyword_args):
    count = 0
    for i in pos_args:
        if i in keyword_args.values():
            count += 1
    return count

print(find_args(1, 2, 3, x=1,y=2,z=3,w=5))