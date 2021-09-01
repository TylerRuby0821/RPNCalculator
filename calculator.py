from os import system, name           # Importing from os for out clear function
import operator                       # Importing operator madule for later use
import re

def char_check(i):
  return re.search(r'[a-zA-Z]$', i)

def clear():                          # Declaring a basic clear function to declutter the command line and terminal upon launch
  if name == 'nt':
    _= system('cls')
  else:
    _= system('clear')

operations = {                        # Defining an operations dictionary with the user of the operator module for later
  "+" : operator.add,
  "-" : operator.sub,
  "/" : operator.truediv,
  "*" : operator.mul
}


#Start by Clearing the terminal, to prevent clutter and make the calculator stand out on its own
#Print a greeting to the user, as well as a brief description of an RPN Calculator and an example.
#Send them on their way to calculating!

clear()
print("Welcome to my RPN Calculator\n")
print("With an RPN calculator, please enter all values first, followed by the operations.")
print("Example:\nInput: 8 2 +\nOutput: 10\n")
print("Enter c to start a new calculation.")
print("Enter q to exit the program.")
print("Happy Calculating!")

stack = []                          # Initializing a Stack
while True:                         # While loop, allowing exit of the calculator when q is the input and keeping our session from closing without user input
  user_input = input('> ')
  if char_check(user_input):
              # Opening up an input for the user and assigning it to our variable
    if user_input == "q":             # If the user inputs "q" the program should close
      print("Calculations Complete!") # Brief message before closing for more dynamic user interaction
      break                     # Closes the program
    else:
      print("Error: Non-Used Character input, Please enter real numbers, operators or q to exit.")
      
  split = user_input.split(' ')     # Spliting the user input on spaces and assigning it to a variable
  for char in split:                # Iterate through the split input
    if char in operations:          # Checking if the current character is an operator, if so we pop the first two items off the stack, save them to
      stack.append(operations[char](float(stack.pop(-2)), float(stack.pop())))
      print("After Operation",stack)
    else:                           # If the char is not an operator, we simply append it to the stack.
      stack.append(float(char))
      print(stack)
  if len(stack) == 1:
    print(stack[-1])                # Printing the ouput

  # else:
  #   print("Error: Input Not Formated Correctly")
