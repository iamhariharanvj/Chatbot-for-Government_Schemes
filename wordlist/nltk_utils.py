import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    stemmer = PorterStemmer()
    return stemmer.stem(word).lower()

def bag_of_words(tokenized_sentence,all_words):
    bag = np.zeros(len(all_words))
    stemmed_words = [stem(word) for word in tokenized_sentence]
    for index,word in enumerate(all_words):
        if word in stemmed_words:
            bag[index] +=1 

    return bag

    