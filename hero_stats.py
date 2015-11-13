import weapons
import armor
import accessory 
import inventory

class HeroStats:
    def __init__(self, base_health, base_attack, base_defense):
        self.base_health = base_health
        self.base_attack = base_attack
        self.base_defense = base_defense

    def display_hero_stats(self):
        print("HP:", self.base_health)
        print("Attack:", self.base_attack)
        print("Defense:", self.base_defense)
        

    def increase_defense(self):
        ask_player_armor= input("Would you like to change your armor? (Yes or No) ")
        if ask_player_armor == "yes":
            print()
            for item in armor.Armor.armor_backpack:
                select_armor = input("Type in which armor you would like to equip:\n {0}".format(armor.Armor.armor_backpack))
                if select_armor == "Sturdy Leather Armor":
                    self.base_defense = self.base_defense + armor.leather_armor.def_rating
                if select_armor == "Squire's Chain Mail":
                    self.base_defense = self.base_defense + armor.chainmail.def_rating
                if select_armor == "Knight of the Bulwark's Armor":
                    self.base_defense = self.base_defense + armor.bulwark.def_rating
                if select_armor == "Mystic Armor":
                    self.base_defense = self.base_defense + armor.mystic.def_rating
                if select_armor == inventory.Inventory.list(player_equipment.value()[1])


ryan = HeroStats(100, 2, 2)
ryan.increase_defense()