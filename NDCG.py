
# coding: utf-8

# In[1]:


import numpy as np
from match import * 

def dcg_at_k(r, k, method=0):
    r = np.asfarray(r)[:k]
    if r.size:
        if method == 0:
            return r[0] + np.sum(r[1:] / np.log2(np.arange(2, r.size + 1)))
        elif method == 1:
            return np.sum(r / np.log2(np.arange(2, r.size + 2)))
        else:
            raise ValueError('method must be 0 or 1.')
    return 0

def ndcg_at_k(r, k, method=0):
    dcg_max = dcg_at_k(sorted(r, reverse=True), k, method)
    if not dcg_max:
        return 0.
    return dcg_at_k(r, k, method) / dcg_max

def find_rel(answer, query, answer_rel):
    rels = np.zeros((len(query)))
    for i in range(len(query)):
        if query[i] in answer:
            index = answer.index(query[i])
            rels[i] = answer_rel[index]
    
    return rels


# In[2]:


answerSet = {'warm soup' : ['Thai Green Curry Chicken Soup', 'Thai Red Curry Soup', 'Coconut Curry Chicken Soup', 'Miso Soup With Vermicelli, Mushrooms And Tofu', 'Thai Red Curry Noddle Soup'],
            'spicy thai chicken' : ['Thai Red Curry Noodle Soup', 'Thai Basil Chicken Bowls', 'Thai Chicken Buddha Bowls', 'Thai Red Curry Soup', 'Thai Coconut Curry Chicken'], 
            'cold noodle' : ['ZARU SOBA', 'Tofu Soba Noodles', 'Tofu soba noodles', 'Asian Garlic Noodles', 'Korean Beef Zucchini Noodles'],
            'chicken salad' : ['Caprese Avocado Salad', 'Chinese Chicken Salad', 'Asian-Style Cobb Salad', 'Asian Quinoa salad', 'Best Ever Classic Macaroni Salad']}

relSet = {'warm soup' : [1, 2, 1, 3, 3],
            'spicy thai chicken' : [3, 1, 1, 2, 1], 
            'cold noodle' : [3, 3, 3, 2, 1],
            'chicken salad' : [1, 3, 1, 1, 1]}


# In[3]:


r = 5
cnts = 1
tmpResult = []

for (doc, sim) in avgResult :
    tmpResult.append(doc)
    if cnts>=r :
        break
    cnts += 1

print(tmpResult)


# In[4]:


rel = find_rel(answerSet[q_origin], tmpResult, relSet[q_origin])
print(ndcg_at_k(rel, 5, 1))

