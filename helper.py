# basic text modules
import re
import string

# nlp specific modules
from typing import List, Union
from nltk.tokenize import sent_tokenize
from spacy.lang.pl.stop_words import STOP_WORDS

# other modules
from IPython.core.display import display, HTML


vector = List[float] # make a list of floats

def dot(v: vector, w: vector) -> float:
    '''
    Multiply two vectors together

    Args:
        v: first vector
        w: second vector
    
    Returns:
        Sum of products of element from two vectors
    '''
    return sum([vi * wi for vi, wi in zip(v,w)])

def cos_sim(v: vector, w: vector) -> float:
    '''
    Calculate cosine similarity between two vectors
    
    Args:
        v: firsts vector
        w: second vector

    Returns:
        Cosine similarity of two vectors.
    '''
    return dot(v, w) / (dot(v,v) * dot(w,w)) ** .5


class Preprocessing(object):
    '''
    Text class used to produce preprocessed tokens. 
    '''
    def __init__(self, text):
        self.text = text
        self.oryg = text

    def lower(self):
        self.text = self.text.lower() 
        return self.text
    
    def remove_punctuation(self):
        self.text = self.text.translate(self.text.maketrans('', '', string.punctuation.replace('.', '')))
        return self.text 
    
    def remove_stop_words(self):
        self.text = ' '.join([word for word in self.text.split() if word not in STOP_WORDS])
        return self.text
    
    def remove_digits(self):
        self.text = re.sub(r'[\d+]', '', self.text)
        return self.text
    
    def sentence_tokenize(self):
        self.text = sent_tokenize(self.text)
        self.text = [sent.replace('.','') for sent in self.text]
        return self.text
    
    def basic_pipeline(self):
        self.lower()
        self.remove_digits()
        self.remove_punctuation()
        self.remove_stop_words()
        self.sentence_tokenize()
        return self.text

    def __call__(self):
        return self.text


def prepare_text(text: str)-> Union[list,list]:
    '''
    Change text into list of preprocessed sentences
    and another list with original sentences (no preprocesing)

    Args:
        text: text in a string format
    
    Returns:
        Two lists: first on with preprpcessed sentences, the second
        one with original sentences
    '''
    cleaned_text = Preprocessing(text) # make Preprocessing object
    sentences = cleaned_text.basic_pipeline() # clean and tokenize the text
    # only tokenize the sentences in the original text
    raw_sentences = Preprocessing(text).sentence_tokenize() 
    return sentences, raw_sentences


def display_highlights(raw_sentences: list, summarized_sents: list):
    '''
    Display the whole text as HTML, and highlight the most importand sentences.
    '''
    final = []
    for sent in raw_sentences: # for every sentence in raw input
        if sent not in summarized_sents: # if the sentence isn't in the summary
            final += sent # display it as normal
        else: # if the sentence is in the summary
            # make a yellow background arround it
            final += f'<span style="background-color:rgba(255,215,0,0.3);"> {sent} </span>'
    display(HTML(''.join([elem for elem in final])))