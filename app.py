#!/usr/bin/env python3

import sys

import core.msg as msg
import core.cfg as cfg
import core.input_processor as ipp
import core.vocabulary as voc
import core.file_worker as fw


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
        elif ipp.isUserWantToView(user_input):
            voc.showContext()
        elif ipp.isUserWantToViewHelp(user_input):
            msg.showHelp()
        elif ipp.isUserWantToWriteToFile(user_input):
            fw.writeToFile()
        elif ipp.isUserWantToLoadDict(user_input):
            fw.loadFromFile()
        elif ipp.isUserWantToClearScreen(user_input):
            ipp.clearScreen()
        else:
            msg.showErrorMsg()


main()
