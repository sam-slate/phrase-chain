from phrases import *
from get_n_consecutive import *
from random import shuffle

p = Phrases()

def print_starting_messages():
	print 'Hello! In this game, you must reorder a bunch of words into a list of two word phrases.' 
	return int(raw_input('How long would you like your chain to be? '))


def start_game(n):
	global p
	# get the chain
	chain = get_random_n_consecutive(p, n)

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

	# call user plays
	user_plays(chain)

def user_plays(chain):
	# check to see if the chain is empty
	if not chain:
		# print out congrats
		print "Congratulations, you got the whole chain!"
	else:
		#set up boolean for got it
		got_it = False
		# loop until got it
		while (not got_it):
			# get the next word
			word = raw_input("Next word: ")
			# check if it matches the second word of the first
			# phrase in the chain list
			if word == chain[0][1]:
				# set the boolean to true and print out statement
				got_it = True
				print "Got it!"
				# recursively call the rest of the chain
				user_plays(chain[1:])
			else: 
				# tell the user that's not it
				print "Nope"



# the main function
if __name__ == "__main__":

	# read in from json
	p.read_in_json(storage_file)

	# print starting message and get n
	n = print_starting_messages()

	# call start game with n
	start_game(n)

	# # read in from json
	# p.read_in_json(storage_file)

	# chain = recurse_get_random_n_consecutive(p, 4, ("back", "up"))
	# print chain
	# chain = get_random_n_consecutive(p, 10)
	# print chain

