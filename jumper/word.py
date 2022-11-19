import random

class Word:
    """ The word to be found by a player (or the Jumper). The word is the puzzle.
    
    The responsibility of Word is to supply a random word and to indicate if the player guessed letter is correct or not.
    
    Attributes:
        _list_of_words (List[string]): A list of possible words to be selected.
        _word: The puzzle itself which is a word from the list
    """

    def __init__(self):
        """Constructs a new Word.

        Args:
            self (Word): An instance of Word.
        """
        self._list_of_words = ( ["ambush", "banana", "chronicle", "diatonic", "earnestly", "fantasy", "garland",
            "helical", "industriousness", "jeopardize", "kaleidoscope", "linger", "manuscript", "newbie",
            "ostracism", "phimosis", "quartile", "raspberry", "snowflake", "thunderbolt", "umbrella",
            "volunteer", "worthless", "xylophone", "yogurt", "zambian" ] )
    
    def get_word(self):
        """Gets a Word from the words list

        Args:
            self (Word): An instance of Word.
        
        Returns:
            string: A word to be used as a Puzzle
        """
        self._word = self._list_of_words[ random.randint(0, 25) ]
        return self._word

