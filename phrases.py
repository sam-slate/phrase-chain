import random
import json


#define the phrases class

class Phrases:

	# define the phrases dictionary with the form:
	# {word : {"derivatives" : set(word1, word2, ...), "matches" : set(word1, word2, ...)}}
	phrases_dict = {}

	# initializer
	def __init__(self):
		return

	def count_phrases(self):
		return len(self.all_phrases())

	# read in phrases_dict from a json file
	def read_in_json(self, file):
		# read in from a file
		output_json = json.load(open(file))
		# set phrases_dict equal to output_json
		self.phrases_dict = output_json
		# loop through and turn all of the lists into sets
		for word, info in self.phrases_dict.items():
			info["derivatives"] = set(info["derivatives"])
			info["matches"] = set(info["matches"])

	# add phrases from a file
	def add_from_file(self, file):
		# get phrases from file
		with open(file, 'r') as f:
			phrases = [line[:-1].split('\t') for line in f]

		#loop through phrases
		for phrase in phrases:
			# make lowercase the phrase
			phrase[0] = phrase[0].lower()
			phrase[1] = phrase[1].lower()
			#add phrase
			self.add_phrase(phrase)

	# adds word to the dictionary if it doesn't already exist
	def add_word (self, word):
		# check if word is in phrases_dict
		if word not in self.phrases_dict:
			# if not, add new dictionary as the value to word
			self.phrases_dict[word] = {"derivatives" : set(), "matches" : set()}

	# adds a phrase to phrases_dict
	def add_phrase (self, phrase):
		#unpacks the phrase
		word1 = phrase[0]
		word2 = phrase[1]
		#adds word1 as a key to the dictionary if not already there
		self.add_word(word1)
		#adds word2 to the list of matches for word1
		self.phrases_dict[word1]["matches"].add(word2)
		#adds word2 as a key to the dictionary if not already there
		self.add_word(word2)

	# adds a list of phrases to phrases_dict
	def add_phrases (self, phrases):
		# loop through phrases
		for phrase in phrases:
			# call add_phrase
			self.add_phrase(phrase)

	# check to see if a phrase is in phrase_dict
	def check_phrase(self, phrase):
		#unpacks the phrase
		word1 = phrase[0]
		word2 = phrase[1]
		# check if word1 is in phrases_dict
		if word1 not in self.phrases_dict:
			return False
		else:
			# check if word2 is in the matches list of word1
			return word2 in self.phrases_dict[word1]["matches"]

	# check if a word is a derivative of another word
	def check_if_derivative(self, word, derivative):
		# check if word is in phrases_dict:
		if word not in self.phrases_dict:
			#if not, return false
			return False
		else:
			return derivative in self.phrases_dict[word]["derivatives"]

	# add derivatives to a word
	def add_derivatives(self, word, derivatives):
		# add the word to phrases_dict just in case
		self.add_word(word)
		# add the derivatives to phrases_dict
		self.phrases_dict[word]["derivatives"].update(set(derivatives))
		# loop through the derivatives
		for d in self.phrases_dict[word]["derivatives"]:
			# add the derivative to phrases_dict just in case
			self.add_word(d)
			# to the derivatives set for d, add all the derivatives as well
			# as word except for d as well as word
			temp_set = self.phrases_dict[d]["derivatives"]
			temp_set.update(self.phrases_dict[word]["derivatives"])
			temp_set.discard(d)
			temp_set.add(word)

	# given a phrase, returns a list of all possible next phrases
	def all_possible_phrases(self, phrase):
		#unpack the phrase
		word1 = phrase[0]
		word2 = phrase[1]

		# check to see if word2 is in the dictionary
		if word2 not in self.phrases_dict:
			# then return empty list
			return []

		#initialize all_possible_phrases
		all_possible_phrases = []

		#get the set of all starting words
		all_starting_words = self.phrases_dict[word2]["derivatives"]
		all_starting_words.add(word2)

		#loop through all the starting words
		for word in list(all_starting_words):
			#loop through the matches for that word
			for match in self.phrases_dict[word]["matches"]:
				# add to all_possible_phrases the phrase
				all_possible_phrases.append((word, match))

		return all_possible_phrases

	# given a phrase, returns a list of all possible next phrases
	# excluding the use of derivatives
	def all_possible_phrases_no_derivatives(self, phrase):
		#unpack the phrase
		word1 = phrase[0]
		word2 = phrase[1]

		# check to see if word2 is in the dictionary
		if word2 not in self.phrases_dict:
			# then return empty list
			return []

		#initialize all_possible_phrases
		all_possible_phrases = []

		# loop through all the matches
		for match in self.phrases_dict[word2]["matches"]:
			# add to all_possible_phrases the phrase
			all_possible_phrases.append((word2, match))

		return all_possible_phrases

	# returns a list of all possible phrases
	def all_phrases(self):
		#initialize all_possible_phrases
		all_phrases = []
		# loop through all words
		for word, info in self.phrases_dict.items():
			# loop through all the matches
			for match in info["matches"]:
				# add to all_possible_phrases the phrase
				all_phrases.append((word, match))

		return all_phrases

	# return a random phrase from all_possible_phrases
	def random_next_phrase(self, phrase):

		# get all possible phrases
		all_possible_phrases = self.all_possible_phrases(phrase)
		# if no phrases
		if not all_possible_phrases:
			return None
		else:
			# use random choice to randomly choose from all_possible_phrases
			return random.choice(all_possible_phrases)

	# return a random phrase from the whole dictionary
	def random_start_phrase(self):
		# use random choice to randomly choose from all_possible_phrases
		return random.choice(self.all_phrases())

	# delete a phrase
	def delete_phrase(self, phrase):
		#unpack the phrase
		word1 = phrase[0]
		word2 = phrase[1]
		# check if phrase is in the dictionary
		if self.check_phrase(phrase):
			# if so, remove the phrase
			self.phrases_dict[word1]["matches"].discard(word2)

	# delete a derivative
	def delete_derivative(self, word, derivative):
		# check if word is in the dictionary
		if word in self.phrases_dict:
			# remove the derivative
			self.phrases_dict[word]["derivatives"].discard(derivative)

		# do the same but for the opposite
		# check if derivative is in the dictionary
		if derivative in self.phrases_dict:
			# remove the derivative
			self.phrases_dict[derivative]["derivatives"].discard(word)

	# print to output the json of the dictionary
	def print_json(self, file):
		# store phrases_dict in a temporary dictionary
		temp_dict = dict(self.phrases_dict)

		# convert all of the sets to lists in temp_dict
		for word, info in temp_dict.items():
			info["derivatives"] = list(info["derivatives"])
			info["matches"] = list(info["matches"])

		string = json.dumps(temp_dict)
		parsed = json.loads(string)
		# print to file
		with open(file, "w") as f:
			print >> f, json.dumps(parsed, indent=4, sort_keys=True)

	# recursive function that takes in a phrases dictionary, n, and the previous phrase
	def recurse_get_random_n_consecutive(self, n, prev_phrase):
		# base case when n = 0
		if n == 0:
			return []

		else:
			# get all possible phrases
			all_possible_phrases = self.all_possible_phrases_no_derivatives(prev_phrase)
			
			# randomly shuffle all_posisble_phrases to provide random chain
			random.shuffle(all_possible_phrases)

			# check if there are any possible phrases
			if len(all_possible_phrases) > 0:
				# if so, loop through them
				for phrase in all_possible_phrases:
					# recursively call recurse_get_n_consecutive with the same p,
					# n-1, and phrase as the prev_phrase
					recurse_call = self.recurse_get_random_n_consecutive(n-1, phrase)
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
	def get_random_n_consecutive(self, n):
		# get all phrases
		all_phrases = self.all_phrases()

		#randomly shuffle all_phrases to provide random chain
		random.shuffle(all_phrases)

		# loop through all_phrases
		for phrase in all_phrases:
			# call the recursive function on the phrase
			chain = self.recurse_get_random_n_consecutive(n, phrase)
			# check if chain is not None
			if chain is not None:
				# if so, we've got it! return chain
				return chain
				# if not, keep going

		# if we've reached here, no such chain exists, return None
		return None


	def test_print(self):
		for word, info in self.phrases_dict.items():
			print word
			print "Derivatives: " + ", ".join(info["derivatives"])
			print "Matches: " + ", ".join(info["matches"]) + "\n"


