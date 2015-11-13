import weapons
import armor
import accessory

class Inventory:
    player_equipment = {
    "Weapon:":weapons.aged_Sword.name, 
    "Armor:":armor.leather_armor.name,
    "Accessory:":accessory.buckler.name
    }
    
inventory = Inventory()
