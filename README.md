# Phrase Chain

This repository is for playing around with chains of two word phrases. There are a couple different games and puzzles built on top of a library of two word phrases.

## Files

### dict.json:
A json file containing a dictionary of two word phrases. Associated with a word is a tuple that contains:
1. A set of derivatives associated with that word (derivatives defined below)
2. A set of words that are "matches" for that word and make up a valid two word phrase when placed after the word (criteria for valid two word phrase defined below).

The type for the dictionary is: `{"word" : {"derivatives" : set(derivative1, derivative2, ...), "matches" : set(match1, match2, ...)}}`

Some invariants for the dictionary:
* Every word that is listed as a derivative or as a match for another word has its own entry
* A word does not list itself as a derivative
* Words that are derivatives of each other share all the same derivatives (except for themselves)


### phrases.py:
Defines the Phrases class which provides an interface to interact with a phrases dictionary


## Definitions
