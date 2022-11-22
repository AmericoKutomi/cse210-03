from terminal_service import TerminalService
from puzzle import Puzzle
from jumper import Jumper

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        jumper (Jumper): The game's jumper with its parachute
        puzzle (Puzzle): The game's puzzle that is a word
        last_letter: The last letter the jumper guessed
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._jumper = Jumper()
        self._puzzle = Puzzle()
        self._last_letter = ''
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._do_outputs()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """ Gets the jumper's letter guess.

        Args:
            self (Director): An instance of Director.
        """
        self._last_letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        
    def _do_updates(self):
        """If the Jumper guesses incorrectly, it will be asked him to cut a line
            If the Jumper does not have a parachute anymore, the game is over

        Args:
            self (Director): An instance of Director.
        """
        if not self._puzzle.watch_letter(self._last_letter):
            self._jumper.cut_line()
            if not self._jumper.has_parachute():
                self._is_playing = False
                self._puzzle.draw_hint()
                self._jumper.draw_parachute()
                self._terminal_service.write_text('I am sorry, you did not find the puzzle.')
        
    def _do_outputs(self):
        """Provides a hint for the Jumper to use.

        Args:
            self (Director): An instance of Director.
        """
        if not self._is_playing:
            return

        self._puzzle.draw_hint()
        self._jumper.draw_parachute()

        if self._puzzle.is_found():
            self._terminal_service.write_text('Congratulations, you have found the puzzle.')
            self._is_playing = False


