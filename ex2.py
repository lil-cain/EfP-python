#!/usr/bin/python3

string = input("What is the input string?")
if len(string) == 0:
    output = "You need to enter a word"
else:
    output = "%s has %d characters" % (string, len(string))

print(output)
