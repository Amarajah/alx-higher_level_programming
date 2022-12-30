#!/usr/bin/python3
"""
Function that prints a text with 2 new lines
after each of these characters: ., ? and : .

"""


def text_indentation(text):
    """
    Checks if text is astring,else throws an error.

    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    """
    Indicates special characters to be noted.
    Use split to split the sentence.
    """
    split_text = re.split('[.?:]', text)

    for line in split_text:
        print(line.strip())
        if line[-1] in '.?:':
            print("\n")
