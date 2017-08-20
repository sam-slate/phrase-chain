from phrases import *
from random import shuffle

#the name of the file where the dictionary is stored
storage_file = "dict.json"

# recursive function that takes in a phrases dictionary, n, and the previous phrase
def recurse_get_random_n_consecutive(p, n, prev_phrase):
	# base case when n = 0
	if n == 0:
		return []

	else:
		# get all possible phrases
		all_possible_phrases = p.all_possible_phrases_no_derivatives(prev_phrase)
		
		# randomly shuffle all_posisble_phrases to provide random chain
		shuffle(all_possible_phrases)

		# check if there are any possible phrases
		if len(all_possible_phrases) > 0:
			# if so, loop through them
			for phrase in all_possible_phrases:
				# recursively call recurse_get_n_consecutive with the same p,
				# n-1, and phrase as the prev_phrase
				recurse_call = recurse_get_random_n_consecutive(p, n-1, phrase)
				# check if not none
				if recurse_call is not None:
					# if so, insert the current phrase as the first 
					# element in the list returned by recurse_call
					recurse_call.insert(0, phrase)
					return recurse_call
				# Otherwise, continue the loop

			#If the end of the for loop is reached, that means that there
			#are no next phrases that get to n, so return None
			return None

		# if not, return none
		else:
			return None

# function that takes in a number n and returns a random chain of
# n consecutive phrases
def get_random_n_consecutive(p, n):
	# get all phrases
	all_phrases = p.all_phrases()

	#randomly shuffle all_phrases to provide random chain
	shuffle(all_phrases)

	# loop through all_phrases
	for phrase in all_phrases:
		# call the recursive function on the phrase
		chain = recurse_get_random_n_consecutive(p, n, phrase)
		# check if chain is not None
		if chain is not None:
			# if so, we've got it! return chain
			return chain
			# if not, keep going

	# if we've reached here, no such chain exists, return None
	return None


