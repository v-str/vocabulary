#!/usr/bin/env python3

import sys

from core import msg
from core import cfg
from core import input_processor as ipp
from core import vocabulary as voc
from core import file_worker as fw


def main():
    msg.showBanner()
    msg.showHelp()
    runMainLoop()

# q - quit
# a - add
# v - view
# h - help
# w - write to file
# l - load from file


def runMainLoop():
    while cfg.program_is_running:
        user_input = ipp.getUserInputString(cfg.enter_sym)
        if ipp.isUserWantToQuit(user_input):
            sys.exit()
        elif ipp.isUserWantToAdd(user_input):
            voc.tryToAdd()
        elif ipp.isUserWantToView(user_input):
            voc.showContext()
        elif ipp.isUserWantToViewHelp(user_input):
            msg.showHelp()
        elif ipp.isUserWantToWriteToFile(user_input):
            fw.writeToFile()
        elif ipp.isUserWantToLoadDict(user_input):
            fw.loadFromFile()
        else:
            msg.showErrorMsg()


main()
