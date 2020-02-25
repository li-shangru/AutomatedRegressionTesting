# Usage

`Generate_Tests.py` will produce arbitrary number of tests according to the parameters set in `Generate_Tests_Parameters.py`
Alter the variables in `Generate_Tests_Parameters.py` if thee wish.

Please place the `oracle.exe` given by the professor and the finalized `exe` file by your project in the current directory.
Your finalized `exe` file can be found, after finalizing your system, under `EIFGENs/analyzer/F_code/`. Change `analyzer` to `analyzer.exe`.
If your `exe` file cannot execute, please also add executable mode to it by running `chmod 700 analyzer.exe`

`Automate.py` will automate the whole process of regression testing, generates tests then run the tests on the oracle and your program.
Simply execute `Automate.py` and then viola!

Good luck and have fun.