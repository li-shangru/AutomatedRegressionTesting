#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EECS3311 Software Design Winter 2020
SimOdyssey2 project random test generator
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
					file.write("play")
				elif seed == 2:
					file.write("abort")
				elif seed == 3:
					file.write("land")
				elif seed == 4:
					file.write("liftoff")
				elif seed == 5:
					file.write("pass")
				elif seed == 6:
					file.write("wormhole")
				elif seed == 7:
					file.write("status")
				elif seed == 8:
					file.write(test())
				elif seed == 9 or seed == 10 or seed == 11 or seed == 12 or seed == 13:
					# Move the player character to a direction.
					file.write(move())
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

def test():
	""" 
	Strats a new game in test mode provided game
	""" 
	a_threshold = str(random.randint(par.threshold_low, par.threshold_high))
	j_threshold = str(random.randint(par.threshold_low, par.threshold_high))
	m_threshold = str(random.randint(par.threshold_low, par.threshold_high))
	b_threshold = str(random.randint(par.threshold_low, par.threshold_high))
	p_threshold = str(random.randint(par.threshold_low, par.threshold_high))
	threshold = [a_threshold, j_threshold, m_threshold, b_threshold, p_threshold]
	threshold.sort()
	return "test(" + threshold[0] + ", " + threshold[1] + ", " + threshold[2] + ", " + threshold[3] + ", " + threshold[4] + ")"

def move():
	""" 
	Move the explorer in a given direction
	""" 
	direction = par.direction[random.randint(0, (len(par.direction)-1))]
	return "move(" + direction + ")"

if __name__ == "__main__":
	main()
