#!/usr/bin/env python3

import sys

range_len = 100
border_len = 2
border_text = " "
title_text = ""


def showBanner(title="Empty", placeholder=" "):
    showLine(placeholder)
    try:
        title_text = str(title)
        showTitle(title, placeholder)
    except TypeError as err:
        printError("showTitle", err)
        sys.exit("Exit")
    showLine(placeholder)


def showLine(placeholder):
    line = fillLineWith(placeholder, range_len)
    print(line)


def showTitle(title, placeholder):
    title_len = len(title)
    total = range_len - title_len - border_len
    before_title_len = round(total / 2)
    after_title_len = before_title_len

    if total % 2:
        after_title_len += 1

    line_before = fillLineWith(placeholder, before_title_len)
    line_after = fillLineWith(placeholder, after_title_len)

    final_title = (line_before + border_text +
                   title + border_text + line_after)
    print(final_title)


def fillLineWith(symbol, range_end=0):
    line = ""
    for i in range(0, range_end):
        line += symbol

    return line


def showText(text):
    print(text)
