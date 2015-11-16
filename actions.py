import player

class Action:
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name - name
        self.kwargs = kwargs
    
    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)
    
    def MoveUp(Action):
        def __init__(self):
            super().__init__(method=Player.move_up, name="Move up", hotkey="[U]")

    def MoveDown(Action):
        def __init__(self):
            super().__init__(method=Player.move_down, name="Move down", hotkey="d")

    def MoveLeft(Action):
        def __init__(self):
            super().__init__(method=Player.move_left, name="Move left", hotkey="l")

    def MoveRight(Action):
        def __init__(self):
            super().__init__(method=Player.move_right, name="Move right", hotkey="r")

    def ViewInventory(Action):
        def __init__(self):
            super().__init__(method=Player.print_inventory, name="View Inventory", hotkey="i")

    def Attack(Action):
        def __init__(self, enemy):
            super().__init__(method=Player.attack, name="Attack", hotkey="a", enemy= enemy)