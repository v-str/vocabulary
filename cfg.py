#!/usr/bin/env python3

program_is_running = True
ready_to_run_vocabulary = False
program_name = "English Vocabulary"
enter_sym = "#:"
start_tuple = ("S", "s", "start", "Start")
quit_tuple = ("Q", "q", "quit", "Quit")
app_dict = dict()


def helpText():
    text = ("\tpress '<S-s>tart' to start vocabulary, "
            "'<Q-q>uit' for quit program\n\n")
    return text


def errorText():
    text = ("Something is wrong\n")
    return text
