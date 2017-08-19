import enchant
from phrases import *
d = enchant.Dict("en_US")

p = Phrases()

storage_file = "dict.json"


suffixes = [
	"s",
	"ed",
	"ing",
	"er",
	"est",
	"ment",
	"tion",
	"ness",
	"en",
	"es",
	"y",
	"ly",
	"or",
	"ion",
	"ation",
	"ition",
	"ible",
	"able",
	"al",
	"ity",
	"ty",
	"ic",
	"ous",
	"eous",
	"ious",
	"ive",
	"ative",
	"itive",
	"ful",
	"less",
	"est"
] 

p.read_in_json(storage_file)


for word, info in p.phrases_dict.items():
	pos_d = []
	for s in suffixes:
		pos_d.append(word + s)

	pos_d2 = [word[:-len(s)] for s in suffixes if word[-len(s):] == s]
	pos_d2 = [w for w in pos_d2 if len(w) > 3]

	ders = [w for w in pos_d if d.check(w)] + [w for w in pos_d2 if d.check(w)] 
	p.add_derivatives(word, ders)

p.print_json(storage_file)