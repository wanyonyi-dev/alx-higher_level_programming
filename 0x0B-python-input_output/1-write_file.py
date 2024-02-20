#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file.
    If file do not exist - it creates it
    otherwise - overwrite the content of the file

    Args:
      filename: text filename (str)
      text: the content (str)
    Returns: the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as txt_file:
        txt_file.write(text)
    return len(text)

