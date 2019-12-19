#!/usr/bin/python3
import functions
import json

t1_json = functions.t_read("tree1.txt")
t2_json = functions.t_read("tree2.txt")
print(json.dumps(t1_json, indent=4, sort_keys=True))
print(json.dumps(t2_json, indent=4, sort_keys=True))


def get_keys(arr):
    new_arr = []
    for i in arr:
        if type(i) != dict:
            new_arr.append(i)
        else:
            new_arr.append(next(iter(i)))
    return new_arr


def new_func(t1, el):
    # print("t1:", t1, "el:", el)
    found_basic = False
    found_middle = False
    # final = ""
    missing_dict = {}
    for i in t1:
        if type(i) == type(el):
            if i == el:
                # print("found one, returning")
                return True
            elif type(i) == dict:
                el_key = next(iter(el))
                i_key = next(iter(i))
                if i_key == el_key:
                    if type(i[i_key]) != list:
                        i[i_key] = [i[i_key]]
                        # print(i[i_key], type(i[i_key]))
                    list_of_missing = []
                    for j in el[el_key]:
                        value = new_func(i[i_key], j)
                        # print("the value is:", value)
                        if value != True:
                            list_of_missing.append(value)
                            found_basic = True
                            found_middle = True
                        else:
                            found_basic = True
                    missing_dict[el_key] = list_of_missing
    if not found_basic:
        # print("returning el:", el)
        return el
    elif found_middle:
        # print("returning missing noderrrrr:", missing_dict)
        return missing_dict
    else:
        return True


def compare_arr(t2, t1):
    for i in t1:
        value = new_func(t2, i)
        if value != True:
            print("yay", value)


compare_arr(t1_json, t2_json)
