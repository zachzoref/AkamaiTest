#!/usr/bin/python3
import json

def t_read(file_name):
    with open(file_name, "r") as pointer:
        try:
            return json.load(pointer)
        except:
            print("There was an error converting the content of {} ".format(file_name) +
                  "into a Python json object, please check the content and try again.")
            exit(1)

def t_write(content, file_name):
    with open(file_name, "w+") as pointer:
        pointer.write(str(content))
