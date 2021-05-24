#!/usr/bin/env python3

program_is_running = True
ready_to_run_vocabulary = False
program_name = "English Vocabulary"
enter_sym = "#: "
add_t = ("A", "a")
view_t = ("V", "v")
help_t = ("H", "h")
write_t = ("W", "w")
load_t = ("L", "l")
quit_t = ("Q", "q")
clear_t = ("C", "c")
placeholder = "-"

app_dict = dict()
app_dict_loaded = dict()
raw_word = str("raw")
tr_word = str("tr")
is_word_added = False
is_dict_loaded = False


def helpText():
    text = ("'<A-a>' add word\n"
            "'<V-v>' view vocabulary\n"
            "'<H-h>' view help\n"
            "'<W-w>' write to file <voc.txt>\n"
            "'<L-l>' load from file <voc.txt>\n"
            "'<C-c>' clear screen\n"
            "'<Q-q>' quit program")
    return text


def errorText():
    text = ("something is wrong, press '<H-h>' to view available commands")
    return text


def emptyDictText():
    text = ("dictionary is empty")
    return text
