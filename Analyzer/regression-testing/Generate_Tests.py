#!/usr/bin/env python3
###########################################################################
# Author:	Shangru Li (Max)
# Version:	0.4
# Date:		2019/11/21
# Warning:	Untested prerelease alpha testing unstable version
###########################################################################
# EECS3311 Software Design Fall 2019
# Analyzer project random test generator
# Generate `num_files` under `file_path` with `num_lines` of command
###########################################################################
import random
import os
import Generate_Tests_Parameters as par

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
				# Generate a random integer in range 1-13, included
				seed = random.randint(1, 13)
				# Generate commands accroading to the `seed`
				# Modify `if seed == INTEGER` accordingly
				if seed == 1:
					# Is the specified program type-correct?
					file.write("type_check")
				elif seed == 2:
					# For the program specified, generate Java-like code.
					file.write("generate_java_code")
				elif seed == 3:
					# Add a new class with name `cn`.
					file.write(add_class())
				elif seed == 4:
					# Add to class `cn` a new attribute `fn` with type `ft`.
					file.write(add_attribute())
				elif seed == 5:
					# Add to class `cn` a new command `fn` with a list of parameters `ps`.
					file.write(add_command())
				elif seed == 6:
					# Add to class `cn` a new query `fn` with a list of parameters `ps`
					file.write(add_query())
				elif seed == 7:
					# Assign to variable with name `n`, in the context of routine `fn` in class `cn`.
					file.write(add_assignment_instruction())
				elif seed == 8:
					# Add a chain of calls to attributes (not queries or commands).
					file.write(add_call_chain())
				elif seed == 9:
					# Events of users adding constants
					file.write(adding_constant())
				elif seed == 10:
					# Events of users adding binary arithmetic operations
					file.write(adding_arithmetic())
				elif seed == 11:
					# Events of users adding binary logical operations
					file.write(adding_logical())
				elif seed == 12:
					# Events of users adding binary relational operations
					file.write(adding_relational())
				elif seed == 13:
					# Events of users adding unary numerical or logical operations
					file.write(adding_numerical())
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

def add_class():
	""" 
	Add a new class with name `cn`.
	""" 
	# Pick a random class name from `class_name`
	cn = par.class_name[random.randint(0, (len(par.class_name)-1))]
	return "add_class(" + cn + ")"

def add_attribute():
	""" 
	add_attribute(
	cn: CLASS_NAME;    -- context class
	fn: FEATURE_NAME;  -- name of attribute
	ft: CLASS_NAME     -- attribute type
	)
	Add to class `cn` a new attribute `fn` with type `ft`.
	""" 
	# Pick a random class name from `class_name`
	cn = par.class_name[random.randint(0, (len(par.class_name)-1))]
	# Pick a random feature name from `feature_name`
	fn = par.feature_name[random.randint(0, (len(par.feature_name)-1))]
	# Pick another random class name from `class_name`
	ft = par.class_name[random.randint(0, (len(par.class_name)-1))]
	return "add_attribute(" + cn + ", " + fn + ", " + ft + ")"


def add_command():
	""" 
	add_command(
		cn: CLASS_NAME;                                 -- context class
		fn: FEATURE_NAME;                               -- name of command
		ps: ARRAY[TUPLE[pn: VAR_NAME; ft: CLASS_NAME]]  -- parameters
	)
	Add to class `cn` a new command `fn` with a list of parameters `ps`.
	Each parameter is a tuple with parameter name `pn` and type `ft`.
	""" 
	# Pick a random class name from `class_name`
	cn = par.class_name[random.randint(0, (len(par.class_name)-1))]
	# Pick a random feature name from `feature_name`
	fn = par.feature_name[random.randint(0, (len(par.feature_name)-1))]
	ps = ["<<"]
	# Randomly generate the parameters
	for i in range(random.randint(0, par.num_parameters)):
		ps.append("[")
		# Pick a random variable name from `var_name`
		pn = par.var_name[random.randint(0, (len(par.var_name)-1))]
		# Pick a random class name from `class_name`
		rt = par.class_name[random.randint(0, (len(par.class_name)-1))]
		ps.append(pn + ", " + rt + "]")
		if i != (par.num_parameters - 1):
			ps.append(", ")
	ps.append(">>")
	return "add_command(" + cn + ", " + fn + ", " + ''.join(ps) + ")"


