import random

#base class for items
class Item:
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def __init__(self):
		return "{}\n=====\n{}\nDamage: {}".format(self.name, self.description)

class Potion(Item):
	def __init__(self):
		super().__init__(name="Health Potion", description="A bottle of questionable color and taste. Fully restores your health")

#start weapons
class Weapons(Item):
    def __init__(self, name, attack, description):
        self.attack = attack
        super().__init__(name, description)

    def __str__(self):
    	return "{}\n=====\n{}\nDamage: {}".format(self.name, self.description, self.attack)

class AgedSword(Weapons):
	def __init__(self):
		super().__init__(name="Aged Sword", description="An old, rusted and chipped sword. You wonder how it hasn't completely snapped into two by now.", attack= 2)

class Longsword(Weapons):
	def __init__(self):
		super().__init__(name="Longsword", description="A gleaming longsword that was kept in good shape.", attack= 8)

class EnchantedLongsword(Weapons):
	def __init__(self):
		super().__init__(name="Enchanted Longsword", description="A prestine longsword you found with small runes inscribed along the Cross Guard. You feel a small magical force emanating from the weapon as you hold it.", attack = 12)

class MysticSword(Weapons):
	def __init__(self):
		super().__init__(name="Mystic Knight's Claymore", description= "A weapon of unknown power, the blade shines a soft hue of white.", attack= 15)

	def mystic_attack(self):
		chance_for_mystic = random.randint(1,5)
		if chance_for_mystic == 1:
		    mystic_attack = self.attack * 2

class Armor(Item):
	def __init__(self, name, description, defense, bonus_health):
		self.defense = defense
		self.bonus_health = bonus_health
		super().__init__(name, description)
