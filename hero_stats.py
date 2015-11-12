class HeroStats:
	def __init__(self, base_health, base_attack, base_defense):
		self.base_health = base_health
		self.base_attack = base_attack
		self.base_defense = base_defense

	def display_hero_stats(self):
		print("HP:", self.base_health)
		print("Attack:", self.base_attack)
		print("Defense:", self.base_defense)

test = HeroStats(100, 3, 2)
test.display_hero_stats()