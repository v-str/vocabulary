#!/usr/bin/env python3

import sys

import msg
import cfg
import input_processor as ipp


def main():
    msg.showBanner(cfg.program_name)
    msg.showBanner(cfg.helpText())
    runMainLoop()


def runMainLoop():
    while cfg.program_is_running:
        user_input = ipp.getUserInputString()
        if ipp.isUserWantToStart(user_input):
            pass
        elif ipp.isUserWantToQuit(user_input):
            cfg.program_is_running = False


main()
