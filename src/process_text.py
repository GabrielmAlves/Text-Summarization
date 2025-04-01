import spacy
from spacy.lang.pt.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

nlp = spacy.load('pt_core_news_lg')

sentence_strength = {}

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
    
    weigh_sentences(doc, words_frequency)
    
    summarized_sentences = nlargest(3, sentence_strength, key=sentence_strength.get)
    print(summarized_sentences)
    
    final_sentences = [ w.text for w in summarized_sentences]
    summary = ' '.join(final_sentences)
    
    return summary 

def find_word_frequency(keyword):
    word_frequency = Counter(keyword)
    
    return word_frequency

def normalize_words_frequency(words_frequency):
    max_frequency = words_frequency.most_common(1)[0][1]
    for word in words_frequency.keys():
        words_frequency[word] = (words_frequency[word]/max_frequency)
    
    return words_frequency

def weigh_sentences(document, words_frequency):
    for sent in document.sents:
        for word in sent:
            if word.text in words_frequency.keys():
                if sent in sentence_strength.keys():
                    sentence_strength[sent]+=words_frequency[word.text]
                else:
                    sentence_strength[sent] = words_frequency[word.text]
    print(sentence_strength)