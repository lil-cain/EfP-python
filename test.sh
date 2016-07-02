#!/bin/bash

function run_ex1() {
    local Output="$(echo $1|./ex1.py)"
    echo ${Output#"What is your name?"}
}

Output1=$(run_ex1 "Cian")
if [[ "$Output1" != "Hello Cian, nice to meet you!" ]]; then
    echo "Error"
    echo "Output is : $Output1"
fi
Output2=$(run_ex1 "Gemma")
if [[ "$Output2" != "Hello Gemma, good to see you again!" ]]; then
    echo "Error"
    echo "Output is $Output2"
fi
