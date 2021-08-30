import os
import operator

operations = {
  "+" : operator.add,
  "-" : operator.sub,
  "/" : operator.truediv,
  "*" : operator.mul
}

class Calculator:
  """
    Setting up a Class for out calculator.
  """

  def calculate(self, s):
    """
    Primary function to run the calculations
    """
    if s == "q":
      exit()
    split = s.split(' ')
    stack = []
    for char in split:
      print(char)
      if char == ' ':
        pass
      if char in operations:
        op2 = stack.pop()
        op = stack.pop()
        stack.append(operations[char](int(op), int(op2)))
      else:
        stack.append(char)
        print(stack)
    print(stack.pop())

print("Welcome to my RPN Calculator")     #Basic Welcome message to let the user know what this program is.
print("With an RPN calculator, please enter all values first, followed by the operations.")
print("Enter q to exit the program.")
print("Happy Calculating!")
calculator = Calculator()                     #Creating a new instance of our calculator class
user_input = ""                               #Creating a variable to hold user input
while user_input is not ["q"]:                #while loop, allowing exit of the calculator when q is the input
  user_input = input('')                      #opening up an input for the user and assigning it to our variable
  output = calculator.calculate(user_input)   #setting up an output variable, where we runt our calculate function on the users input
  print(output)                               # returning the output to the user
