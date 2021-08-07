#!/usr/bin/bash

regex_pat='(\/usr\/lib\/)(instantclient\/)(lib.*)'

for file in /usr/lib/instantclient/*
do
    if [["${file}" =~ $regex_pat]]
    then
        ln -s ${file} ${BASH_REMATCH[0]}${BASH_REMATCH[2]}
    fi
done