def add_query():
	""" 
	add_query(
		cn: CLASS_NAME;                                  -- context class
		fn: FEATURE_NAME;                                -- name of query
		ps: ARRAY[TUPLE[pn: VAR_NAME; pt: CLASS_NAME]];  -- parameters
		rt: CLASS_NAME                                   -- return type
	)
	Add to class `cn` a new query `fn` with a list of parameters `ps`
	and return type `rt`.
	Each parameter is a tuple with parameter name `pn` and type `ft`.
	""" 
	# Pick a random class name from `class_name`
	cn = par.class_name[random.randint(0, (len(par.class_name)-1))]
	# Pick a random feature name from `feature_name`
	fn = par.feature_name[random.randint(0, (len(par.feature_name)-1))]
	ps = ["<<"]
	# Randomly generate the parameters
	for i in range(random.randint(0, par.num_parameters)):
		ps.append("[")
		# Pick a random variable name from `var_name`
		pn = par.var_name[random.randint(0, (len(par.var_name)-1))]
		# Pick a random class name from `class_name`
		rt = par.class_name[random.randint(0, (len(par.class_name)-1))]
		ps.append(pn + ", " + rt + "]")
		if i != (par.num_parameters - 1):
			ps.append(", ")
	ps.append(">>")
	# Pick a random class name from `class_name`
	rt = par.class_name[random.randint(0, (len(par.class_name)-1))]
	return "add_query(" + cn + ", " + fn + ", " + ''.join(ps) + ", " + rt + ")"


def add_assignment_instruction():
	""" 
	add_assignment_instruction (cn: CLASS_NAME; fn: FEATURE_NAME; n: VAR_NAME)
	Assign to variable with name `n`, in the context of routine `fn` in class `cn`.
	Here `n` should either be `Result` (in the context of a query),
	or an attribute name in the current class.
	""" 
	# Pick a random class name from `class_name`
	cn = par.class_name[random.randint(0, (len(par.class_name)-1))]
	# Pick a random feature name from `feature_name`
	fn = par.feature_name[random.randint(0, (len(par.feature_name)-1))]
	# Pick another random class name from `class_name`
	n = par.var_name[random.randint(0, (len(par.var_name)-1))]
	return "add_assignment_instruction(" + cn + ", " + fn + ", " + n + ")"


def add_call_chain():
	""" 
	add_call_chain(chain: ARRAY[VAR_NAME])
	Add a chain of calls to attributes (not queries or commands).
	""" 
	chain = ["<<"]
	# Randomly generate the parameters
	for i in range(random.randint(0, par.num_parameters)):
		# Pick a random variable name from `var_name`
		var = par.var_name[random.randint(0, (len(par.var_name)-1))]
		chain.append(var)
		if i != (par.num_parameters - 1):
			chain.append(", ")
	chain.append(">>")
	return "add_call_chain(" + ''.join(chain) + ")"


def adding_constant():
	""" 
	Events of users adding constants, randomly pick one of the two
	""" 
	if random.randint(0, 1) == 1:
		result = bool_value()
	else:
		result = int_value()
	return result


def bool_value():
	""" 
	bool_value (c: BOOLEAN)
	""" 
	if random.randint(0, 1) == 1:
		result = "True"
	else:
		result = "False"
	return "bool_value(" + result + ")"


def int_value():
	""" 
	int_value (c: INTEGER)
	""" 
	result = random.randint(par.int_value_lower_bound, par.int_value_top_bound)
	return "int_value(" + str(result) + ")"


def adding_arithmetic():
	""" 
	Events of users adding binary arithmetic operations
	addition
	subtraction
	multiplication
	quotient
	modulo
	""" 
	seed = random.randint(1, 5)
	if seed == 1:
		result = "addition"
	elif seed == 2:
		result = "subtraction"
	elif seed == 3:
		result = "multiplication"
	elif seed == 4:
		result = "quotient"
	elif seed == 5:
		result = "modulo"
	else:
		print ('Unspecified seed value: %d' % seed)
	return result


def adding_logical():
	""" 
	Events of users adding binary logical operations
	conjunction
	disjunction
	""" 
	seed = random.randint(1, 2)
	if seed == 1:
		result = "conjunction"
	elif seed == 2:
		result = "disjunction"
	else:
		print ('Unspecified seed value: %d' % seed)
	return result


def adding_relational():
	""" 
	Events of users adding binary relational operations
	equals
	greater_than
	less_than
	""" 
	seed = random.randint(1, 3)
	if seed == 1:
		result = "equals"
	elif seed == 2:
		result = "greater_than"
	elif seed == 3:
		result = "less_than"
	else:
		print ('Unspecified seed value: %d' % seed)
	return result


def adding_numerical():
	""" 
	Events of users adding unary numerical or logical operations
	numerical_negation
	logical_negation
	""" 
	seed = random.randint(1, 2)
	if seed == 1:
		result = "numerical_negation"
	elif seed == 2:
		result = "logical_negation"
	else:
		print ('Unspecified seed value: %d' % seed)
	return result

if __name__ == "__main__":
	main()
