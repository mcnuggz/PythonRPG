import items

class Enemies:
	def __init__(self, name, health, attack, defense):
		self.name = name
		self.health = health
		self.attack = attack
		self.defense = defense

	def is_alive(self):
		return self.health > 0

class Skeleton(Enemies):
	def __init__(self):
		super().__init__(name="Risen Skeleton", health= 50, attack = 4, defense= 2)

class Goblin(Enemies):
	def __init__(self):
		super().__init__(name="Frienzied Goblin", health= 120, attack= 5, defense= 3)

class Sorcerer(Enemies):
	def __init__(self):
		super().__init__(name="Twisted Sorcerer", health= 170, attack= 10, defense= 7)

class Ogre(Enemies):
	def __init__(self):
		super().__init__(name="Jailer Ogre", health= 220, attack= 15, defense= 13)

class Behemoth(Enemies):
	def __init__(self):
		super().__init__(name="Doomfang, the Enraged Behemoth", health= 250, attack= 18, defense= 18)