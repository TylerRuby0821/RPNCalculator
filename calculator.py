class Calculator:
  """
    Setting up a Class for out calculator.
  """

  def calculate(self, s):
    """
    Primary function to run the calculations
    """
    current = []
    operands = ["+", "-", "/", "*"]
    if operands not in s:
      current.append(s)
      return s
    else:
      new_calculation = s.split(' ')
      return output


print("Welcome to my RPN Calculator")     #Basic Welcome message to let the user know what this program is.
print("With an RPN calculator, please enter all values first, followed by the operations.")
calculator = Calculator()                     #Creating a new instance of our calculator class
user_input = ""                               #Creating a variable to hold user input
while user_input is not ["q"]:                #while loop, allowing exit of the calculator when q is the input
  user_input = input('')                      #opening up an input for the user and appending it to our variable
  output = calculator.calculate(user_input)   #setting up an output variable, where we runt our calculate function on the users input
  print(output)                               # returning the output to the user
