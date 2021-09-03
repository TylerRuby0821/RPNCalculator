from os import system, name           # Importing from os for out clear function
import operator                       # Importing operator madule for later use
import re                             # Imported for Regex Checker

# Declaring a basic clear function to declutter the command line and terminal upon launch
def clear():
  if name == 'nt':
    _= system('cls')
  else:
    _= system('clear')

# Regex character check, to look for letters not used for commands
def char_check(i):
  return re.search(r'[a-zA-Z]$', i)

class RPNCalculator:

  """ Creating a basic reverse polish notation calculator """


  def __init__(self, stack = [], operations ={
      "+" : operator.add,
      "-" : operator.sub,
      "/" : operator.truediv,
      "*" : operator.mul
      }):

    self.stack = stack
    self.operations = operations

  def handle_command(self, user_in):
    if user_in == "q":             # If the user inputs "q" the program should close
        print("Calculations Complete!") # Brief message before closing for more dynamic user interaction
        exit()
    if user_in == "c":
      self.stack = []
      print("Cleared\n")

                    
  def calculate(self, user_input):
    split = user_input.split(' ')     # Spliting the user input on spaces and assigning it to a variable
    for char in split:                # Iterate through the split input
      if char in self.operations:          # Checking if the current character is an operator, if so we pop the first two items off the stack, save them to
        if len(self.stack) < 2:
          print("Error: Not enough values to perform an operation.")
          continue
        self.stack.append(self.operations[char](float(self.stack.pop(-2)), float(self.stack.pop())))
        # print("After Operation",stack)
      else:
        try:                           # If the char is not an operator, we simply append it to the stack.
          self.stack.append(float(char))
        except ValueError:
          print("Error: Non-Used Character input, Please enter real numbers, Valid operators(+, - , /, *) or q to exit.")
          continue
    if len(self.stack) >= 1:
      return self.stack[-1]              # Printing the ouput





#Start by Clearing the terminal, to prevent clutter and make the calculator stand out on its own
#Print a greeting to the user, as well as a brief description of an RPN Calculator and an example.
#Send them on their way to calculating!
clear()
new_calc = RPNCalculator()
print("Welcome to my RPN Calculator\n")
print("With an RPN calculator, please enter all values first, followed by the operations.")
print("Example:\nInput: 8 2 +\nOutput: 10\n")
print("Enter c to start a new calculation.")
print("Enter q to exit the program.")
print("Happy Calculating!\n")

# Initializing a Stack
stack = []
# While loop, allowing exit of the calculator when q is the input and keeping our session from closing without user input
while True:
  # Opening up an input for the user and assigning it to our variable
  user_input = input('> ')
  if char_check(user_input):
    new_calc.handle_command(user_input)
  else:
    print(new_calc.calculate(user_input))

  

