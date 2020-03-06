#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EECS4302 Compiler and Intreters Winter 2020
Solver project random test generator
Generate `num_files` under `tests_path` with `num_lines` of commands
"""

import random
import os
import sys
sys.path.insert(1, '../')
import Parameters as par
import importlib

__author__ = "Shangru Li"
__copyright__ = "Copyright 2020, Shangru Li"
__credits__ = "Shangru Li"
__license__ = "MIT"
__version__ = "0.3"
__maintainer__ = "Shangru Li"
__email__ = "maxsli@protonmail.com"
__status__ = "Untested Prerelease Alpha Testing Unstable"

variables = par.variables
decleared = []

def main():
	for i in range(par.num_files):
		initialize_variables()
		# Create `tests_path` if not exists
		if not os.path.exists(par.tests_path):
			try:
				os.mkdir(par.tests_path)
			except OSError:
				print ("Creation of the directory %s failed" % par.tests_path)
		# Open the file `at(i+1).txt` and overwrite its content
		# `open([path_to_file], [mode])`.
		# mode: "a" - Append - will append to the end of the file
		# mode: "w" - Write - will overwrite any existing content
		try:
			file = open(par.tests_path + "at" + str(i+1) + ".txt", "w+")
			for j in range(par.num_lines):
				# Generate a random integer in range 1-14, included
				seed = random.randint(1, 2)
				# Generate commands accroading to the `seed`
				# Modify `if seed == INTEGER` accordingly
				if seed == 1 and len(variables) > 0:
					file.write(variable_declearation())
				elif seed == 2 and len(decleared) > 0:
					file.write(verify())
				else:
					j = j - 1
				# Write a new line to end of each line if it's not the last
				if j != (par.num_lines - 1):
					file.write('\n')
			# Close file after finish writing
			try:
				file.close
				print ("Generated test file: " + par.tests_path + "at" + str(i+1) + ".txt.")
			except OSError:
				print ("Close file %s failed" % par.tests_path + "at" + str(i+1) + ".txt")
		except OSError:
			print ("Open file %s failed" % par.tests_path + "at" + str(i+1) + ".txt")
	print ("================================================")
	print ("Successfully generated " + str(par.num_files) + " test files.")
	print ("================================================")

def variable_declearation():
	""" 
	Declear a new variable
	""" 
	variable = variables[random.randint(0, (len(variables)-1))]
	variables.remove(variable)
	decleared.append(variable)
	if random.randint(0,1) is 0:
		return "var " + variable
	else:
		if random.randint(0,1) is 0:
			return "var " + variable + " = false"
		else:
			return "var " + variable + " = true"

def verify():
	""" 
	Verify a randomly generated expression
	""" 
	return "verify " + generate_expression(0)

def generate_expression(recursive_depth):
	"""
	Generate a random expression recursively
	"""
	seed = random.randint(1, 12)
	# Base case: return a random variable, could be undeclared
	if seed == 1 and recursive_depth < 5:
		return "not " + generate_expression(recursive_depth+1)
	elif seed == 2 and recursive_depth < 5:
		return generate_expression(recursive_depth+1) + " or " + generate_expression(recursive_depth+1)
	elif seed == 3 and recursive_depth < 5:
		return generate_expression(recursive_depth+1) + " and " + generate_expression(recursive_depth+1)
	elif seed == 4 and recursive_depth < 5:
		return generate_expression(recursive_depth+1) + " => " + generate_expression(recursive_depth+1)
	elif seed == 5 and recursive_depth < 5:
		return generate_expression(recursive_depth+1) + " <=> " + generate_expression(recursive_depth+1)
	elif seed == 6 and recursive_depth < 5:
		return "(" + generate_expression(recursive_depth+1) + ")"
	elif seed == 7:
		return "true"
	elif seed == 8:
		return "false"
	else:
		return decleared[random.randint(0, (len(decleared)-1))]

def initialize_variables():
	importlib.reload(par)
	global variables
	global decleared
	variables = par.variables
	decleared = []

if __name__ == "__main__":
	main()
