# Phrase Chain

This repository is for playing around with chains of two word phrases. There are a couple different games and puzzles built on top of a dictionary of two word phrases.

## Set up and running

Download files into the same directory.

**phrase_chain.py**: Run using python

**guess_chain.py**: Run using python

**add_derivatives.py**: Run using python. Requires [pyenchant](http://pythonhosted.org/pyenchant/download.html) installed.

## Files

### [dict.json](https://github.com/sam-slate/phrase-chain/blob/master/dict.json):
A json file containing a dictionary of two word phrases. Associated with a word is a tuple that contains:
1. A list of derivatives associated with that word (derivatives defined below)
2. A list of words that are "matches" for that word and make up a valid two word phrase when placed after the word (criteria for valid two word phrase defined below)

The type for the dictionary is: `{word : {"derivatives" : [derivative1, derivative2, ...], "matches" : [match1, match2, ...]}}`

Some invariants for the dictionary:
* Every word that is listed as a derivative or as a match for another word has its own entry
* A word does not list itself as a derivative
* Words that are derivatives of each other share all the same derivatives (except for themselves)


### [phrases.py](https://github.com/sam-slate/phrase-chain/blob/master/phrases.py):
Defines the Phrases class which provides an interface to interact with a phrases dictionary. Reads in and writes to the dict.json file.

### [guess_chain.py](https://github.com/sam-slate/phrase-chain/blob/master/guess_chain.py):
Program that runs the guess chain game using the Phrases class. A user selects how long they want their chain to be and is then given a list of shuffled words. They must guess the correct order of the words one by one. 

### [phrase_chain.py](https://github.com/sam-slate/phrase-chain/blob/master/phrase_chain.py):
Program that runs a phrase chain game using the Phrases class. A user interacts with a computer from the command line to build a chain of two word phrases, using the second word in the previous phrase as the first word in the next. As of now, the rules are defined as such:
* The computer begins with a randomly selected two word phrase
* Each player must in turn come up with the next two word phrase using the second word in the previous phrase as the first word
* A player can pass and the next player then must come up with the phrase. When both the computer and the user pass, the round is over.

Important to this script is the user's ability to correct the computer's phrases and derivatives and to add their own to the computer's dictionary. At every step, the computer asks if its phrases and derivatives are correct and allows for the user to delete errors from its memory. Similarly, if the user uses a phrase or a derivative the computer does not understand, the computer will ask first if it should edit its memory to include the new information. In this way, the user is helping to build up the phrase dictionary while playing. 

### [add_derivatives.py](https://github.com/sam-slate/phrase-chain/blob/master/add_derivatives.py):

Script that adds derivatives to the phrase dictionary using a list of suffixes and a spell-checking library from [pyenchant](http://pythonhosted.org/pyenchant/).

## Definitions

**Two Word Phrases**

I've defined a two word phrase loosely as two seperately defined words that are often used together. I've included compound words that can be split into two (e.g. notebook, github), as well as hyphenated words (e.g. long-term). Grammatically speaking, I use the union of all open, closed, and hyphenated compound words.  

**Derivatives**

I've defined derivatives as words that are derived from other words, called root words. They are formed by adding an affix to the root words.
