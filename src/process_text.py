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
            
    words_frequency = find_word_frequency(important_words)        
    
    normalize_words_frequency(words_frequency)

def find_word_frequency(keyword):
    word_frequency = Counter(keyword)
    
    return word_frequency

def normalize_words_frequency(words_frequency):
    max_frequency = words_frequency.most_common(1)[0][1]
    for word in words_frequency.keys():
        words_frequency[word] = (words_frequency[word]/max_frequency)
    
    return words_frequency.most_common(10)