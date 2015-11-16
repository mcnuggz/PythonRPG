import random
import player

#base class for items
class Item(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def __str__(self):
		return "{}\n=====\n{}".format(self.name, self.description)

#start weapons
class Weapons(Item):
    def __init__(self, name, description, attack):
        self.attack = attack
        super().__init__(name, description)

    def __str__(self):
    	return "{}\n=====\n{}\n Attack:{}".format(self.name, self.description, self.attack)

#warrior weapons
class AgedSword(Weapons):
	def __init__(self):
		super().__init__(name="Aged Sword", description="An old, rusted and chipped sword. You wonder how it hasn't completely snapped into two by now.", attack= 2)

class Longsword(Weapons):
	def __init__(self):
		super().__init__(name="Longsword", description="A gleaming longsword that was kept in good shape.", attack= 8)

class Enchanted(Weapons):
	def __init__(self):
		super().__init__(name="Enchanted Longsword", description="A prestine longsword you found with small runes inscribed along the Cross Guard. You feel a small magical force emanating from the weapon as you hold it.", attack = 12)

class MysticSword(Weapons):
	def __init__(self):
		super().__init__(name="Mystic Knight's Claymore", description= "A weapon of unknown power, the blade shines a soft hue of white.", attack= 15)

	def mystic_attack(self):
		chance_for_mystic = random.randint(1,5)
		if chance_for_mystic == 1:
		    mystic_attack = player.attack * 2

#start armor
class Armor(Item):
    def __init__(self, name, description, defense, bonus_health):
        self.defense = defense
        self.bonus_health = bonus_health
        super().__init__(name, description)
    
    def __str__(self):
        return "{}\n=====\n{}\n Defense:{}\n Bonus Health: {}".format(self.name, self.description, self.defense, self.bonus_health)

#warrior armor
class LeatherArmor(Armor):
	def __init__(self):
		super().__init__(name="Sturdy Leather Armor", description="Thick leather armor given to you at the start of your adventure.", defense= 2, bonus_health= 40)

class Chainmail(Armor):
	def __init__(self):
		super().__init__(name="Squire's Hauberk", description= "A shirt of chainmail that reaches down to your mid-thigh. Has plating on the left shoulder and right arm.", defense= 7, bonus_health= 60)
class Bulwark(Armor):
	def __init__(self):
		super().__init__(name="Knight of the Bulwark's Armor", description="The armor from the Bulwark's Order was famously known for its defensive capabilities, as well as its weight.", defense= 12, bonus_health= 80)
class MysticArmor(Armor):
	def __init__(self):
		super().__init__(name="Mystic Knight's Armor", description= "It appears like a standard set of Infantry armor, but you feel a comforting presence as you wear it.")

#start accessoriess
class Accessory(Item):
    def __init__(self, name, description, extra_defense, extra_health):
        self.extra_defense = extra_defense
        self.extra_health = extra_health
        super().__init__(name, description)
    
    def __str__(self):
    	return "{}\n=====\n{}\n Defense:{}\n Bonus Health: {}".format(self.name, self.description, self.extra_defense, self.extra_health)

#warrior accessories
class Buckler(Accessory):
	def __init__(self):
		super().__init__(name="Worn Buckler Shield", description="A small shield that was given to you at the start of your adventure.", extra_defense= 1, extra_health= 10)
class Heater(Accessory):
	def __init__(self):
		super().__init__(name="Templar's Heater Shield", description="A shield painted white with a red cross painted over it. It appears to have served its previous owner well as it has several scatches etched along its surface.", extra_defense= 3, extra_health= 20)
class Kite(Accessory):
	def __init__(self):
		super().__init__(name="Blue Kite Shield", description="A long shield, covering the length of your body when standing. Painted blue and gold, has several stratches on its surface. It is difficult to manuever around with it.", extra_defense= 5, extra_health= 30)
class MysticShield(Accessory):
	def __init__(self):
		super().__init__(name="Mystic Knight's Shield", description= "Looks like a standard metal buckler shield, however when it use a brilliant orange field extends out acting like a wall protecting its user.", extra_defense = 7, extra_health= 60)
