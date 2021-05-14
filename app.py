#!/usr/bin/env python3

import sys

from core import msg
from core import cfg
from core import input_processor as ipp
from core import vocabulary as voc


def main():
    msg.showBanner()
    msg.showHelp()
    runMainLoop()


def runMainLoop():
    while cfg.program_is_running:
        user_input = ipp.getUserInputString(cfg.enter_sym)
        if ipp.isUserWantToQuit(user_input):
            sys.exit()
        elif ipp.isUserWantToAdd(user_input):
            voc.tryToAdd()
        elif ipp.isUserWantToShow(user_input):
            voc.showContext()
        elif ipp.isUserWantToViewHelp(user_input):
            msg.showHelp()
        else:
            msg.showErrorMsg()


main()
