#!/usr/bin/env python3

import cfg
import msg
import sys

enter_sym = "#:"
start_tuple = ("S", "s", "start", "Start")
quit_tuple = ("Q", "q", "quit", "Quit")


def getUserInputString():
    return str(input(enter_sym))


def isUserWantToStart(user_input):
    return user_input in start_tuple


def isUserWantToQuit(user_input):
    return user_input in quit_tuple


def acquireLaunchConfirmation():
    user_input = getUserInputString()
    if isUserWantToStart(user_input):
        cfg.ready_to_run_vocabulary = True
    elif isUserWantToQuit(user_input):
        cfg.program_is_running = False
