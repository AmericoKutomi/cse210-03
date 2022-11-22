# Jumper
from terminal_service import TerminalService

class Jumper:
    """The person and his parachute
    
    The responsibility of the Jumper is represent itself and its parachute, and to take off some part of parachute when asked to do it
    
    Attributes:
        parachute (list[string]): The parachute is represented by a list of parts, and also with the image of the jumper
        terminal_service: For getting and displaying information on the terminal.    
    """
    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._parachute = ([ 
            '  ___  ',        
            ' /___\ ',        
            ' \   / ',        
            '  \ /  ',        
            '   O   ',        
            '  /|\  ',        
            '  / \  ',
            '       ',
            '^^^^^^^'     ])
        self._terminal_service = TerminalService()
       
    def draw_parachute(self):
        """Draws the parachute.
        """
        for parachute_item in self._parachute:
            self._terminal_service.write_text(f'{parachute_item}')
        self._terminal_service.write_text('')

    def cut_line(self):
        """ The most high part of the parachute is removed.
            If all the parachute is gone, the head is changed from O to X

        Args:
            self (Jumper): An instance of Jumper.
        """
        if len(self._parachute) >= 6:
            self._parachute.pop(0)
        if len(self._parachute) == 5:
            self._parachute[0] = '   X   '

    def has_parachute(self):
        """Return if the parachute still exists

        """
        return len(self._parachute) >= 6
