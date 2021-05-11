#!/usr/bin/env python3

program_is_running = True
ready_to_run_vocabulary = False
program_name = "English Vocabulary"
enter_sym = "#: "
add_tuple = ("A", "a")
quit_tuple = ("Q", "q")

app_dict = dict()
raw_word = str("raw")
tr_word = str("tr")


def helpText():
    text = ("\tpress '<A-a>' to add word, "
            "'<Q-q>' for quit program\n\n")
    return text


def errorText():
    text = ("Something is wrong\n")
    return text
