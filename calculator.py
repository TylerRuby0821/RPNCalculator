import os
import operator

operations = {
  "+" : operator.add,
  "-" : operator.sub,
  "/" : operator.truediv,
  "*" : operator.mul
}
print("Welcome to my RPN Calculator")     #Basic Welcome message to let the user know what this program is.
print("With an RPN calculator, please enter all values first, followed by the operations.")
print("Enter q to exit the program.")
print("Happy Calculating!")
            
stack = []               # Initializing a Stack
while True:            #while loop, allowing exit of the calculator when q is the input
  user_input = input('') #opening up an input for the user and assigning it to our variable
  if user_input == "q":
    exit()
  split = user_input.split(' ')
  for char in split:
    print(char)
    if char == ' ':
      pass
    if char in operations:
      op2 = stack.pop()
      print("OP 1", op2)
      op = stack.pop()
      print("OP 2", op)
      print("stack after pops", stack)
      stack.insert(0, operations[char](int(op), int(op2)))
      print("Stack after operation", stack)
    else:
      stack.append(char)
      print(stack)
  print(stack[0])
