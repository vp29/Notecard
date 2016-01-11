__author__ = 'Erics'

from classes.QA import QA

sentence = "Saturation means SATURATED w/ H BONDS i.e NO cis C=C bonds"

quest = QA(sentence)

print "Testing definition question"
quest.create_def()
print quest.question
print quest.answer

print "\n\nTesting Fill in the blank question"
quest.create_fib()
print quest.question
print quest.answer

