__author__ = 'Christian'
import goslate
import Stemmer


class Translator:

    def __init__(self):
        self.dummy = NotImplemented
        self.gs = goslate.Goslate()

    def translate(self, corpus):
        return self.gs.translate(corpus, 'en', source_language='da')


class Filter:

    def __init__(self):
        self.stemmer = Stemmer.Stemmer('danish')

    def remove_stop_words(self, corpus, stop_words=None):
        return NotImplementedError

    def remove_special_chars(self, corpus):
        return NotImplementedError

    def stem_word(self, word):
        return self.stemmer.stemWord(word)

    def stem_corpus(self, corpus):
        stemmed_corpus = ''
        for word in corpus.split(' '):
            stemmed_corpus = ' '.join([stemmed_corpus, self.stem_word(word)])
        return stemmed_corpus


