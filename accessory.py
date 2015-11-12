class Accessory:
	def __init__(self, name, def_bonus, health_bonus):
		self.name = name
		self.def_bonus = def_bonus
		self.health_bonus = health_bonus

	def accessory_description(self):
		print(self.name, self.def_bonus, self.health_bonus)

buckler= Accessory("Worn Buckler Shield", 1, 10)
heater = Accessory("Templar Heater Shield", 3, 20)
kite = Accessory("Red Kite Shield", 5, 30)
mystic= Accessory("Mystic Knight's Shield", 7, 50)

buckler.accessory_description()
print()
heater.accessory_description()
print()
kite.accessory_description()
print()
mystic.accessory_description()