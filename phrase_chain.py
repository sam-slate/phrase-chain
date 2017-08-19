from phrases import *

#the name of the file where the dictionary is stored
storage_file = "dict.json"

#the instance of the phrases class used
p = Phrases()

#the number of passes in a row
num_passes = 0

#list of past phrases
past_phrases = []

def print_starting_messages():
	# starting messages
	print "Let's play phrase chain! We've got " + str(p.count_phrases()) + " phrases for you\n"
	print "The rules are very simple: "
	print "1) I give you a two word phrase"
	print "2) You come up with a new two word phrase that starts with my second word"
	print "3) We go back and forth with phrases, but we cannot repeat a phrase already used"
	print "4) We'll play until neither of us can come up with a new phrase!\n"

	print "Here's my first phrase:"

def start_game():
	#boolean to check if the start phrase is an error or not
	#set to true to get past the first round
	error_phrase = True

	#while loop for checking if the start phrase is real
	while(error_phrase):
		# get the starting phase
		start_phrase = p.random_start_phrase()
		# print the starting phrase
		print start_phrase[0] + " " + start_phrase[1] + "\t\t\t\t(if you think this phrase is wrong, please type \"error\")"
		# collect phrase from the user
		inp = raw_input('Type a phrase or pass (type "pass"): ')
		# check if it is not error
		if inp != "error" and inp != "Error":
			# set boolean to false
			error_phrase = False
			#add phrase to past_phrases
			past_phrases.append(start_phrase)
			#call phrase or pass on the input and the start_phrase
			phrase_or_pass(inp, start_phrase)
		# otherwise, if initial phrase was an error
		else:
			# delete the phrase
			p.delete_phrase(start_phrase)
			# print out message and loop back
			print "\nThanks for letting us know! We will delete it. Your new phrase is:"

def phrase_or_pass(inp, prev_phrase):
	# check if pass
	if inp == "pass" or inp == "Pass" or inp == "p" or inp == "P":
		#if so, call user passes
		user_passes(prev_phrase)
	else:
		phrase = (inp.split(" ")[0], inp.split(" ")[1])
		#call check_user_phrase
		check_user_phrase_match(phrase, prev_phrase)

def user_passes(prev_phrase):
	# set num_passes as global
	global num_passes
	# check how many passes there are
	if num_passes == 1:
		# if there has already been one pass, end game
		end_game(prev_phrase)
	else:
		# set num_passes equal to 1
		num_passes = 1
		# call user goes
		computer_goes(prev_phrase)

def check_user_phrase_match(phrase, prev_phrase):
	# check if second word in prev_phrase is a word or derivative
	# of first word in phrase
	if prev_phrase[1] == phrase[0] or p.check_if_derivative(phrase[0], prev_phrase[1]):
		# if so, check if user phrase is valid
		check_user_phrase_valid(phrase, prev_phrase)
	else:
		ask_if_derivative(phrase, prev_phrase)

def ask_if_derivative(phrase, prev_phrase):
	#print message saying it's not derivative
	print "Hmm, I don't have " + prev_phrase[1] + " and " + phrase[0] + " as derivatives of each other . . ."
	# ask if it was a derivative
	inp = raw_input('Is it really a derivative? (y/n): ')
	# check how they answered
	if inp == "y" or inp == "yes" or inp == "Y" or inp == "Yes":
		#call function for it was derivative
		it_was_a_derivative(phrase, prev_phrase)
	else:
		it_was_not_a_derivative(phrase, prev_phrase)

def it_was_a_derivative(phrase, prev_phrase):
	# add derivative
	p.add_derivatives(prev_phrase[1], [phrase[0]])
	# print message
	print "Thanks for letting me know!"
	# now check for validity
	check_user_phrase_valid(phrase, prev_phrase)

def it_was_not_a_derivative(phrase, prev_phrase):
	# print supportive message
	print "Alright, try again!"
	# call user goes with prev_phrase since we still have not moved on yet
	user_goes(prev_phrase)

def check_user_phrase_valid(phrase, prev_phrase):
	# set num_passes as global
	global num_passes
	#check if phrase is in the dictionary
	if p.check_phrase(phrase):
		#reset number of passes
		num_passes = 0
		#add phrase to past_phrases
		past_phrases.append(phrase)
		#call computer goes with phrase
		computer_goes(phrase)
	else:
		#otherwise, call not_valid
		not_valid(phrase, prev_phrase)

