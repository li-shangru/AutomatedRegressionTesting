#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parameter file for script `Generate_Tests.py`
"""

# Number of files to be generated, will replace old files
num_files = 10

# Number of lines in each generated file
num_lines = 100

# Path where files should be generated, relative to current file
file_path = "tests/"

# List of all possible game difficulty level
difficulty_level = [
	"easy", "medium", "hard"
]

# List of all possible move directions
move_direction = [
	"N", "S", "E", "W"
]
