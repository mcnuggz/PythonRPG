class Accessory:
    accessory_backpack = []

    def __init__(self, name, def_bonus, health_bonus):
        self.name = name
        self.def_bonus = def_bonus
        self.health_bonus = health_bonus
        
    def add_to_backpack(self):
        self.accessory_backpack.append(self.name)

    def accessory_description(self):
        print(self.name, self.def_bonus, self.health_bonus)
    

buckler= Accessory("Worn Buckler Shield", 1, 10)
heater = Accessory("Templar Heater Shield", 3, 20)
kite = Accessory("Red Kite Shield", 5, 30)
mystic= Accessory("Mystic Knight's Shield", 7, 50)

buckler.add_to_backpack()
heater.add_to_backpack()
kite.add_to_backpack()
mystic.add_to_backpack()