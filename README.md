Arithmetic Command-Line Tool

This Python script performs basic arithmetic operations (add, subtract, multiply, divide) using command-line arguments.

Description:

The script takes three arguments:

    --number1: First number (required)

    --number2: Second number (required)

    --operation: Arithmetic operation to perform. Optional (defaults to "add"). Valid choices: add, subtract, multiply, divide

It uses Python’s built-in argparse module to parse and validate inputs.

# Addition (default operation)
python script.py --number1 10 --number2 5

# Subtraction
python script.py --number1 10 --number2 5 --operation subtract

# Multiplication
python script.py --number1 10 --number2 5 --operation multiply

# Division
python script.py --number1 10 --number2 5 --operation divide

Output:

argv is Namespace(number1='10', number2='5', operation='add')
number1 is 10
number2 is 5
operation is add
Result is 15
