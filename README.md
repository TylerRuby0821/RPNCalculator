# CLI RPN Calculator
#### Submitted by: Tyler Ruby
## Features

- Ability for users to enter single or multiple numbers at a time for calculation.
- Basic operations (Add, Subtract, Multiply, Divide).
- Ability for users to clear the current calculation, allowing multiple calculations without closing the application.
- Ability for users to end the program by entering "q".
- Validation to handle characters, as well as out of order operations.


## Reasoning
I stand behind my technical choices of keeping the calculator as straight the the point of RPN format, in the CLI as possible. The program is developed with multiple comment and print statements, designed to improve quality for developers as well as users. I use a function off launch to clear the console, followed by multiple prints giving fairly detailed instruction of how the calculator works and should be used. It takes in user input, feeding out either a response of what was entered, or the calculation, depending on how many, and where the inputs were made during the calculation.
I use Regex, to search the input for characters, allowing the use of both character commands like "q" to exit the program, but also to handle validation and errors of a user input.

## Changes
Things I would like to implement futher:
[] Re-format existing code into a class based structure, allowing for more automation of testing using something like Pytest
[] Add expanded operations such as Modulo, etc.
[] Improve upon my design, making it as efficient as possible and eliminating unneccsary code.

## How it Works
You will need Python 3 installed.
Simply pull the code, and run "python3 calculator.py" to start the CLI interface.
After that, there are brief on screen instructions for guidance.
