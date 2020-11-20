#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
__author__ = "Amanda Simmons, Pete Mayor, Jonny Sueck, and Daniel Lomelino"

import sys


def create_word_dict(filename):
    """Returns a word/count dict for the given file."""

    with open(filename, 'r') as f:
        file_content_lst = f.readlines()
        formatted_lst = []
        final_word_lst = []
        for line in file_content_lst:
            line = line.lower().strip('\n')
            formatted_lst.append(line)
        for line in formatted_lst:
            words = line.split()
            final_word_lst.extend(words)
        count_dict = {}
        for word in final_word_lst:
            if word in count_dict:
                count_dict[word] += 1
            else:
                count_dict[word] = 1
        return count_dict


def print_words(filename):
    """Prints one per line '<word> : <count>', sorted
    by word for the given file.
    """
    print_dict = create_word_dict(filename)
    for word in print_dict:
        print(word)
    return print_dict


def print_top(filename):
    """Prints the top count listing for the given file."""
    print_dict = create_word_dict(filename)
    sorted_list = sorted(print_dict.items(), key=lambda t: t[1], reverse=True)
    for t in sorted_list[:20]:
        print(f'{t[0]} : {t[1]}')


# This basic command line argument parsing code is provided and calls
# the print_words() and print_top() functions which you must implement.
def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
