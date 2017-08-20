from phrases import *
from random import shuffle
import time

#the name of the file where the dictionary is stored
storage_file = "dict.json"

p = Phrases()

def print_starting_messages():
	print 'Hello! In this game, you must reorder a bunch of words into a list of two word phrases.' 
	return int(raw_input('How long would you like your chain to be? '))


def start_game(n):
	global p
	# get the chain
	chain = p.get_random_n_consecutive(n)

	#copy the chain in order to shuffle it
	shuffled_chain = chain[:]

	# randomly shuffle the chain
	shuffle(shuffled_chain)

	# get the words to print out by taking the second word in each phrase
	print_out = [p[1] for p in shuffled_chain]

	# get the comma seperated string from print_out
	to_print = ', '.join(print_out)

	# Print out starting information
	print "Your words are: " + to_print
	print "And your first word is: " + chain[0][0]

	# Get the starting time
	start = time.time()

	# call user plays
	user_plays(chain, to_print)

	# get the ending time
	end = time.time()
	print("It took: " + str(end - start))

def user_plays(chain, to_print):
	# check to see if the chain is empty
	if not chain:
		# print out congrats
		print "Congratulations, you got the whole chain!"
	else:
		#set up boolean for got it
		got_it = False
		# loop until got it
		while (not got_it):
			# print words left
			print to_print
			# get the next word
			word = raw_input("Next phrase: " + chain[0][0] + " ")
			# check if it matches the second word of the first
			# phrase in the chain list
			if word == chain[0][1]:
				# set the boolean to true and print out statement
				got_it = True
				print "Got it!"

				#replace the word in to_print with its strike through version
				to_print = to_print.replace(word, strike(word))
				# recursively call the rest of the chain
				user_plays(chain[1:], to_print)
			else: 
				# tell the user that's not it
				print "Try again"


def strike(text):
    result = ''
    for c in text:
        result = result + "-"
    return result

# the main function
if __name__ == "__main__":

	# read in from json
	p.read_in_json(storage_file)

	# print starting message and get n
	n = print_starting_messages()

	# call start game with n
	start_game(n)

