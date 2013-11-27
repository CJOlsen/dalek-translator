## Dalek Translator: words.py
## Author: Christopher Olsen
##
## This file is where incoming words are translated into Dalek-y words.


# this tries to download the wordnet and if it's already current it just returns
import nltk
try:
    nltk.download('wordnet')
except:
    pass

from nltk.corpus import wordnet as wn

def _get_all_ate_verbs():
    """ Walks through all of the verb synsets and keeps those whose name ends
        with the characters 'ate'.  Returns the list of 'ate' verbs.  There are
        currently 1080 of them.

        """
    ate_verbs = []
    for synset in list(wn.all_synsets('v')):
        s_name = synset.name.split('.')[0]
        if s_name[-3:] == "ate":
            ate_verbs.append(synset)
    return ate_verbs

_ate_verbs = _get_all_ate_verbs()

def _to_synset(word):
    return wn.synset(str(word+'.v.01'))


def _find_most_similar_lch(word):
    """ Takes a word and searches for the most similar of the 'ate' verbs using
        lch_similarity as a measure.
    
        """
    try:
        ## this fails if word isn't a verb, or is a sentence, or is misspelled, etc.
        search_word = _to_synset(word)
    except:
        return False
        
    ## Check 'exterminate!' first, if it's close enough use it
    if search_word.lch_similarity(_to_synset('exterminate')) > 1.8:
        return "exterminate"

    best_word = None
    best_score = 0
    for current_word in _ate_verbs:
        current_score = search_word.lch_similarity(current_word)
        if current_score > best_score:
            best_word = current_word
            best_score = current_score
    return best_word.name.split('.')[0]
            
def dalekify(word):
    """ Takes a verb, returns the most similar of the verbs ending in '-ate' """
    best = _find_most_similar_lch(word)
    if best:
        return best.upper() + "!!!"
    else:
        return "A Dalek would never say that (hint: this only works for verbs and some short phrases like 'knock over')"
