#!/usr/bin/env python3

enter_sym = "#:"
start_tuple = ("S", "s", "start", "Start")
quit_tuple = ("Q", "q", "quit", "Quit")


def getUserInputString():
    return str(input(enter_sym))


def isUserWantToStart(user_input):
    return user_input in start_tuple


def isUserWantToQuit(user_input):
    return user_input in quit_tuple
