__author__ = 'Christian'

class Translator:

    def __init__(self):
        self.dummy = NotImplemented


    def translate(self, corpus, lang='en'):
        return NotImplementedError

class Filter:

    def __init__(self):
        self.dummy = NotImplemented

    def remove_stop_words(self, corpus, stop_words=None):
        return NotImplementedError

    def remove_special_chars(self, corpus):
        return NotImplementedError

