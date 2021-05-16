#!/usr/bin/env python3

import pathlib

filename = "voc.txt"


def writeToFile():
    f = open(filename, "a+")

    fpath = str(pathlib.Path(filename).parent.absolute())
    ffilename = fpath + "/" + filename

    print("ffilename: ", ffilename)

    #f.write("Vocabulary program\n")

    # for count, key in enumerate(d, 1):
    #    line = str(count) + ") " + str(key) + " - " + str(d[key]) + "\n"
    #    f.write(line)

    f.close()
