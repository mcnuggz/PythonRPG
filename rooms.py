import enemies

class Rooms:
    dungeon={
    "Hallway": enemies.skeleton,
    "Storeroom": enemies.goblin,
    "Hidden Laboratory": enemies.sorceror,
    "Portal to Guard Room": enemies.ogre,
    "Prison Chamber": enemies.behemoth
    }

    def __init__(self):
        self.currentRoom = list(self.dungeon.keys())[0]

    def show_location(self):
        print("You are in", self.currentRoom)

    def move_to_room(self):
        player_moves = input("Do you want to change rooms? Press [H] to move to the Hallway, [S] for the Storeroom, [L] for the Laboratory, [P] to the Prison Chamber! ")
        if player_moves == "H":
            self.currentRoom == list(self.dungeon.keys())[0]
            print("You have moved to the Hallway.")
        if player_moves == "S":
            self.currentRoom == list(self.dungeon.keys())[1]
            print("You have moved to the Storage Room")
        if player_moves == "L":
            self.currentRoom == list(self.dungeon.keys())[2]
            print("You have entered the Hidden Laboratory")
        if player_moves == "P":
            confirm_to_enter = input("You hear a loud, deep growl as you approach the door tot he Prison Chamber. You have a feeling that once you enter this room, you will not be able to leave unless you defeat whatever is inside. Are you sure you want to enter? Yes or No ")	   
            if confirm_to_enter == "Yes":
                print("\n You have entered the Prison Chamber. May the Gods keep you safe.")
                self.currentRoom == list(self.dungeon.keys())[3]
            elif confirm_to_enter == "No":
                self.currentRoom == list(self.dungeon.keys())[0]
                print("\n You decided to make a tactical retreat to the Hallway.")

room = Rooms()
room.move_to_room()