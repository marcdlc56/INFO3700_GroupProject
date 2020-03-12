import spacy
from spacy import displacy
from spacy.lang.en.stop_words import STOP_WORDS
import pandas as pd

import string
import pickle

text = ''
for line in open('output.txt', 'r'):
    text = text + str((line.strip()))

nlp = spacy.load('en_core_web_sm')

doc = nlp(text)

sent = nlp.create_pipe('sentencizer')

nlp.add_pipe(sent, before='parser')

stopwords = list(STOP_WORDS)

displacy.render(doc, style = 'dep')

displacy.render(doc, style = 'ent')

punct = string.punctuation

punct = punct + '—' + '\'' + "\"" + "\"" + "“" + '“'
doc = nlp(text)

tokens = []
mystopwords = ['“this','“i', 'mr.', 'mrs.', 'cardenas']
stopwords = stopwords.__add__(mystopwords)

def text_data_cleaning(sentence):
    tokens = []
    for token in doc:
        if token.lemma_ != "-PRON-":
            temp = token.lemma_.lower().strip()
        else:
            temp = token.lower_
        tokens.append(temp)

    cleaned_tokens = []
    for token in tokens:
        if token not in stopwords and token not in punct:
            cleaned_tokens.append(token)
    return cleaned_tokens


cleaned_data = text_data_cleaning(text)

print(cleaned_data)
# with open("cleaned_data.txt", "w") as output_file:
#    for x in cleaned_data:
#        output_file.write(x)
