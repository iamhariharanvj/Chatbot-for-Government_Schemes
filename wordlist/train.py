import json
from sklearn.linear_model import LogisticRegression
import numpy as np
import pickle
from nltk_utils import tokenize,stem,bag_of_words

with open("intents.json","r") as f:
    intents = json.load(f)

tags = []
all_words = []
df = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)

    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        df.append([w,tag])


ignore_list = ["?","!",".",","]
all_words = [stem(w) for w in all_words if w not in ignore_list]

all_words = sorted(set(all_words))
tags = sorted(set(tags))

X_train = []
y_train = []

for (patterned_sentence,tag) in df:
    bag = bag_of_words(patterned_sentence,all_words)
    X_train.append(bag)
    y_train.append(tag)

X_train = np.array(X_train)
y_train = np.array(y_train)

model = LogisticRegression()
model.fit(X_train,y_train)
print("Model Trained Successfully......")

pickle.dump(model,open("models/Model V1.pkl","wb"))
pickle.dump(all_words,open('wordlist/words.pkl','wb'))
