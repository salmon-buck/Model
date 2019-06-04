#!/usr/bin/env python
# coding: utf-8

# In[4]:


from readDB import *
from preProcessing import preProcessing
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import defaultdict


def fn_nvarFilt(poses, nvar):
    nvjr = list(nvar)
    ja = lambda tag: tag if tag != 'j' else 'a'
    nvars = [(p0, ja(p1[:1].lower())) for p0, p1 in poses if p1[:1] in nvjr]
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(nvar[0], pos=nvar[1]) for nvar in nvars]

def FindN(query):
    tokens = word_tokenize(query.lower())
    poses = pos_tag(tokens)
    nltk_res = fn_nvarFilt(poses, 'N')
    nltk_freq = defaultdict(int)
    for token in nltk_res:
        nltk_freq[token] += 1
    return nltk_res

# FindN 을 사용하여 쿼리에서 명사를 추출하여 Boolean에 사용

q=input() #쿼리 입력 ex) warm chicken with onion

candidate=FindN(q)   # candidate = [chicken,onion]
print(candidate)


# In[21]:


def boolean_Ingredient(q_ing, db_ing) :
    for food in db.keys():
        flag = 0
        s = db[food]['ingredient']
        for qu in (q_ing):
            if qu not in s:
                break;
            else:
                flag += 1 
        if flag == len(q_ing):
            print(food)
    return db_ing

data = boolean_Ingredient(candidate, db) # data에는 chicken과 onion이 포함된 커리만 출력됨

