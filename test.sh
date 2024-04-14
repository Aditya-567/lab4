#!/bin/bash

FILE="/E/shellscripts/login/lab4/index.html"
if [ -f "$FILE" ]; then
    echo "$FILE exists, opening..."
    "/c/Program Files (x86)/Google/Chrome/Application/chrome.exe" "$(cygpath -wa "$FILE")"
else
    echo "$FILE does not exist"
fi

