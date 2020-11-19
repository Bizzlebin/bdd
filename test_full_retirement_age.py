# Test Full Retirement Age 02
# 
# test_full_retirement_age.py
# 
# ***
# 
# By Jeremiah Thomas
# 
# ***
# 
# Created 2020-11-18
# 
# +++
# Dedication
# 
# CSC 256-0001
# 
# +++
# Description
# 
# A small program to test Full Retirement Age 02 using pytest-bdd.
# 

# 
# +++
# Imports
# 
import pytest
from pytest_bdd import scenario, given, when, then
from full_retirement_age import *
# 
# +++
# Assignments
# 
# ===
# Initializations
# 

# 
# ===
# Constants
# 

# 
# +++
# Functions
# 
# ===
# Definitions
# 
@scenario('full_retirement_age.feature', 'January Birth')
def test_january_birth():

	pass

@when('the year 2000 and the month 01 are entered')
def input_january_birth(monkeypatch):

	monkeypatch.setattr('builtins.input', lambda _: '2000') # https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
	assert read_exit(get_int('Enter birth year (YYYY): ', min = min_year, max = max_year, error = f'That is not a valid year from {min_year} to {max_year}!', escape = '')) == 2000

	monkeypatch.setattr('builtins.input', lambda _: '01')
	assert read_exit(get_int('Enter birth month (MM): ', min = 1, max = 12, error = 'That is not a valid month from 01 to 12 !', escape = '')) == 1

@then('the full retirement age of 67 years and 0 months and date January 2067 are shown')
def january_birth():

	full_retirement_age = create_full_retirement_age(2000, full_retirement_ages)
	assert full_retirement_age[0] == 67
	assert full_retirement_age[1] == 0

	retirement_date = create_retirement_date(2000, 1, full_retirement_age)
	assert months[retirement_date[1]] == 'January'
	assert retirement_date[0] == 2067

@scenario('full_retirement_age.feature', 'December Birth')
def test_december_birth():

	pass

@when('the year 2000 and the month 12 are entered')
def input_december_birth(monkeypatch):

	monkeypatch.setattr('builtins.input', lambda _: '2000')
	assert read_exit(get_int('Enter birth year (YYYY): ', min = min_year, max = max_year, error = f'That is not a valid year from {min_year} to {max_year}!', escape = '')) == 2000

	monkeypatch.setattr('builtins.input', lambda _: '12')
	assert read_exit(get_int('Enter birth month (MM): ', min = 1, max = 12, error = 'That is not a valid month from 01 to 12 !', escape = '')) == 12

@then('the full retirement age of 67 years and 0 months and date December 2067 are shown')
def december_birth():

	full_retirement_age = create_full_retirement_age(2000, full_retirement_ages)
	assert full_retirement_age[0] == 67
	assert full_retirement_age[1] == 0

	retirement_date = create_retirement_date(2000, 12, full_retirement_age)
	assert months[retirement_date[1]] == 'December'
	assert retirement_date[0] == 2067

@scenario('full_retirement_age.feature', 'Invalid Birth Year')
def test_invalid_birth_year():

	pass

@when('"<invalid_year>" and a month are entered')
def input_invalid_birth_year(monkeypatch, invalid_year):

	monkeypatch.setattr('builtins.input', invalid_year) # No lambda here: scenario outline means the values are passed directly through the call to the examples table

@then('the program should produce an error')
def invalid_birth_year():

	with pytest.raises(TypeError):
		read_exit(get_int('Enter birth month (MM): ', min = 1, max = 12, error = 'That is not a valid month from 01 to 12 !', escape = ''))

@scenario('full_retirement_age.feature', 'Invalid Birth Month')
def test_invalid_birth_month():

	pass

@when('a birth year and "<invalid_month>" are entered')
def input_invalid_birth_month(monkeypatch, invalid_month):

	monkeypatch.setattr('builtins.input', invalid_month)

@then('the program should produce an error')
def invalid_birth_year():

	with pytest.raises(TypeError):
		read_exit(get_int('Enter birth month (MM): ', min = 1, max = 12, error = 'That is not a valid month from 01 to 12 !', escape = ''))

@scenario('full_retirement_age.feature', 'Enter')
def test_enter():

	pass

@when('the Enter key is pressed without other input')
def input_enter(monkeypatch):

	monkeypatch.setattr('builtins.input', lambda _: '')

@then('the program should exit without error')
def enter():

	with pytest.raises(SystemExit):
		read_exit(get_int('Enter birth year (YYYY): ', min = min_year, max = max_year, error = f'That is not a valid year from {min_year} to {max_year}!', escape = ''))
		read_exit(get_int('Enter birth month (MM): ', min = 1, max = 12, error = 'That is not a valid month from 01 to 12 !', escape = ''))