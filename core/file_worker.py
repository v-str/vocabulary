#!/usr/bin/env python3

import pathlib
import os

from core import cfg

filename = "voc.txt"


def writeToFile():
    f = open(filename, "a+")

    fpath = str(pathlib.Path(filename).parent.absolute())
    ff = fpath + "/" + filename

    # if os.stat(ff).st_size == 0:

    for count, key in enumerate(cfg.app_dict, 1):
        line = str(count) + ") " + str(key) + " - " + \
            str(cfg.app_dict[key]) + "\n"
        f.write(line)

    f.close()

    print("File ", filename, " written")
