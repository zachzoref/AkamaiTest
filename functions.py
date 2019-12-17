#!/usr/bin/python3
import json

def t_read(file_name):
    with open(file_name, "r") as pointer:
        return json.load(pointer)

def t_write(content, file_name):
    with open(file_name, "w+") as pointer:
        pointer.write(str(content))
