# conftest
# 
# conftest.py
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
# A small program to provide universal givens for pytest-bdd.
# 

# 
# +++
# Imports
# 
import pytest
from pytest_bdd import given
# 
# +++
# Functions
# 
# ===
# Definitions
# 
@given('the program is running')
def is_running():

	pass