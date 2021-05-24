#!/usr/bin/env python3

import pathlib
import os
import re

from core import cfg, msg

filename = "voc.text"
folderpath = "/.local/share/vocabulary"
fulldirpath = os.path.expanduser("~") + folderpath
filepath = fulldirpath + "/" + filename


def writeToFile():

    if __isNothingToWrite__():
        msg.showEmptyDictMsg()
        return

    if not os.path.exists(fulldirpath):
        os.makedirs(fulldirpath)

    f = open(filepath, "a+")

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

    try:
        temp_list = __readFile__()

        for line in temp_list:
            newstr = line.strip().split(" - ")
            cfg.app_dict_loaded[newstr[0]] = newstr[1]

        cfg.is_dict_loaded = True
        print("Vocabulary loaded")
    except FileNotFoundError:
        print("File " + filename + " not exist")


def __isNothingToWrite__():
    if not cfg.is_word_added:
        return True
    return False


def __readFile__():

    try:
        f = open(filepath, "r")
        file_list = f.readlines()
        f.close()
        return file_list

    except FileNotFoundError as err:
        raise FileNotFoundError

    return list()
