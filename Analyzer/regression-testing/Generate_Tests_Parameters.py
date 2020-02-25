#!/usr/bin/env python3
###########################################################################
# Parameter file for script `Generate_Tests.py`
###########################################################################

# Number of files to be generated, will replace old files
num_files = 10

# Number of lines in each generated file
num_lines = 100

# Path where files should be generated, relative to current file
file_path = "tests/"

# List of all possible variable names
var_name = [
	"\"Result\"", "\"v1\"", "\"v2\"", "\"v3\""
]

# List of all possible feature names
feature_name = [
	"\"f1\"", "\"f2\"", "\"f3\""
]

# List of all possible class names
class_name = [
	"\"INTEGER\"", "\"BOOLEAN\"", "\"A\"", "\"B\"", "\"C\""
]

# TOP BOUND of the number of parameters in command, query and size of call chain
num_parameters = 3

# Lower bound of the value generated for event `int_value`
int_value_lower_bound = -10

# Top bound of the value generated for event `int_value`
int_value_top_bound = 10