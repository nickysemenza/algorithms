#prints all the characters in a string that appear more than once
inp = "hello"
occurances = {}
for c in inp:
	if occurances.get(c) is None:
		occurances[c] = 1
	else:
		occurances[c] = occurances[c]+1
print "duplicate characters: "
for each in occurances:
	if occurances.get(each) > 1:
		print each