
class Hint:
    """ The Hint is a clue to the player (or the Jumper).
    
    The responsibility of Hint is to compare a word (the puzzle) with the letters guessed by the player and show the result.
    
    Attributes:
        _word: the word used in the game as a puzzle
        _hint: The hint with blank lines and or the correct letters guessed by the player in the word
        _letters: The correct guesses player made
    """

    def __init__(self, word):
        """Constructs a new Hint.

        Args:
            self (Hint): An instance of Hint.
        """
        self._word = word                           # stores the word as Puzzle
        self._hint = "_" * len(self._word)          # repeats "_" the quantity of letters; all blank lines
        self._letters = ''                          # no letter guesses yet
    
    def get_hint(self):
        """Gets a hint for the jumper.

        Args:
            self (Hint): An instance of Hint.
        
        Returns:
            string: A hint for the jumper.
        """
        
        return self._hint

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
