from character import Character
from items import Weapon

class Mage(Character):
    """
    Represents a mage character in the RPG
    A mage is a subclass of Character with additional attribute mana and mana_max,
    as well as a modified attack method that uses mana to cast spells 
    """

    def __init__(
        self, name: str, 
        hp_max: int = 100, 
        damage: int = 10, 
        weapon: Weapon = None, 
        mana: int = 30,
        mana_max: int = 30
        ) -> None:
        """
        Initialise the Mage character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (class): Character's weapon (default = None)
            mana (int): Current mana points (default = 30)
            mana_max (int): Max mana points (default = 30)
        """
        super().__init__(name, hp_max, damage, weapon)
        self.mana = mana
        self.mana_max = mana_max
        
    def attack(self, target) -> None:
            """
            Attack and deal damage to target character. Use mana points to cast 
            spells dealing double damage, if enough points. Otherwise,
            perform base attack. 
            """
            if self.mana >= 10: # Check if mage has enough mana to cast a spell
                damage = self.damage * 2 # Double the damage
                self.mana -= 10
            else: # Not enough mana, perform base attack, with weapon if available   
                if self.weapon is not None:
                    damage = self.weapon.roll_damage()
                else:
                    damage = self.damage
                min(self.mana + 5, self.mana_max) # Restore 5 mana, but not above max

            # Deal damage to target
            target.take_damage(damage)