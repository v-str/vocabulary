#!/bin/bin/env python3

import cfg
import msg
import input_processor as ipp


def addWord():
    raw_word = ipp.getUserInputString("word ")
    if ipp.isUserWantToQuit(raw_word):
        cfg.program_is_running = False
        print("Quit")
        return
    tr_word = ipp.getUserInputString("translation ")
    cfg.app_dict[raw_word] = tr_word
