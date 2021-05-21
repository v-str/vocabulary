#!/usr/bin/env python3

import pathlib
import os
import re

from core import cfg
from core import msg

filename = "voc.text"


def writeToFile():

    if __isNothingToWrite__():
        msg.showEmptyDictMsg()
        return

    f = open(filename, "a+")

    for key in cfg.app_dict:
        line = str(key) + " - " + str(cfg.app_dict[key]) + "\n"
        f.write(line)

    cfg.app_dict.clear()
    cfg.app_dict_loaded.clear()
    cfg.is_word_added = False

    f.close()

    print("File ", filename, " written")


def loadFromFile():
    cfg.app_dict_loaded.clear()

    temp_list = __readFile__()

    for line in temp_list:
        newstr = line.strip().split(" - ")
        cfg.app_dict_loaded[newstr[0]] = newstr[1]

    cfg.is_dict_loaded = True
    print("Vocabulary loaded")


def __isNothingToWrite__():
    if not cfg.is_word_added:
        return True
    return False


def __readFile__():
    try:
        f = open(filename, "r")
        file_list = f.readlines()
        f.close()
        return file_list

    except FileNotFoundError as err:
        print("File not exist")

    return list()
