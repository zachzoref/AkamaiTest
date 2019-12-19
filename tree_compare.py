#!/usr/bin/python3

import argparse
import functions
import json

def init_args():
    parser = argparse.ArgumentParser("")
    parser.add_argument("tree1", help="The first tree file name. By default it looks for a file called tree1.txt in the pwd",
                        default="tree1.txt", nargs="?")
    parser.add_argument("tree2", help="The second tree file name. By default it looks for a file called tree2.txt in the pwd",
                        default="tree2.txt", nargs="?")
    parser.add_argument("-p", "--pretty",
                        help="Pretty print the diff between the trees",
                         action="store_true")
    args = parser.parse_args()

    return args.tree1, args.tree2, args.pretty

"""
The following function receives a "tree" and an element to look for in the tree.
The function iterates over the input tree, and if it finds an equal element, it returns a None.
If not, it returns the exact difference between similar elements.
The function works by recursively checking dictionaries containing more lists,
in order to get to the final element which is not equal to the original,
and then returns the keys which points to the difference, step by step, backwards.
It consists of O(n) time complexity, and the overall program is O(m*n).
"""
def search_in(tree, element):
    # Initiating the necessary variables
    found_basic = False
    different_dict = False
    diff_dict = {}

    # Iterating over the tree to identify equal or similar element
    for i in tree:

        # Checking if the types are the same
        if type(i) == type(element):

            # Checking if they are equal. If so, exit the function.
            if i == element:
                return None

            # If they are not the same, and it's a dictionary,
            # we have to check the nesting elements.
            elif type(i) == dict:

                # Identifiying if the keys are the same
                element_key = next(iter(element))
                i_key = next(iter(i))
                if i_key == element_key:
                    # If the content of the checked element is not a list,
                    # enter it to a list so we can iterate over it
                    if type(i[i_key]) != list:
                        i[i_key] = [i[i_key]]

                    list_of_missing = []
                    # We found a different dictionary with identical keys,
                    #so we have to make sure we don't return the whole element,
                    #but only the missing nested elements.
                    found_basic = True

                    # Iterating over the elements in our dictionary to find the different values
                    for j in element[element_key]:
                        # Recursively entering the function until finding a difference.
                        value = search_in(i[i_key], j)

                        # If we found a different element inside,
                        # we append it to the final array of different elements.
                        if value != None:
                            list_of_missing.append(value)
                            different_dict = True

                    # If it's only one missing element, a list is not necessary
                    if len(list_of_missing) == 1:
                        list_of_missing = list_of_missing[0]

                    # Implementing the final dictionary to return to the parent running function
                    diff_dict[element_key] = list_of_missing

    if not found_basic:
        return element

    elif different_dict:
        return diff_dict

    else:
        return None

"""
The following function is somewhat the main function to run the core recursive function.
It iterates over a tree and finds what is missing from another tree.
"""
def compare_trees(t1, t2):

    diff_list = []
    for i in t2:
        diff = search_in(t1, i)
        if diff != None:
            diff_list.append(diff)
    return diff_list

"""
This function is the answer to the bonus question: pretty print the diff tree.
It iterates over the tree and recursively prints the dictionaries.
"""
def pretty_print(tree, level = 0):

    for i in tree:
        if type(i) != dict:
            print("   " * level, "+-- {} {}".format(i, type(i)))
        else:
            i_key = next(iter(i))
            print("   " * level, "+--+ {} {}".format(i_key, type(i)))
            level += 1
            pretty_print(i[i_key], level)


def main():
    t1, t2, pretty = init_args()

    t1_json = functions.t_read(t1)
    t2_json = functions.t_read(t2)

    t1_diff = compare_trees(t1_json, t2_json)
    t2_diff = compare_trees(t2_json, t1_json)

    if len(t1_diff) > 0:
        if pretty:
            print("Tree 1 is missing the following elements:")
            pretty_print(t1_diff)

        t1_file_content = "Tree 1 missing \n" + json.dumps(t1_diff, indent=4, sort_keys=True)
        functions.t_write(t1_file_content, "tree1_diff.txt")
        print("The diff comparison between tree2 to tree1 was exported to the file tree1_diff.txt successfully\n")

    if len(t1_diff) > 0:
        if pretty:
            print("Tree 2 is missing the following elements:")
            pretty_print(t2_diff)

        t2_file_content = "Tree 2 missing \n" + json.dumps(t2_diff, indent=4, sort_keys=True)
        functions.t_write(t2_file_content, "tree2_diff.txt")
        print("The diff comparison between tree1 to tree2 was exported to the file tree2_diff.txt successfully\n")


if __name__ == "__main__":
    main()
