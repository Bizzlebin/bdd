# Full Retirement Age
# 
# full_retirement_age.feature
# 
# ***
# 
# By Jeremiah Thomas
# 
# ***
# 
# Created 2020-11-15
# 
# Updated 2020-11-19
# 
# +++
# Dedication
# 
# CSC 256-0001
# 
# +++
# Description
# 
# A Gherkin feature file for testing the Full Retirement Age 01 program; my first feature file. Note: example names must be valid Python variable names!
# 
# So far it seems that Gherkin *massively* complicates testing—why not just have managers write test scenarios as before but inline them as comments in a pytest module? Or just keep them as part of the acceptance test documentation in the requirements? It would do the same thing with less management *and* programmer overhead. I am not sure where Gherkin fits in, how much less to test, etc.
# 
Feature: Full Retirement Age
	As a user, I want to provide a birth year and month, so that I can receive the corresponding retirement age and date for full SSA benefits.

	Background:
		Given the program is running

	Scenario: January Birth
		When the year 2000 and the month 01 are entered
		Then the full retirement age of 67 years and 0 months and date January 2067 are shown

	Scenario: December Birth
		When the year 2000 and the month 12 are entered
		Then the full retirement age of 67 years and 0 months and date December 2067 are shown

	Scenario Outline: Invalid Birth Year
		When "<invalid_year>" and a month are entered
		Then the program should produce an error

		Examples: Invalid Years
			| invalid_year |
			|         1899 |
			|         2021 |
			|       2000.1 |
			|        -2000 |
			|            x |

	Scenario Outline: Invalid Birth Month
		When a birth year and "<invalid_month>" are entered
		Then the program should produce an error

		Examples: Invalid Months
			| invalid_month |
			|             0 |
			|            13 |
			|           1.1 |
			|            -1 |
			|             y |

	Scenario: Enter
		When the Enter key is pressed without other input
		Then the program should exit without error