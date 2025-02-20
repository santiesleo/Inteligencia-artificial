from pyformlang.fst import FST
import re

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from FST.FstSynonyms import *
from FST.FstAntonyms import *
from FST.FstPronouns import *
from FST.FstPastTenses import *
from FST.FstFutureTenses import *
from FST.FstPresentTenses import *


#--------------Sinonimos-------------------
fst=transformate_synonyms()


#---------------Antonimos------------------
fstAntonyms=transformate_antonyms()

#--------------Tiempos verbales-------------------


#past simple
fstPastSimple=create_fst_present_to_past_simple()


#present continuous
fstPresentContinuous=create_fst_present_to_continuous()


#simple future


fstFutureSimple=create_fst_present_to_future_simple()

#--------------Cambiar pronombres (subject pronouns)-------------------


fst_i=create_fst_pronouns_to_i()
fst_you=create_fst_pronouns_to_you()
fst_he=create_fst_pronouns_to_he()
fst_she=create_fst_pronouns_to_she()
fst_it=create_fst_pronouns_to_it()
fst_we=create_fst_pronouns_to_we()
fst_they=create_fst_pronouns_to_they()


#---------------------------------


#--------------Funciones para procesar texto con FST-------------------


def split_into_sentences(text):
    return re.split(r'(?<=[.!?]) +', text)

def apply_fst_to_sentence(fst, sentence):
    words = sentence.split()
    transformed_words = []

    for word in words:
        normalized_word = word.lower()
        
        translated = list(fst.translate([normalized_word]))

        if translated:
            transformed_word = translated[0][0]
            transformed_words.append(transformed_word)  # No capitalizar aquí
        else:
            transformed_words.append(word)

    # Capitalizar solo la primera palabra de la oración
    if transformed_words:
        transformed_words[0] = transformed_words[0].capitalize()

    return " ".join(transformed_words)

def process_text_with_fst(fst, text):
    sentences = split_into_sentences(text)
    transformed_sentences = []

    for sentence in sentences:
        transformed_sentence = apply_fst_to_sentence(fst, sentence)
        transformed_sentences.append(transformed_sentence)

    return " ".join(transformed_sentences)