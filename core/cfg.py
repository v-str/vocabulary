#!/usr/bin/env python3

program_is_running = True
ready_to_run_vocabulary = False
program_name = "English Vocabulary"
enter_sym = "#: "
add_t = ("A", "a")
show_t = ("S", "s")
help_t = ("H", "h")
write_t = ("W", "w")
load_t = ("L", "l")
quit_t = ("Q", "q")
placeholder = "-"

app_dict = dict()
raw_word = str("raw")
tr_word = str("tr")


def helpText():
    text = ("'<A-a>' add word\n"
            "'<S-s>' show vocabulary\n"
            "'<H-h>' view help\n"
            "'<W-w>' write to file <voc.txt>\n"
            "'<L-l>' load from file <voc.txt>\n"
            "'<Q-q>' quit program\n")
    return text


def errorText():
    text = ("something is wrong, press '<H-h>' to view available commands")
    return text
