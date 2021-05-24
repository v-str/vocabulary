#!/usr/bin/env python3

import sys

import core.cfg as cfg

range_len = 100
border_len = 2
border_text = " "


def showBanner():
    showLine(cfg.placeholder)
    try:
        showTitle(cfg.program_name, cfg.placeholder)
    except TypeError as err:
        printError("showTitle", err)
        sys.exit("Exit")
    showLine(cfg.placeholder)


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


def showHelp():
    print(cfg.helpText())


def showErrorMsg():
    print(cfg.errorText())


def showEmptyDictMsg():
    print(cfg.emptyDictText())


def showPreLoadMsg():
    print("Your current vocabulary contain some data.\n"
          "If you load vocabulary from file, current vocabulary will be lost.\n"
          "Proceed?\n")
