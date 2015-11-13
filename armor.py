class Armor:
    armor_backpack = []

    def __init__(self, name, def_rating, bonus_health):
        self.name = name
        self.def_rating = def_rating
        self.bonus_health = bonus_health

    def add_to_backpack(self):
        self.armor_backpack.append(self.name)

    def armor_description(self):
        print(self.name)


leather_armor = Armor("Sturdy Leather Armor", 2, 50)
chainmail = Armor("Squire's Chain Mail", 7, 60)
bulwark = Armor("Knight of the Bulwark's Armor", 12, 80)
mystic = Armor("Mystic Knight's Armor", 18, 120)

leather_armor.add_to_backpack()
chainmail.add_to_backpack()
bulwark.add_to_backpack()
mystic.add_to_backpack()