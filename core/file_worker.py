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

    f = open(filename, "a+")

    fpath = str(pathlib.Path(filename).parent.absolute())
    ff = fpath + "/" + filename

    # if os.stat(ff).st_size == 0:

    for count, key in enumerate(cfg.app_dict, 1):
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
