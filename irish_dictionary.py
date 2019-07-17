# teanglann.ie dictionary checker
# Saved as irish dictionary.py
# Created by Davis Sandefur; last update 22.12.14

import dictionary_functions

""" This file contains the main function, irish_dictionary, which combines all
the classes from the dictionary_functions.py folder to output the entries and
suggestions in list format, ready to be read off"""


def irish_dictionary(word, language, version):
    """ This function checks teanglann.ie for a word, Irish or English, and
    returns the word and related words. If no word exists, it returns similar
    words as given by the website.  """

    # Gets the entry and suggestions

    entry, suggestion, form_of, url = dictionary_functions.entry_lookup(word, language, version)
    # Get entries and suggestions in a list using HTMLRead class
    entries = dictionary_functions.entry_cleanup(entry)
    suggestions = dictionary_functions.entry_cleanup(suggestion)
    suggestions = dictionary_functions.string_cleanup(suggestions)

    if form_of is not None:  # If it exists
        form_of = dictionary_functions.entry_cleanup(form_of)
        form_of = dictionary_functions.string_cleanup(form_of)

    return entries, suggestions, form_of, url


def gaeilge_gaeilge(word):
    entry = dictionary_functions.gaeilge_gaeilge(word)
    entries = dictionary_functions.entry_cleanup(entry)
    return entries

if __name__ == '__main__':
    irish_entry, irish_suggestions, form_of, url = irish_dictionary('bain le', 'irish', 'english')
    english_entry, english_suggestions, foo, url2 = irish_dictionary('hello', 'english', 'english')
    print(form_of)
