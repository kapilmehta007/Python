import argparse

"""

"""


parser=argparse.ArgumentParser()
parser.add_argument("--number1", help="First number",required=True) 
parser.add_argument("--number2", help="Second number",required=True)
"""if we give a default value for operation,
 and also required as true and also if we dont give any value for operation
 then it throws an error"""
parser.add_argument("--operation", help="Operation", default="add",choices=["add", "subtract", "multiply", "divide"])
argv = parser.parse_args()
print("argv is",argv)
print ("number1 is",argv.number1)
print ("number2 is",argv.number2)
print ("operation is",argv.operation)

if(argv.operation == "add"):
    result= int(argv.number1) + int(argv.number2)
elif(argv.operation == "subtract"):
    result= int(argv.number1) - int(argv.number2)
elif(argv.operation == "multiply"):
    result= int(argv.number1) * int(argv.number2)
elif(argv.operation == "divide"):
    result= int(argv.number1) / int(argv.number2)
else:
    print("Invalid operation")
print("Result is",result)