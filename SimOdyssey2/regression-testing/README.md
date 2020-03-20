# Introduction

This software includes a pure random test generation tool to generate input test
cases for EECS3311 SimOdyssey project.

Combined with the ETF regression testing suite, to achieve fully automated testing.

## Getting Started

1. Place the `oracle.exe` under the current directory.

2. Place the finalized version of your project (located at `EIFGENs/simodyssey/F_code/maze`) under the current directory.

3. Rename `simodyssey` to `simodyssey.exe`.

4. Make sure `simodyssey.exe` has executable mode, if not, run `chmod 700 simodyssey.exe`.

5. Execute the automated testing script by running `./Automate.py` from command line.

6. (optional) Modify the content of `Parameters.py` to customize testing parameters.

## Overview

* [`Generate_Tests.py`](./src/Generate_Tests.py) will generate random acceptance tests file specially for Maze project.

* [`ETF_Test.py`](./src/ETF_Test.py) will run the generated acceptance tests on `oracle.exe` and `simodyssey.exe`, then compare the output.

* [`Parameters.py`](./Parameters.py) contains the parameters for the two scripts above.

* [`Automate.py`](./Automate.py) will automate the process of generate random tests and running regression testing.
