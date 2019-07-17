# Irish Dictionary Checker Modules
# Saved as dictionary_functions.py
# Created by Davis Sandefur; last updated 22.12.14

"""This module contains all the functions needed to scrub teanglann.ie,
either in English or Irish , as well as the functions needed to parse the HTML
and create a running word list of the words."""

import urllib.request
import urllib.parse
import urllib.error

from bs4 import BeautifulSoup


def entry_lookup(word, language, version):
    """ This function searches and gets the data for entry and suggestion
    from teanglann.ie.
    """
    word = urllib.parse.quote_plus(word)
    word = '%20'.join(word.split('+'))
    language = language.lower()
    breis_slug = {"english": "eid", "irish": "fgb"}  # Path slug for teanglann

    if version == 'english':
        try:
            url = "http://teanglann.ie/en/"+breis_slug[language]+'/'+word
            response = urllib.request.urlopen(url)
        except urllib.error.HTTPError:
            return ['Audio Only'], ['Audio Only'], None
    if version == 'gaeilge':
        try:
            url = "http://teanglann.ie/ga/"+breis_slug[language]+'/'+word
            response = urllib.request.urlopen(url)
        except urllib.error.HTTPError:
            return ['Guth amháin'], ['Guth amháin'], None

    html = response.read()
    soup = BeautifulSoup(html)
    entry = soup.findAll("div", class_=breis_slug[language] + " entry")
    suggestions = soup.findAll("div", class_="suggestions")
    form_of = soup.findAll("div", class_="know")
    # print(bool(form_of))
    if not form_of:
        return entry, suggestions, None, url
    return entry, suggestions, form_of, url


def gaeilge_gaeilge(word):
    """ This function searches and gets the data for the An Foclóir Beag entry from teanglann.ie
    """
    word = urllib.parse.quote_plus(word)
    try:
        response = urllib.request.urlopen("http://teanglann.ie/en/fb/"+word)
    except urllib.error.HTTPError:
        pass

    html = response.read()
    soup = BeautifulSoup(html)
    entry = soup.findAll("div", class_="fb entry")
    return entry


def entry_cleanup(html):
        """This function appends the text of the html to the list and returns it"""
        entries = []
        try:
            for b in html:
                entries.append(b.get_text())
        except AttributeError:
            try:
                for b in html:
                    entries.append(b.get_text())
            except IndexError:
                return None
            except AttributeError:
                return html
            return html
        return entries


def string_cleanup(string):
    """ This function takes a string with excess whitespace and cleans it up
    """
    try:
        suggestions = str(string[0])
        suggestions = ' '.join(suggestions.split())

        return suggestions

    except:
        return ''


if __name__ == "__main__":
        entry, suggestions, form_of, url = entry_lookup("find out", "english", "english")
        print(entry)
        entry, suggestions, form_of, url = entry_lookup("bain le", "irish", "english")
        print(entry)
