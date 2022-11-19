from terminal_service import TerminalService
from word import Word
from parachute import Parachute
from hint import Hint


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        parachute (Parachute): The game's jumper with its parachute
        word (Word): The game's puzzle that is a word
        hint (Hint): The hint to be given to the jumper according to his guesses
        last_letter: The last letter the jumper guessed
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._parachute = Parachute()
        self._word = Word()
        self._hint = Hint(self._word.get_word())
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
        self._parachute.add_letter(self._last_letter)
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        if not self._hint.watch_letter(self._last_letter):
            if not self._parachute.cut_line():
                self._is_playing = False
                self._show_hint()
                self._show_parachute()
                self._terminal_service.write_text('I am sorry, you did not find the puzzle.')
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        if not self._is_playing:
            return

        self._show_hint()
        self._show_parachute()

        if self._hint.is_found():
            self._terminal_service.write_text('Congratulations, you have found the puzzle.')
            self._is_playing = False

    def _show_hint(self):
        hint = self._hint.get_hint()
        complete_text = ''
        for n in range(len(hint)):
            complete_text += hint[n] + ' '
        self._terminal_service.write_text(f'\n{complete_text}\n')

    def _show_parachute(self):
        parachute = self._parachute.get_parachute()
        for parachute_item in parachute:
            self._terminal_service.write_text(f'{parachute_item}')
        self._terminal_service.write_text('')
