#!/usr/bin/env python3

import sys

placeholder = " "
title_text = ""
range_len = 100
border_len = 2
border_text = " "


def showBanner(title="Empty"):
    showLine()
    try:
        title_text = str(title)
        showTitle(title)
    except TypeError as err:
        printError("showTitle", err)
        sys.exit("Exit")
    showLine()


def showLine():
    line = fillLineWith(placeholder, range_len)
    print(line)


def showTitle(title):
    title_len = len(title)
    total = range_len - title_len - border_len
    before_title_len = round(total / 2)
    after_title_len = before_title_len

    if total % 2:
        after_title_len += 1

    line_before = fillLineWith(placeholder, before_title_len)
    line_after = fillLineWith(placeholder, after_title_len)

    final_title = (line_before, border_text, title,
                   border_text, line_after)
    print(final_title)


def fillLineWith(symbol, range_end=0):
    line = ""
    for i in range(0, range_end):
        line += symbol

    return line


def printError(funcName, err_msg):
    print("Error in function: ", funcName)
    print("Error message: ", err_msg)
