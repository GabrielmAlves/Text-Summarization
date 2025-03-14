import spacy
from spacy.lang.pt.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

nlp = spacy.load('pt_core_news_lg')

def process_text(text):
    doc = nlp(text)

    important_words = []
    stopwords = list(STOP_WORDS)
    pos_tag_list = ['ADJ', 'PROPN', 'NOUN', 'VERB']
    
    for token in doc:
        if (token.text in stopwords or token.text in punctuation):
            continue
        if (token.pos_ in pos_tag_list):
            important_words.append(token.text)
            
    for t in important_words:
        print(t)