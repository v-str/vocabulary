#!/usr/bin/env python3

from core import cfg
from core import msg
from core import input_processor as ipp
from core import file_worker as fw


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
    cfg.is_word_added = True


def showContext():
    # function enumerate let me enumerate my dictionary automatically
    # start - counter for beauty print
    counter = 1
    for enum, key in enumerate(cfg.app_dict, counter):
        print(enum, ") ", key, " - ", cfg.app_dict[key])
        counter += 1
    if cfg.is_dict_loaded:
        for enum, key in enumerate(cfg.app_dict_loaded, counter):
            print(enum, ") ", key, " - ", cfg.app_dict_loaded[key])


def vocabularyIsEmpty():
    return len(cfg.app_dict) == 0
