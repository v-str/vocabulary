#!/usr/bin/env python3

placeholder = "*"
range_len = 100

def showBanner(string = "Empty"):
	showHead()
	showTitle(string)

def showHead():
    line = ""
    for i in range(0, range_len):
        line += placeholder

    print(line)

def showTitle(string):
	title_len = len(string)
	print("Title: ", string, " len: ", title_len)
