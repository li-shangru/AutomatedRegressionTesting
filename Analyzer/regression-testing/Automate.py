#!/usr/bin/env python3
###########################################################################
# Automated the proccess of regression testing
# Generate test files and run regression test on these tests.
###########################################################################
import ETF_Test
import Generate_Tests

Generate_Tests.main()
ETF_Test.main()