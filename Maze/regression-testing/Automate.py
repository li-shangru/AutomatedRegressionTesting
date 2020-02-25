#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Automated the proccess of regression testing
Generate test files and run regression testing on these tests.
"""

import sys
sys.path.insert(1, './src')
import ETF_Test
import Generate_Tests

Generate_Tests.main()
ETF_Test.main()