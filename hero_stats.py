class HeroStats:
    def __init__(self, base_health, base_attack, base_defense):
        self.base_health = base_health
        self.base_attack = base_attack
        self.base_defense = base_defense

    def display_hero_stats(self):
        print("HP:", self.base_health)
        print("Attack:", self.base_attack)
        print("Defense:", self.base_defense)

    # def increase_attack(self):

ryan = HeroStats(100, 2, 2)
ryan.display_hero_stats()