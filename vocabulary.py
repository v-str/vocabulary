#!/usr/bin/env python3

import sys

import banner
import input_processor as ipp

program_is_running = True
program_name = "English Vocabulary"


def runMainLoop():
    while program_is_running:
        sys.exit()


def main():
    banner.showBanner(program_name)
    runMainLoop()


main()
