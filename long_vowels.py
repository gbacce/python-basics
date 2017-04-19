string = raw_input("Word: ")

word = list(string)

for i in range(0,len(word)-1):
	home_slice = word[i:i+2]
	if home_slice == ['a', 'a']:
		word.remove("a")
		word.insert(i, "aaaa")
	if home_slice == ['e', 'e']:
		word.remove("e")
		word.insert(i, "eeee")
	if home_slice == ['i', 'i']:
		word.remove("i")
		word.insert(i, "iiii")
	if home_slice == ['o', 'o']:
		word.remove("o")
		word.insert(i, "oooo")
	if home_slice == ['u', 'u']:
		word.remove("u")
		word.insert(i, "uuuu")

woooord = "".join(word)

print woooord
