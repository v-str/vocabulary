#!/usr/bin/env python3

from core import msg
from core import cfg
from core import input_processor as ipp
from core import vocabulary
from core import file_worker


def main():
    msg.showBanner()
    msg.showHelp()
    # mainLoop()


def runMainLoop():
    while cfg.program_is_running:
        if not cfg.ready_to_run_vocabulary:
            ipp.acquireLaunchConfirmation()
        else:
            vocabulary.tryToAdd()

    vocabulary.showContext()
    file_worker.writeToFile(cfg.app_dict)


main()
