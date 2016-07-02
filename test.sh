#!/bin/bash

function run_command() {
    local Command="$1"
    local Input="$2"
    local Prompt="$3"
    local Output="$(echo -e $Input|$Command)"
    echo ${Output#"$Prompt"}
}


function test_excercise() {
    local Command="$1"
    local Input="$2"
    local Prompt="$3"
    local Correct_out="$4"
    local Output="$(run_command "$Command" "$Input" "$Prompt")"

    if [[ "${Output}" != "$Correct_out" ]]; then
        echo "Error"
        echo "Output is ${Output}"
    fi
}

test_excercise ./ex1.py "Cian" "What is your name?" "Hello Cian, nice to meet you!"
test_excercise ./ex1.py "Gemma" "What is your name?" "Hello Gemma, good to see you again!"
test_excercise ./ex2.py "Cian" "What is the input string?" "Cian has 4 characters"
test_excercise ./ex2.py "Gemma" "What is the input string?" "Gemma has 5 characters"
test_excercise ./ex2.py "" "What is the input string?" "You need to enter a word"
test_excercise ./ex3.py "These aren't the droids you're looking for\nObi Wan Kenobi" "What is the quote?Who said it?" "Obi Wan Kenobi says \"These aren't the droids you're looking for\""
test_excercise ./ex4.py "dog\nwalk\nblue\nquickly\n" "Enter a noun?Enter a verb?Enter an adjective?Enter an adverb?" "Do you walk your blue dog quickly? That's a bit mad!"
