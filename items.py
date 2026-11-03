from dice import Dice

class Weapon:
    """Represents a weapon in the RPG"""
    
    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise the Weapon
    
        Args:
            name (str): The name of the weapon.
            damage_dice (class): Damage delt determined by the die.
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int: 
        """Roll the die to obtain the amount of damage. (.roll() is not required as we defined __call__)"""
        return self.damage_dice()

    

        
    