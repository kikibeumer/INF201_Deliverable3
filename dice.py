import random 

class Dice:
    """Represents a die in the RPG"""

    def __init__(self, sides: int = 6) -> None:
        """
        Initialise the dice 

        Args:
            sides(int): number of sides on the dice.

        """
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides.")
        self.sides = sides

    def roll(self) -> int:
        """Roll the dice and return a random values between 1 and the number of sides"""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Representation of dice object"""
        return f"Dice(sides={self.sides})"

    def __call__(self) -> None:
        """
        Called when the instance is “called” as a function; 
        When rolling the dice, instead of writing Dice(20).roll(), Dice(20) calls __call__ and rolls the dice.
        """
        return self.roll()
        
