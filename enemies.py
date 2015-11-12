class Enemy:
	def __init__(self, name, health, attack, defense):
		self.name = name
		self.health = health
		self.attack = attack
		self.defense = defense

	def enemy_info(self):
		print("Enemy Name:", self.name)
		print("Enemy HP:", self.health)
		print("Enemy Attack:", self.attack)
		print("Enemy Defense:", self.defense)

skeleton = Enemy("Risen Skeleton", 50, 4, 2)
goblin = Enemy("Frienzied Goblin", 120, 5, 3)
sorceror = Enemy("Twisted Sorceror", 170, 10, 6)
behemoth = Enemy("Doomfang, the Enraged Behemoth", 250, 18, 18)
print()
skeleton.enemy_info()
print()
goblin.enemy_info()
print()
sorceror.enemy_info()
print()
behemoth.enemy_info()