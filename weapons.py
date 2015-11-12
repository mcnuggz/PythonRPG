class Weapons:

	def __init__(self, name, attack):
		self.name = name
		self.attack = attack

	def weapon_description(self):
		print(self.name,",",self.attack)

	def mystic_attack(self):
		if mystic_sword == True:
			dbl_attack = attack * 2

agedSword = Weapons("Aged Sword", 3)
longsword = Weapons("Longsword", 8)
enchanted_sword = Weapons("Enchanted Longsword", 12)
mystic_sword = Weapons("Mystic Knight's Sword", 16)

agedSword.weapon_description()
longsword.weapon_description()
enchanted_sword.weapon_description()
mystic_sword.weapon_description()