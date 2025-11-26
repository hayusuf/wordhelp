"""Tests for define_word.py"""
import re
import pyperclip
from define_word import define_clipboard

def test_words():
    """Checking the words that are returned by define_word."""
    pyperclip.copy("A cupel or cupelling hearth in which precious metals are " \
    "melted for trial and refinement")
    words = pyperclip.paste()
    words = set(re.findall(r"\b\w+\b", words))
    returned_words = define_clipboard(True)
    assert words == returned_words

def test_output(capsys):
    """Checking that correct definition is returned."""
    pyperclip.copy("cupel")
    output = "1. cupel\n\t\tnoun\n\t\t1) A small circular receptacle used in " \
    "assaying gold or silver with lead.\n\n\t\tSynonyms: \n\t\tAntonyms: \n\n\t\tverb\n\t\t1) To refine by means of a cupel.\n\n\t\tSynonyms: \n\t\tAntonyms: \n\n\n"
    define_clipboard(True)
    captured = capsys.readouterr()
    assert output == captured.out