def not_valid(phrase, prev_phrase):
	#let them know it's not valid and ask if it was really a phrase
	print "Hmm, I don't have the phrase yet . . ."
	inp = raw_input('Is it really a phrase? (y/n): ')
	# check how they answered
	if inp == "y" or inp == "yes" or inp == "Y" or inp == "Yes":
		#call function for it was valid
		it_really_was_valid(phrase, prev_phrase)
	else:
		it_really_wasnt_valid(phrase, prev_phrase)

def it_really_was_valid(phrase, prev_phrase):
	# set num_passes as global
	global num_passes
	#add the phrase to the dictionary
	p.add_phrase(phrase)
	# print thanks
	print "Thanks for letting me know!"
	#reset number of passes
	num_passes = 0
	#add phrase to past_phrases
	past_phrases.append(phrase)
	# now the computers turn to go, passing just phrase now
	computer_goes(phrase)

def it_really_wasnt_valid(phrase, prev_phrase):
	# print supportive message
	print "Alright, try again!"
	# call user goes with prev_phrase since we still have not moved on yet
	user_goes(prev_phrase)

def user_goes(phrase):
	# get input from the user
	inp = raw_input('Type a phrase or pass (type "pass"): ')
	#call phrase or pass on the input and the phrase
	phrase_or_pass(inp, phrase)

def computer_goes(phrase):
	# get random next phrase from the dictionary
	next_phrase = p.random_next_phrase(phrase)
	# check if next_phrase is none
	if next_phrase is None:
		# computer pass
		computer_pass(phrase)
	else:
		# otherwise, computer can go, pass in phrase it can use
		computer_can_go(next_phrase, phrase)

def computer_pass(phrase):
	# set num_passes as global
	global num_passes
	# check how many passes there are
	if num_passes == 1:
		# print message
		print "I can't go either!"
		# if there has already been one pass, end game
		end_game(phrase)
	else:
		# alert user computer can't go
		print "I can't go, I pass!"
		# set num_passes equal to 1
		num_passes = 1
		# call user goes
		user_goes(phrase)

def computer_can_go(phrase, prev_phrase):
	# print computer phrase with caveat
	print phrase[0] + " " + phrase[1] + "\t\t\t\t(type \"derror\" for derivative error and \"perror\" for phr	ase error)"

	# get input
	inp = raw_input('Type a phrase or pass (type "pass"): ')

	# check for derivative error
	if inp == "derror" or inp == "Derror":
		#if so, call computer_derivative_error
		computer_derivative_error(phrase, prev_phrase)
	# check for phrase error
	elif inp == "perror" or inp == "Perror":
		# call function for computer_phrase_error
		computer_phrase_error(phrase, prev_phrase)
	# otherwise no error
	else:
		#add phrase to past_phrases
		past_phrases.append(phrase)
		#call phrase or pass on the input and the phrase
		phrase_or_pass(inp, phrase)
		# otherwise, if initial phrase was an error

def computer_derivative_error(phrase, prev_phrase):
	# delete the derivative
	p.delete_derivative(prev_phrase[1], phrase[0])

	# print out message
	print "Thanks for letting me know! I will delete it."

	#call computer goes on the same phrase
	computer_goes(prev_phrase)


def computer_phrase_error(phrase, prev_phrase):
	# delete the phrase
	p.delete_phrase(phrase)

	# print out message
	print "Thanks for letting me know! I will delete it."

	#call computer goes on the same phrase
	computer_goes(prev_phrase)

def print_past_phrases():
	# loop through past_phrases
	for i, p in enumerate(past_phrases):
		#print it out
		print str(i + 1) + ": " + p[0] + " " + p[1]

def end_game(phrase):
	#sets past_phrases to global
	global past_phrases
	# print all of the phrases
	print_past_phrases()
	# erase past phrases
	past_phrases = []

	# print game over messages
	print "Game over, both of us failed!"
	print "The word that stumped us was: " + phrase[0] + " " + phrase[1] 

	# ask if they want to play again
	inp = raw_input('Want to play again? I\'ve learned from last time (y/n): ')

	# check how they answered
	if inp == "y" or inp == "yes" or inp == "Y" or inp == "Yes":
		# if yes, start agme again
		start_game()
	else:
		# shut down!
		shut_down()

def shut_down():
	p.print_json(storage_file)
	print "Thanks so much for saving! Your additions have been saved in " + storage_file


# the main function
if __name__ == "__main__":

	# read in from json
	p.read_in_json(storage_file)


	print_starting_messages()

	start_game()



