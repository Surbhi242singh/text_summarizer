#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#spaCy is object oriented
#nltk is string oriented

#spaCy is like iphone, gives best results
#nltk is like dslr, allows customization, can give best results once familiarized


# In[1]:


get_ipython().system('pip install spacy')
get_ipython().system('python -m spacy download en')


# In[5]:


text = """
Maria Sharapova has basically no friends as tennis players on the WTA Tour. The Russian player has no problems in openly speaking about it and in a recent interview she said: 'I don't really hide any feelings too much. 
I think everyone knows this is my job here. When I'm on the courts or when I'm on the court playing, I'm a competitor and I want to beat every single person whether they're in the locker room or across the net.
So I'm not the one to strike up a conversation about the weather and know that in the next few minutes I have to go and try to win a tennis match. 
I'm a pretty competitive girl. I say my hellos, but I'm not sending any players flowers as well. Uhm, I'm not really friendly or close to many players.
I have not a lot of friends away from the courts.' When she said she is not really close to a lot of players, is that something strategic that she is doing? Is it different on the men's tour than the women's tour? 'No, not at all.
I think just because you're in the same sport doesn't mean that you have to be friends with everyone just because you're categorized, you're a tennis player, so you're going to get along with tennis players. 
I think every person has different interests. I have friends that have completely different jobs and interests, and I've met them in very different parts of my life.
I think everyone just thinks because we're tennis players we should be the greatest of friends. But ultimately tennis is just a very small part of what we do. 
There are so many other things that we're interested in, that we do.'
"""


# In[6]:


import spacy
from spacy.lang.en.stop_words import STOP_WORDS
stopwords=list(STOP_WORDS)

from string import punctuation 

nlp=spacy.load('en_core_web_sm')
doc=nlp(text)


# Word Tokenization

# In[8]:


tokens=[token.text for token in doc]
print(tokens)


# In[9]:


punctuation=punctuation+'\n'
punctuation


# In[12]:


#counting word frequency

word_freq={}
for word in doc:
    if word.text.lower not in stopwords:
        if word.text not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text]=1
            else:
                word_freq[word.text]+=1


# In[13]:


print(word_freq)


# In[14]:


max_freq=max(word_freq.values())


# In[15]:


for word in word_freq.keys():
    word_freq[word]=word_freq[word]/max_freq


# In[16]:


print(word_freq)


# Sentence Tokenization

# In[17]:


sentence_tokens=[sent for sent in doc.sents]
print(sentence_tokens)


# In[18]:


#calculating sentence scores based on word frequency. Sentence with higher score will be considered in summarization
#sentence score is the summation of frequency of each word in that sentence


# In[19]:


sentence_scores = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_freq.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent]=word_freq[word.text.lower()]
            else:
                sentence_scores[sent]+=word_freq[word.text.lower()]


# In[20]:


print(sentence_scores)


# In[21]:


from heapq import nlargest

select_length=int(len(sentence_tokens)*0.3)    #selecting top 30% of the sentences, top=>largest scores


# In[25]:


summary=nlargest(select_length,sentence_scores,key=sentence_scores.get)
final_summary=[word.text for word in summary]
summary=' '.join(final_summary)


# In[23]:


print(text)


# In[26]:


print(summary)


# In[ ]:




