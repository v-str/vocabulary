#!/usr/bin/env python3

placeholder = "*"
range_len = 100


def showBanner(title="Empty"):
    showHead()
    showTitle(title)


def showHead():
    line = ""
    for i in range(0, range_len):
        line += placeholder

    print(line)


def showTitle(title):
    title_len = len(title)
    print("Title: ", title, " len: ", title_len)
