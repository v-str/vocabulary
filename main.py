#!/usr/bin/env python3

import banner
import input_processor as ipp

program_is_running = True


def main():
    while program_is_running:
        banner.showBanner("English Vocabulary")
        ipp.showHelpMsg()
        res = input()


main()
