# Puzzle
import random
from terminal_service import TerminalService

class Puzzle:
    """ The Puzzle to be found by a player (or the Jumper). A word is the puzzle.
    
    The responsibility of Puzzle is to supply a random word and to indicate if the player guessed letter is correct or not.
    
    Attributes:
        list_of_words (List[string]): A list of possible words to be selected.
        word: The puzzle itself which is a word from the list
        hint: The hint with blank lines and or the correct letters guessed by the player in the word
        letters: The correct guesses player made
        terminal_service: For getting and displaying information on the terminal.
"""

    def __init__(self):
        """Constructs a new Puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._list_of_words = ( ["ambush", "banana", "chronicle", "diatonic", "earnestly", "fantasy", "garland",
            "helical", "industriousness", "jeopardize", "kaleidoscope", "linger", "manuscript", "newbie",
            "ostracism", "phimosis", "quartile", "raspberry", "snowflake", "thunderbolt", "umbrella",
            "volunteer", "worthless", "xylophone", "yogurt", "zambian" ] )
        self._word = self._list_of_words[ random.randint(0, 25) ]
        self._hint = "_" * len(self._word)          # repeats "_" the quantity of letters; all blank lines
        self._letters = ''                          # no letter guesses yet
        self._terminal_service = TerminalService()
    
    def draw_hint(self):
        complete_text = ''
        for n in range(len(self._hint)):
            complete_text += self._hint[n] + ' '
        self._terminal_service.write_text(f'\n{complete_text}\n')

    def is_found(self):
        """Whether or not the Puzzle Word has been found.

        Args:
            self (Puzzle): An instance of Puzzle.
            
        Returns:
            boolean: True if the Puzzle was found; false if otherwise.
        """
        return (self._word == self._hint)

    def watch_letter(self, letter):
        """Whether or not the letter is in Puzzle

        Args:
            self (Puzzle): An instance of Puzzle.
            
        Returns:
            boolean: True if the letter is in the Puzzle; false if otherwise.
        """
        # checks if the letter exists in the Word
        in_word = letter in self._word

        # if letter exists in the Puzzle, the solution is updated
        if in_word:
            if not letter in self._letters:                         # the letter was not used yet
                self._letters += letter                             # add letter to the correct guessed letters
                for n in range(len(self._word)):                    
                    if self._word[n] == letter:                     # if in the letter position
                        self._hint = self._hint[:n] + letter + self._hint[n+1:]  # change the blank line by the letter
        
        # returns true if letter is in the Puzzle
        return in_word
