#!/usr/bin/env python3

import cfg
import msg
import input_processor as ipp


def tryToAdd():
    cfg.raw_word = addWord("word: ")

    if not ipp.isUserWantToQuit(cfg.raw_word):
        cfg.tr_word = addWord("<" + cfg.raw_word + "> translation: ")
    else:
        return

    if not ipp.isUserWantToQuit(cfg.tr_word):
        addToDict(cfg.raw_word, cfg.tr_word)


def addWord(text):
    word = ipp.getUserInputString(text)
    if ipp.isUserWantToQuit(word):
        cfg.program_is_running = False

    return word


def addToDict(first, second):
    cfg.app_dict[first] = second


def showContext():
    count = 1
    for k, v in cfg.app_dict.items():
        print(count, ") ", k, " - ", v)
        count += 1
