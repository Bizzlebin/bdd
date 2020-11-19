# Get Int
# 
# get_int.py
# 
# ***
# 
# By Jeremiah Thomas
# 
# ***
# 
# Created 2020-08-19
# 
# Updated 2020-08-24
# 
# +++
# Description
# 
# A small module to simplify the process of obtaining a valid integer from the user; with basic error checking/handling.
# 

# 
# +++
# Functions
# 
# ===
# Get Int
# 
def get_int(prompt, min = float('-inf'), max = float('inf'), error = 'That is not a valid number!', escape = None):
	'''
	Get a valid integer from the user.

	This function repeatedly asks the user for an integer using an arbitrary prompt, passed as an argument. The minimum and maximum valid numbers, inclusive, are fully tunable. All non-integers raise exceptions, as do invalid numbers; the function and error-handling are completely self-contained and the error message can be customized.

	**prompt**: str (complete on-screen prompt for the user)
	**min**: float = float('-inf') (minimum valid value for number)
	**max**: float = float('inf') (maximum valid value for number)
	**error**: str = 'That is not a valid number!' (on-screen warning for the user when number is invalid)
	**escape**: str = None (escape key/word/sequence for exiting the loop)

	Return number: int (validated integer)
	'''
	'''
	Verifying user input is incredibly common in programs, so this is a function I have used, in one form or another, since CSC 121 in 2H 2019; this particular, streamlined implementation—with parameters to make it more customizable—is a derivation of get_float.py, which was originally created for CSC 256 earlier the same day.
	'''
	while True:
		string = input(prompt)
		if string == escape:
			return escape
		try:
			number = int(string)
			if number < min:
				raise ValueError
			if number > max:
				raise ValueError
			return number
		except ValueError:
			print(error)