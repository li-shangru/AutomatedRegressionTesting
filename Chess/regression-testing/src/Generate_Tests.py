#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EECS3311 Software Design Winter 2020
Chess project random test generator
Generate `num_files` under `tests_path` with `num_lines` of commands
"""

import random
import os
import sys
sys.path.insert(1, '../')
import Parameters as par

__author__ = "Shangru Li"
__copyright__ = "Copyright 2020, Shangru Li"
__credits__ = "Shangru Li"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Shangru Li"
__email__ = "maxsli@protonmail.com"
__status__ = "Untested Prerelease Alpha Testing Unstable"

def main():
	for i in range(par.num_files):
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
				# Generate a random integer in range 1-13, included
				seed = random.randint(1, 13)
				# Generate commands accroading to the `seed`
				# Modify `if seed == INTEGER` accordingly
				if seed == 1:
					file.write(play())
				elif seed == 2 or seed == 3 or seed == 4:
					file.write(move("king"))
				elif seed == 5 or seed == 6 or seed == 7:
					file.write(move("knight"))
				elif seed == 8 or seed == 9 or seed == 10:
					file.write("undo")
				elif seed == 11 or seed == 12 or seed == 13:
					file.write("redo")
				else:
					print ('Unspecified seed value: %d' % seed)
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

def play():
	""" 
	Strats a new game in test mode provided game
	""" 
	size = str(random.randint(par.size_low, par.size_high))
	return "play(" + size + ")"

def move(piece_name):
	""" 
	Move a given chess piece
	""" 
	square_x = str(random.randint(par.square_low, par.square_high))
	square_y = str(random.randint(par.square_low, par.square_high))
	return "move_" + piece_name + "([" + square_x + "," + square_y + "])"

if __name__ == "__main__":
	main()
