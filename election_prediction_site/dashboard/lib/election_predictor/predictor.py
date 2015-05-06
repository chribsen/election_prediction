__author__ = 'Christian'
from textstat.textstat import textstat


class Predictor:

    def __init__(self):
        self.afinn_words = None

    def init_words(self):
        self.afinn_words = dict(map(lambda (k, v): (k, int(v)),
                     [line.split('\t') for line in open("AFINN-111.txt")])) #TODO: Get path (in /danish_words dir)

    def get_sentiment(self, corpus):
        return sum(map(lambda word: self.afinn_words.get(word, 0), corpus.lower().split()))

    def get_readability(self, corpus, type='ari'):
        readability = None
        if type == 'ari':
            readability = textstat.automated_readability_index(corpus)
        elif type == 'flesch':
            readability = textstat.flesch_reading_ease(corpus)
        elif type == 'smog':
            readability = textstat.smog_index(corpus)
        elif type == 'flesch_kinciad':
            readability = textstat.flesch_kincaid_grade(corpus)
        elif type == 'coleman':
            readability = textstat.coleman_liau_index(corpus)
        elif type == 'dale_chall':
            readability = textstat.dale_chall_readability_score(corpus)
        elif type == 'difficult_words':
            readability = textstat.difficult_words(corpus)
        elif type == 'linsear':
            readability = textstat.linsear_write_formula(corpus)
        elif type == 'gunning_fog':
            readability = textstat.gunning_fog(corpus)
        elif type == 'readability_conensus':
            readability = textstat.readability_consensus(corpus)

        return readability

