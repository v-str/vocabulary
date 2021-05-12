#!/usr/bin/env python3

program_is_running = True
ready_to_run_vocabulary = False
program_name = "English Vocabulary"
enter_sym = "#: "
add_t = ("A", "a")
show_t = ("S", "s")
help_t = ("H", "h")
quit_t = ("Q", "q")
placeholder = "-"

app_dict = dict()
raw_word = str("raw")
tr_word = str("tr")


def helpText():
    text = ("'<A-a>' to add word\n"
            "'<S-s>' to show vocabulary\n"
            "'<H-h>' to view help\n"
            "'<Q-q>' for quit program\n")
    return text


def errorText():
    text = ("Something is wrong\n")
    return text
