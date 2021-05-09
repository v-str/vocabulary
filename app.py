#!/usr/bin/env python3

import msg
import cfg
import input_processor as ipp


def main():
    msg.showBanner(cfg.program_name)
    msg.showBanner(cfg.helpText())
    runMainLoop()


def runMainLoop():
    while cfg.program_is_running:
        if not cfg.ready_to_run_vocabulary:
            ipp.acquireLaunchConfirmation()
        else:
            # vocabulary.addWord()


main()
