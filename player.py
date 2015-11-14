import items

class Player():
	def __init__(self):
		self.inventory= [items.AgedSword(), items.LeatherArmor(), items.Buckler(), items.Potions(0)]
		self.maxhealth = self.health + items.Armor.bonus_health + items.Armor.extra_health
		self.health = 100
		self.location_x, self.location_y = dungeon.starting_position
		self.victory = False

	def is_alive(self):
		return self.health > 0

	def show_inventory(self):
		for item in self.inventory:
			print(item, '\n')