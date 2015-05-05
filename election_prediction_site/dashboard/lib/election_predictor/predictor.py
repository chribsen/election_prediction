__author__ = 'Christian'


class Predictor:

    def __init__(self):
        self.afinn = None

    def init_words(self):
        self.afinn = dict(map(lambda (k,v): (k,int(v)),
                     [ line.split('\t') for line in open("AFINN-111.txt") ])) #TODO: Get path

    def get_sentiment(self, corpus):
        return sum(map(lambda word: self.afinn.get(word, 0), corpus.lower().split()))

