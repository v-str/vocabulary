#!/usr/bin/env python3

import os

from core import cfg
from core import msg


def getUserInputString(prefix=""):
    return str(input(prefix))


def isUserWantToAdd(user_input):
    return user_input in cfg.add_t


def isUserWantToView(user_input):
    return user_input in cfg.view_t


def isUserWantToViewHelp(user_input):
    return user_input in cfg.help_t


def isUserWantToQuit(user_input):
    return user_input in cfg.quit_t


def isUserWantToWriteToFile(user_input):
    return user_input in cfg.write_t


def isUserWantToLoadDict(user_input):
    return user_input in cfg.load_t


def isUserWantToLoadAnyway():
    while True:
        user_input = input("Y,n: ")
        if user_input in ('Y', 'y'):
            return True
        elif user_input in ('N', 'n'):
            return False


def isUserWantToClearScreen(user_input):
    return user_input in cfg.clear_t


def clearScreen():
    os.system('clear')
