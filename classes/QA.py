__author__ = 'Erics'

import random


class QA:
    sentence = ""
    question = ""
    answer = ""
    words = []

    # This will eventually need to be turned into something different
    def_terms = ['means', 'mean', 'is']

    def __init__(self, sentence):
        self.sentence = sentence
        self.words = sentence.split(' ')

    # Create a fill in the blank question
    def create_fib(self):
        fib_word = random.randrange(0, len(self.words))
        self.question = ""
        self.answer = ""
        for i in range(len(self.words)):
            if i != fib_word:
                self.question += self.words[i] + " "
            else:
                self.question += "____"
                self.answer = self.words[i]

    # Create a definition question (if possible)
    def create_def(self):
        spl_sent = None
        for i in self.def_terms:
            if i in self.sentence:
                spl_sent = self.sentence.split(i)
                self.question = "What is the meaning of " + spl_sent[0]
                self.answer = spl_sent[1]
                break

        if spl_sent == None:
            self.question = None
            self.answer = None
