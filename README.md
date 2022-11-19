# cse210-03
CSE210 Week 3 Assignment - Jumper

The Jumper game is used to exemplify the use of encapsulation in classes.

The Director objects uses the following objects:
- Parachute;
- Word;
- Hint;
- Terminal Service.

These objects have their states as private. The Director object uses them indirectly by methods. It is not possible to read nor change them directly.

This is an example of encapsulation, to prevent an object user from doing anything bad with the states internally used by the classes.
