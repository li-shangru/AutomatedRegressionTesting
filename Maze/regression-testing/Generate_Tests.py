#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EECS3311 Software Design Winter 2020
Maze project random test generator
Generate `num_files` under `file_path` with `num_lines` of commands
"""

import random
import os
import Generate_Tests_Parameters as par

__author__ = "Shangru Li"
__copyright__ = "Copyright 2020, Shangru Li"
__credits__ = "Shangru Li"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Shangru Li"
__email__ = "maxsli@protonmail.com"
__status__ = "Untested Prerelease Alpha Testing Very Unstable"

def main():
	for i in range(par.num_files):
		# Create `file_path` if not exists
		if not os.path.exists(par.file_path):
			try:
				os.mkdir(par.file_path)
			except OSError:
				print ("Creation of the directory %s failed" % par.file_path)
		# Open the file `at(i+1).txt` and overwrite its content
		# `open([path_to_file], [mode])`.
		# mode: "a" - Append - will append to the end of the file
		# mode: "w" - Write - will overwrite any existing content
		try:
			file = open(par.file_path + "at" + str(i+1) + ".txt", "w+")
			for j in range(par.num_lines):
				# Generate a random integer in range 1-8, included
				seed = random.randint(1, 8)
				# Generate commands accroading to the `seed`
				# Modify `if seed == INTEGER` accordingly
				if seed == 1:
					# Calculate the solution path.
					file.write("solve")
				elif seed == 2:
					# Abort the current game.
					file.write("abort")
				elif seed == 3 or seed == 4:
					# Create a new game.
					file.write(new_game())
				elif seed == 5 or seed == 6 or seed == 7 or seed == 8:
					# Move the player character to a direction.
					file.write(move_direction())
				else:
					print ('Unspecified seed value: %d' % seed)
				# Write a new line to end of each line if it's not the last
				if j != (par.num_lines - 1):
					file.write('\n')
			# Close file after finish writing
			try:
				file.close
				print ("Generated test file: " + par.file_path + "at" + str(i+1) + ".txt.")
			except OSError:
				print ("Close file %s failed" % par.file_path + "at" + str(i+1) + ".txt")
		except OSError:
			print ("Open file %s failed" % par.file_path + "at" + str(i+1) + ".txt")
	print ("================================================")
	print ("Successfully generated " + str(par.num_files) + " test files.")
	print ("================================================")

def new_game():
	""" 
	Create a new game with random difficulty
	""" 
	# Pick a random difficulty level from `difficulty_level`
	level = par.difficulty_level[random.randint(0, (len(par.difficulty_level)-1))]
	return "new_game(" + level + ")"

def move_direction():
	""" 
	Move the player character in the random direction
	""" 
	# Pick a random direction from `move_direction`
	direction = par.move_direction[random.randint(0, (len(par.move_direction)-1))]
	return "move(" + direction + ")"

if __name__ == "__main__":
	main()
