#!/bin/python3
name = input('What is your name?')
if name in ['Gemma', 'Debbie'] :
    output = "Hello %s, good to see you again!" % name
else:
    output = "Hello %s, nice to meet you!" % name

print(output)
