from __future__ import division 
import random 

def weighted_draw_from_dict(prob_dict):
    # Utility function -- do not modify
    # Randomly choose a key from a dict, where the values are the relative probability weights.
    # http://stackoverflow.com/a/3679747/86684
    choice_items = prob_dict.items()
    total = sum(w for c, w in choice_items)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choice_items:
       if upto + w > r:
          return c
       upto += w
    assert False, "Shouldn't get here"


## ---------------------- write your answers below here -------------------
#I added an import line above so i can divide naturally

def draw_next_word_unigram_model(uni_counts):
    total_ct = 0 #total num. wordz
    probability_dict = {}
    
    for xx in uni_counts:
        #populates prob dict, gets total words for later
        total_ct += uni_counts.get(xx, 0)
        probability_dict[xx] = uni_counts.get(xx, 0)
        
    #apply division of total to every value
    probability_dict = {key: value/total_ct for key,value in probability_dict.items()}
        
    # return dict using weight_draw..
    return weighted_draw_from_dict(probability_dict)

def draw_next_word_bigram_model(uni_counts, bi_counts, prev_word):
    condition_probability_dict = {}
    divisor = 0

    for yy in bi_counts:
        divisor = uni_counts.get(yy, 0)
        condition_probability_dict[yy] = bi_counts.get(yy, 0)
        condition_probability_dict[yy] = {key: value/divisor for key,value in condition_probability_dict[yy].items()}
    return weighted_draw_from_dict(condition_probability_dict[prev_word])

def sample_sentence(uni_counts, bi_counts):
    tokens = ['**START**'] 
    #use draw_next_word_bigram_model() to populate tokens using the model
    while tokens[-1] != '**END**':
        tokens.append(draw_next_word_bigram_model(uni_counts, bi_counts, tokens[-1]))

    return tokens

