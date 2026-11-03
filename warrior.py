from character import Character
from items import Weapon

class Warrior(Character):
    """
    Represents a warrior character in the RPG
    A warrior is a subclass of Character with additional attribute armor and 
    modified take_damage method that reduces damage by armor
    """

    def __init__(
        self, name: str, 
        hp_max: int = 100, 
        damage: int = 10, 
        weapon: Weapon = None, 
        armor: int = 5
        ) -> None:
        """
        Initialise the Warrior character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (class): Character's weapon (default = None)
            armor (int): Armor rating (default = 5)
        """
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor
        
    def take_damage(self, damage: int) -> None:
            """Reduce own HP by damage, but not below 0. Reduce damage by armor"""
            reduced_damage = max(damage - self.armor, 0)
            self._hp -= reduced_damage
            self._hp = max(self._hp, 0)