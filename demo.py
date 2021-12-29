import spacy
import pickle
from nltk import tokenize

# python -m spacy download en_core_web_lg

nlp = spacy.load('en_core_web_md')

all_words = pickle.load(open("wordlist/words.pkl","rb"))
words = input()
words = tokenize(words)

score = []
for word in words:

    for words in all_words:
        words = nlp(words)
        word = nlp(word)
        score.append(word.similarity(words))
        print(score)