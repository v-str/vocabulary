#!/usr/bin/env python3

import pathlib
import os

from core import cfg
from core import msg

filename = "voc.text"


def writeToFile():

    if __isNothingToWrite__():
        msg.showEmptyDictMsg()
        return

    temp_list, strings_len = __readFile__()

    f = open(filename, "a+")

    for count, key in enumerate(cfg.app_dict, strings_len):
        line = str(count) + ") " + str(key) + " - " + \
            str(cfg.app_dict[key]) + "\n"
        f.write(line)

    cfg.app_dict.clear()
    cfg.is_word_added = False

    f.close()

    print("File ", filename, " written")


def loadFromFile():
    temp_list, strings_len = __readFile__()
    if len(temp_list) == 0:
        print("Nothing to load")
    else:
        strings_len = len(cfg.app_dict)
        print("len of dict: ", strings_len)
        # parse strings from temp list
        # for line in temp_list:
        # temp_line = line
        # find number before ')' symbol
        # change that symbol to 'strings_len + 1'
        # find KEY after ')' sym but before '-' symbol
        # find VALUE after '-' symbol


def __isNothingToWrite__():
    if not cfg.is_word_added:
        return True
    return False


def __readFile__():
    try:
        f = open(filename, "r")
        file_list = f.readlines()
        strings_len = 0

        fpath = str(pathlib.Path(filename).parent.absolute())
        ff = fpath + "/" + filename

        if os.stat(ff).st_size != 0:
            # count lines and save line number
            strings_len = len(file_list) + 1
            f.close()
        else:
            f.close()

        return file_list, strings_len

    except FileNotFoundError as err:
        print("file not exist, nothing to read")

    return 1
