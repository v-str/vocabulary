#!/usr/bin/env python3

from core import cfg
from core import msg

def getUserInputString(prefix=""):
    return str(input(prefix))


def isUserWantToStart(user_input):
    return user_input in cfg.start_tuple


def isUserWantToQuit(user_input):
    return user_input in cfg.quit_tuple


def acquireLaunchConfirmation():
    user_input = getUserInputString(cfg.enter_sym)
    if isUserWantToStart(user_input):
        cfg.ready_to_run_vocabulary = True
    elif isUserWantToQuit(user_input):
        cfg.program_is_running = False
