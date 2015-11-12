class Armor:
	def __init__(self, name, def_rating, bonus_health):
		self.name = name
		self.def_rating = def_rating
		self.bonus_health = bonus_health

	def armor_description(self):
		print(self.name, self.def_rating, self.bonus_health)

leather_armor = Armor("Sturdy Leather Armor", 2, 50)
chainmail = Armor("Squire's Chain Mail", 7, 60)
bulwark = Armor("Knight of the Bulwark's Armor", 12, 80)
mystic = Armor("Mystic Knight's Armor", 18, 120)

leather_armor.armor_description()
chainmail.armor_description()
bulwark.armor_description()
mystic.armor_description()