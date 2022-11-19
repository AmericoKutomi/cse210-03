# Jumper

class Parachute:
    """The person and his parachute
    
    The responsibility of the parachute is represent itself used by a jumper and take off some part when asked to do it
    
    Attributes:
        parachute (list[string]): The parachute is represented by a list of parts, and also with the image of the jumper
        guesses (List[string]): The letters already guessed by the Jumper

    """
    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Seeker): An instance of Seeker.
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
        self._lives = 4    
        self._guesses = []
       
    def get_parachute(self):
        """Gets the parachute.
        
        Returns:
            list: The parachute or whats has been left
        """
        return self._parachute

    def cut_line(self):
        """ The most high part of the parachute is removed.

        Args:
            self (Seeker): An instance of Seeker.
        """
        if self._lives > 0:
            self._parachute.pop(0)
            self._lives -= 1
        if self._lives == 0:
            self._parachute[0] = '   X   '
        
        return self._lives > 0

    def add_letter(self, letter):
        """Moves to the given location.

        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """
        self._guesses += letter
