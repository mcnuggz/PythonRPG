import dungeon, items
import random

class Player:
    def __init__(self):
        self.inventory= [items.AgedSword(), items.LeatherArmor(), items.Buckler()]
        self.health = 100
        self.base_attack = 2
        self.base_defense = 2
        self.location_x, self.location_y = dungeon.starting_position
        self.victory = False
        self.death = False

    def is_alive(self):
        return self.health > 0

    def show_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(dungeon.room_exists(self.location_x, self.location_y).intro_text())

    def move_up(self):
        self.move(dx= 0, dy= -1)

    def move_down(self):
        self.move(dx= 0, dy= 1)

    def move_left(self):
        self.move(dx= -1, dy= 0)

    def move_right(self):
        self.move(dx= 1, dy= 0)

    def attack(self, enemy):
        best_weapon = None
        max_damage = 0
        for item in self.inventory:
            if isinstance(item, items.Weapons):
                if item.attack > max_damage:
                    max_damage = item.attack
                    best_weapon = item

        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.health -= best_weapon.attack
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.health))

    def do_action(self, action, **kwargs):
    	action_method= getattr(self, action.method.__name__)
    	if action_method:
    		action_method(**kwargs)

    def flee(self, room):
        available_moves= rooml.adjacent_moves()
        r = random.randint(0, len(available_moves) -1)
        self.do_action(available_moves[r])