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

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- jumper              (source code for game)
  +-- __main__.py       (program entry point)
  +-- director.py       (director class)
  +-- hint.py           (hint class)
  +-- parachute.py      (parachute class = Jumper)
  +-- terminal_service.py (terminal service class)
  +-- word.py           (word class)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0

## Authors
---
* AMERICO SADAO KUTOMI (kut22001@byui.edu)
