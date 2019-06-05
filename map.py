#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
from sklearn.metrics import average_precision_score


# In[35]:


# query
def mAP(query, answer):
    truth = np.zeros((5))
    for i in range(5):
        if answer[i] in query:
            truth[query.index(answer[i])] = 1
    score = [1,1,1,1,1]
    ap = average_precision_score(truth, score)
    return ap


# In[36]:


answer = ['Korean Curry', 'Asian Style Nachos', 'Sesame Chicken Potstickers', 'Slow Cooker Corn Chowder', 'Instant Pot Mushroom Risotto']
query = ['Korean Curry', 'Sesame Chicken Potstickers', 'Easy Chicken Tikka Masala', 'Asian Style Nachos', 'Instant Pot Mushroom Risotto']

mAP(query, answer)

#['Sema Chicken', 'Garlic Ginger Chicken Potstickers', 'Sesame Chicken Potstickers', 'Asian-Style Cobb Salad', 'Coconut Curry Chicken Soup', 'Asian Style Chicken Nuggets With Lemon Glaze', 'Sweet And Sour Stir-Fried Chicken', 'Chinese Orange Chicken', 'Chinese Chicken Salad', 'Chinese Beef with Broccoli', 'Slow Cooker Indian Butter Chicken', 'Easy Chicken Tikka Masala', 'Instant Pot Mushroom Risotto', 'Italian Wedding Soup', 'Mushroom Ramen', 'Asian Style Nachos', 'Korean Chicken Kabobs', 'Korean Curry', 'Instant Pot Chicken Tortilla Soup', 'Roasted Shrimp Enchiladas with Jalapeno Cream Sauce', 'Chicken Khao Soi', 'Thai Red Curry Noodle Soup', 'Thai Green Curry Chicken Soup', 'Thai Sweet Potato and Carrot Soup', 'Thai Peanut Chicken Noodles', 'Slow Cooker Corn Chowder']

