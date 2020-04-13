#!/bin/bash
rm -rf docs
pdoc --html labs --output-dir docs --force

mv docs/labs/* docs
rmdir docs/labs

if [[ $1 == "--open" ]] ||
    [[ $2 == "--open" ]] ||
    [[ $1 == "-open" ]] ||
    [[ $2 == "-open" ]] ||
    [[ $1 == "open" ]] ||
    [[ $2 == "open" ]] ||
    [[ $1 == "o" ]] ||
    [[ $2 == "o" ]]; then
    open docs/index.html
else
    echo "open docs/index.html"
fi
