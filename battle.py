from character import Character

class Battle: 
    """Represents a turn-based battle between two characters in the RPG"""
    
    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Initialize the Battle

        Args:
            hero (Character): the hero character of the battle
            enemy (Character): the enemy character of the battle
        """
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """
        Play a single round, where hero attacks enemy, and if enemy is 
        still alive, enemy attacks hero
        """
        
        # Hero attacks enemy
        self.hero.attack(self.enemy)
        
        # Check if enemy is still alive
        if self.enemy.is_alive:
            # Enemy attacks hero
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """Simulate battle until one character is defeated"""
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()