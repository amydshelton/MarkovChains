#!/usr/bin/env python

#import sys, string
import random
seuss = open("green_eggs.txt")
seuss_read = seuss.read().lower().strip()
#print seuss_read

#chains_dict[key] = chains_dict.get(key, value)

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
   # print chains_dict
    return chains_dict

def make_text(chains_dictionary):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
  #  print chains_dictionary.keys()
    random_key = random.choice(chains_dictionary.keys())
    print random_key
    #return "Here's some random text."

def main():
 #   args = sys.argv

    # Change this to read input_text from a file
  #  input_text = "Some text"

    chain_dict = make_chains(seuss_read)
    make_text(chain_dict)
    # print random_text

if __name__ == "__main__":
    main()