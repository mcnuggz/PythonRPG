class Armor:
	def __init__(self, def_rating, bonus_health):
		self.def_rating = def_rating
		self.bonus_health = bonus_health

leather_armor = Armor(2, 50)
chainmail = Armor(7, 60)
bulwark = Armor(12, 80)
mystic = Armor(18, 120)