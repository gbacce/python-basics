# # print "Hello, world!"
# # Print two different things on the same line.
# print ("Hello world!", "Again")

# # This won't work!!
# # print "This
# # is a couple
# # lines of a sentence.
# # Please print.

# # This will...
# print """This
# will ignore the new lines
# until it sees another
# three double quotes"""


# # Variables = string, number, letters, any other stuff that you can make with a keyboard 
# # and you want to stash something that's not fast into something that is fast.
# # There is no declaration. 
# # In JS... var name = "variable";
# # name = "name"
# # Python is not heavily typed (for instance C#)
# first_name = "Guido";
# last_name = "Bacce";
# full_name = first_name + " " + last_name
# print full_name

# # Arithmetic
# the_meaning_of_life = 40 + 2
# # print the_meaning_of_life
# print the_meaning_of_life / 2
# print the_meaning_of_life % 5
# # returns 8 because  both are ints
# # print the_meaning_of_life / 5
# print int(30.5 / 5.2)

# print 4 + "joe"
# print 4 * "Joe"

# Data types (variable types)
# - Strings - English type stuff for people (in yellow)
# - Numbers - something with digits and stuff that goes with digits (. -)
# --- Floats, Integers
# - Booleans - True or False. 1 or 0. Yes or no. On or Off
# - Lists - list of variables in one variable
# - Dictionary - variables of variables (equivalent of JS object)
# - Objects - deal with it later

# Strings
# first_name = "Guido"
# last_name = "Bacce"
# print "Hello, {} {}".format(first_name, last_name)
# # print "Hello " + first_name + " " + last_name
# # Placeholders
# print "Hello, %s %s" % (first_name, last_name)
# print "Hello, %s %s for the %drd time!" % (first_name, last_name, 3)

# Floats
# pi_the_magic_float = 3.14
# print pi_the_magic_float
# print type(pi_the_magic_float)
# make_me_an_integer = int(pi_the_magic_float)
# print make_me_an_integer
# print .2 + .1

# Booleans - true or false
# the_truth = True  (
# 	True is a keyword - has to be uppercase to be considered a Booleans
# print type(the_truth)
# the_lie = False
# print type(the_lie)

# Raw Input
first_name = raw_input("First Name: ")
last_name = raw_input("Last Name: ")
# print first_name

# Conditionals
# 1 = (one equal sign) means you want to assign something
# 2 = (two equal signs) means you want to compare the left and right values

if (first_name == last_name): 
	print "Your first name is the same as your last name?"

# if you want to compare greater than or equal to, use >=
age = raw_input("How old are you? ")
print type(age)
	# The raw input, even if it is a number, will always be a string. So it needs to be manually converted to an integer for this comparison.
age_as_int = int(age)
if (age_as_int >= 21):
	print "Cheers."

