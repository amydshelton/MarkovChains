#!/usr/bin/env python

import sys 
import random



def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    words = corpus.split()
    chains_dict = {}

    for i in range(len(words)-2):
        key = (words[i], words[i + 1])
        value = words[i+2]
        
        if key in chains_dict:
            chains_dict[key].append(value)
        else:
            chains_dict[key] = [value]

    return chains_dict

def make_text(chains_dictionary):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    

    random_key = random.choice(chains_dictionary.keys())
    seed_key = random_key
    output_string = seed_key[0] + ' ' + seed_key[1]
    
    #while seed_key in chains_dictionary:
    for i in range(60):   
        options = chains_dictionary[seed_key]
        chosen_one = random.choice(options)
        output_string = output_string + ' ' + chosen_one
        seed_key = (seed_key[1], chosen_one)

    return output_string

def main():
    
    #script, filename = argv
    args = sys.argv

    combined_text = ""
    #chain_dict = {}
    for arg in args[1:]:
        raw_text = open(arg)
        text = raw_text.read().lower().strip()
        combined_text = combined_text + ' ' + text


    chain_dict = make_chains(combined_text)
    print(make_text(chain_dict))

if __name__ == "__main__":
    main()