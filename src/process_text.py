import spacy
from spacy.lang.pt.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

nlp = spacy.load('pt_core_news_lg')

print(nlp.pipe_names)