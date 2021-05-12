#!/usr/bin/env python3

from core import cfg
from core import msg


def getUserInputString(prefix=""):
    return str(input(prefix))


def isUserWantToAdd(user_input):
    return user_input in cfg.add_t


def isUserWantToShow(user_input):
    return user_input in cfg.show_t


def isUserWantToViewHelp(user_input):
    return user_input in cfg.help_t


def isUserWantToQuit(user_input):
    return user_input in cfg.quit_t
