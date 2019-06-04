from Model.readDB import *
from nltk.corpus import wordnet
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Data_Preprocessing.recipeProcess.preProcessing import preProcessing

import random

def synonyms(query, query_processed) :
    candidate = [[] for i in range(len(query))]
    count=0
    for w in query_processed :

        if w not in total_wordset :
            for syn in wordnet.synsets(query[count]):
                for l in syn.lemmas():
                    print(l.name())
                    print(preProcessing(l.name()))
                    if preProcessing(l.name())[0] in total_wordset :
                        print('얏호:', l.name())
                        candidate[count].append(preProcessing(l.name())[0])

        else :
            candidate[count].append(w)

        if not candidate[count]:
            candidate[count].append(w)

        count+=1

    return candidate

def randomPick(candidate) :
    query_list=[]
    itr=10
    mul=0
    for c in candidate :
        mul*=len(c)
    if mul<10 :
        itr=mul
    for i in range(itr) :
        query=[]
        for synonyms in candidate :
            tmp=random.choice(synonyms)
            query.append(tmp)
        query_list.append(query)

    return query_list

q=input()
q_processed=preProcessing(q)
q=q.split()
print(q, q_processed)
candidate=synonyms(q, q_processed)
print(candidate)
query_list=randomPick(candidate)
print(query_list)