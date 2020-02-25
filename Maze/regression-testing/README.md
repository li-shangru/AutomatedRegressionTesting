# Introduction

This software includes a pure random test generation tool to generate input test
cases for EECS3311 Maze project.

Combined with the ETF regression testing suite, to achieve fully automated testing.

## Getting Started

1. Place the `oracle.exe` under the current directory.

2. Place the finalized version of your project (located at `EIFGENs/maze/F_code/maze`) under the current directory.

3. Rename `maze` to `maze.exe`.

4. Make sure `maze.exe` has executable mode, if not, run `chmod 700 maze.exe`.

5. Execute the automated testing script by running `./Automate.py` from command line.

6. (optional) Modify the content of `Parameters.py` to customize testing parameters.

## Overview

* __`Generate_Tests.py`__ will generate random acceptance tests file specially for Maze project.

* __`ETF_Test.py`__ will run the generated acceptance tests on `oracle.exe` and `maze.exe`, then compare the output.

* __`Parameters.py`__ contains the parameters for the two scripts above.

* __`Automate.py`__ will automate the process of generate random tests and running regression testing.
