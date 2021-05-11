#!/usr/bin/env python3


def writeToFile(d):
    f = open("test.file", "a+")
    f.write("Vocabulary program\n")

    for count, key in enumerate(d, 1):
        line = str(count) + ") " + str(key) + " - " + str(d[key]) + "\n"
        f.write(line)

    f.close()
