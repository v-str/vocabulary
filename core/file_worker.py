#!/usr/bin/env python3

import pathlib
import os

from core import cfg
from core import msg

filename = "voc.txt"


def writeToFile():

    if __isNothingToWrite__():
        msg.showEmptyDictMsg()
        return

    strings_len = __readFile__()

    f = open(filename, "a+")

    for count, key in enumerate(cfg.app_dict, strings_len):
        line = str(count) + ") " + str(key) + " - " + \
            str(cfg.app_dict[key]) + "\n"
        f.write(line)

    cfg.app_dict.clear()
    cfg.is_word_added = False

    f.close()

    print("File ", filename, " written")


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
            print("File is not empty.")
            # count lines and save line number
            strings_len = len(file_list) + 1
            print("len: ", strings_len)
            f.close()
        else:
            f.close()

        return strings_len

    except FileNotFoundError as err:
        print("file not exist, nothing to read")

    return 1
