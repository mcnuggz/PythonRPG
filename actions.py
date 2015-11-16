from player import Player

class Actions:
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs
    
    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)
    
class MoveUp(Actions):
    def __init__(self):
        super().__init__(method=Player.move_up, name="Move Up", hotkey="u")

class MoveDown(Actions):
    def __init__(self):
        super().__init__(method=Player.move_down, name="Move Down", hotkey="d")

class MoveLeft(Actions):
    def __init__(self):
        super().__init__(method=Player.move_left, name="Move Left", hotkey="l")

class MoveRight(Actions):
    def __init__(self):
        super().__init__(method=Player.move_right, name="Move Right", hotkey="r")

class ViewInventory(Actions):
    def __init__(self):
        super().__init__(method=Player.show_inventory, name="View Inventory", hotkey="i")

class Attack(Actions):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey="a", enemy= enemy)