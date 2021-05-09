#!/usr/bin/env python3

import cfg
import msg
import sys


def getUserInputString(prefix=""):
    return str(input(prefix + cfg.enter_sym))


def isUserWantToStart(user_input):
    return user_input in cfg.start_tuple


def isUserWantToQuit(user_input):
    return user_input in cfg.quit_tuple


def acquireLaunchConfirmation():
    user_input = getUserInputString()
    if isUserWantToStart(user_input):
        cfg.ready_to_run_vocabulary = True
    elif isUserWantToQuit(user_input):
        cfg.program_is_running = False
