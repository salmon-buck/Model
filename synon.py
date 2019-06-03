from word2vec.readDB import *
from nltk.corpus import wordnet

def synonyms(query) :
    synonyms = []
    antonyms = []
    for syn in wordnet.synsets(query):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

    print(set(synonyms))
    print(set(antonyms))

q=input().split()
for w in q :
    if w not in total_word :
        print(w)
        synonyms(w)