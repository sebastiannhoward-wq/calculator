# Calculator
A python 3 calulator used from the Terminal, built step by step in SCCM4910

## What it will do
Add, subtract, multiply and divide two numbers; display the result.

## How to run it
use ./run.sh to run it, stop with ctrl+c, test with 6*7=42
From Week 3: python3 calculator.py
Enter the first number, operator (+ - * /), then second number.
The program prints Result: followed by the answer
Here I added an extra line so that git can see an edit

## How to test it
Use this command to enter the virtual environment with pytest installed:

source /opt/python-venv/sccm-4910/bin/activate

Once this command has been run, then run the command ./check.sh
This command will run the pytest on the calculator and confirm that all of the different functions are working as they should.
The result should be 4 passes (one for each operation) and a special addition case

