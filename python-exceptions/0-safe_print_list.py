#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            if i > 0:
                print(", ", end="")
            print("{}".format(my_list[i]), end="")
            i += 1
        except:
            break
    print()
    return i
