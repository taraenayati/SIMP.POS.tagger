# -*- coding: utf-8 -*-
"""pos_detector

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eY7Zw4BFEjgHeYgwogrdrwtRnv3Qm3z6
"""

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Mapping of NLTK POS tags to the simplified tags
POS_MAPPING = {
    'NN': 'N', 'NNS': 'N', 'NNP': 'N', 'NNPS': 'N',         # Nouns
    'VB': 'V', 'VBD': 'V', 'VBG': 'V', 'VBN': 'V', 'VBP': 'V', 'VBZ': 'V',  # Verbs
    'IN': 'P',                                               # Prepositions
    'JJ': 'ADJ', 'JJR': 'ADJ', 'JJS': 'ADJ',                 # Adjectives
    'RB': 'ADV', 'RBR': 'ADV', 'RBS': 'ADV',                 # Adverbs
    'CC': 'CONJ',                                            # Conjunctions
    'DT': 'D',                                               # Determiners
    'IN': 'C'                                                # Complementizers
}

def pos_tagger(sentence):
    """
    Takes an English sentence as input and returns each word with a simplified POS tag.

    Args:
        sentence: The input sentence (string).

    Returns:
        A list of tuples, where each tuple contains a word and its simplified POS tag.
    """
    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)

    # Convert NLTK POS tags to simplified tags
    simplified_tags = [(word, POS_MAPPING.get(tag, 'OTHER')) for word, tag in pos_tags]
    return simplified_tags

# Example usage
sentence = input("Write down your sentence: ")
tagged_sentence = pos_tagger(sentence)
tagged_sentence

"""pronouns / preposition /"""