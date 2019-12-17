#!/usr/bin/python3
import functions
import json

t1_json = functions.t_read("tree1.txt")
t2_json = functions.t_read("tree2.txt")
print(json.dumps(t1_json, indent=4, sort_keys=True))
print(json.dumps(t2_json, indent=4, sort_keys=True))

def is_there(tree, element):
    missing = []

    print("the tree is:", tree, "and the element is: ", element)
    print("tree type: ", type(tree), "element type: ", type(element))
    if type(tree) != list and type(element) != list and type(element) != dict:
        print("tree is not a list and element is not list & dict")
        if tree != element:
            return str(element)
    else:
        print("got into else 19")
        for i in tree:
            print(i)

            if element == i:
                print("element equals i")
                return True

            elif type(element) == dict and type(i) == dict:
                print("element and i are dicts")
                element_key = next(iter(element))
                i_key = next(iter(i))

                if element_key != i_key:
                    print("keys of dicts not the same")
                    missing.append(element)
                else:
                    if type(element[element_key]) == list:
                        print("the content of dict is list")
                        for element_child in element[element_key]:
                            value = is_there(i[i_key], element_child)

                            if value != True:
                                print("the value is: ",value)
                                missing.append("{} => {}".format(element_key,str(value)))
                                print("the missing is: ",missing)
                    else:
                        print("the content of dict is not a list")
                        value = is_there(i[i_key], element[element_key])
                        if value != True:
                            print("shittt")
                            missing.append(value)
    print("adding element to missing 50")
    missing.append(element)
    return missing


for i in t1_json:
    #print(i)
    value = is_there(t2_json, i)
    if value != True:
        print(value)
