string = "this is a string"

# print string

# upper_string = string.upper()
# print upper_string

# cap_string = string[:1].upper() + string[1:]
# print cap_string

# # This actually slices the string, going through all of it by steps of -1. Slicing syntax is [start:end:step]
# reverse_string = string[::-1]
# print reverse_string


# print string.split()

character = list(string)


for i in range(0,len(character)):
	if character[i] == "a":
		character.remove("a")
		character.insert(i, "4")
	if character[i] == "e":
		character.remove("e")
		character.insert(i, "3")
	if character[i] == "g":
		character.remove("g")
		character.insert(i, "6")
	if character[i] == "i":
		character.remove("i")
		character.insert(i, "1")
	if character[i] == "o":
		character.remove("o")
		character.insert(i, "0")
	if character[i] == "s":
		character.remove("s")
		character.insert(i, "5")
	if character[i] == "t":
		character.remove("t")
		character.insert(i, "7")



print string



