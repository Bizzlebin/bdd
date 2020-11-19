# Full Retirement Age 02
# 
# full_retirement_age.py
# 
# ***
# 
# By Jeremiah Thomas
# 
# ***
# 
# Created 2020-08-19
# 
# Updated 2020-11-18
# 
# +++
# Dedication
# 
# CSC 256-0001
# 
# +++
# Description
# 
# A small program to calculate a retirement age and date based upon input birth year and month; with basic error checking/handling; updated for modularization so pytest works successfully.
# 

# 
# +++
# Imports
# 
from get_int import get_int
from sys import exit
# 
# +++
# Variables
# 
min_year = 1900
max_year = 2020
months = \
	{
	1: 'January',
	2: 'February',
	3: 'March',
	4: 'April',
	5: 'May',
	6: 'June',
	7: 'July',
	8: 'August',
	9: 'September',
	10: 'October',
	11: 'November',
	12: 'December',
	}
full_retirement_ages = \
	{
	1937: (65, 0),
	1938: (65, 2),
	1939: (65, 4),
	1940: (65, 6),
	1941: (65, 8),
	1942: (65, 10),
	1954: (66, 0),
	1955: (66, 2),
	1956: (66, 4),
	1957: (66, 6),
	1958: (66, 8),
	1959: (66, 10),
	float('inf'): (67, 0),
	}
# 
# +++
# Functions
# 
def read_exit(buffer):

	if buffer:
		return buffer
	else:
		exit() # Defaults to 0

def create_full_retirement_age(birth_year, full_retirement_ages):

	for age in full_retirement_ages:
		if birth_year <= age:
			return full_retirement_ages[age]

def create_retirement_date(birth_year, birth_month, full_retirement_age):

	retirement_year = birth_year + full_retirement_age[0]
	retirement_month = birth_month + full_retirement_age[1]
	if retirement_month > 12:
		retirement_year += 1
		retirement_month -= 12
	return (retirement_year, retirement_month)
# 
# +++
# Output
# 
if __name__ == '__main__':
	print('Welcome to the Full Retirement Age calculator!')
	print('Press Enter on any line—before entering information—to exit.')
	while True:
		print()
		birth_year = read_exit(get_int('Enter birth year (YYYY): ', min = min_year, max = max_year, error = f'That is not a valid year from {min_year} to {max_year}!', escape = ''))
		birth_month = read_exit(get_int('Enter birth month (MM): ', min = 1, max = 12, error = 'That is not a valid month from 01 to 12 !', escape = ''))
		full_retirement_age = create_full_retirement_age(birth_year, full_retirement_ages)
		print(f'Full retirement age is {full_retirement_age[0]} years and {full_retirement_age[1]} months.')
		retirement_date = create_retirement_date(birth_year, birth_month, full_retirement_age)
		print(f'This will occur in {months[retirement_date[1]]} of {retirement_date[0]} .')