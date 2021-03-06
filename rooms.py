import items, enemies, dungeon, player, actions
from time import sleep

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        moves = []
        if dungeon.room_exists(self.x + 1, self.y):
            moves.append(actions.MoveRight())
        if dungeon.room_exists(self.x - 1, self.y):
            moves.append(actions.MoveLeft())
        if dungeon.room_exists(self.x, self.y - 1):
            moves.append(actions.MoveUp())
        if dungeon.room_exists(self.x, self.y + 1):
            moves.append(actions.MoveDown())
        return moves

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        return moves
        
class StartingRoom(Tile):
    def intro_text(self):
        return """
    Deep below the streets of a bustling city, an aniquated prison was shaken awake from a mysterious force. You, hero, are a cadet  in the citys' guard; tasked with the mission of investigating why the Earth shakes beneath the city.  You were provided with  leather armor and an old sword and instructed about your mission and added that if the reasons are not natural, call for  reinforcements and fall back. However, you only see that as a chance to prove yourself as a capable person, in hopes to  becoming a Royal Guard. You steel yourself and enter the dark, cryptic entrance to the undercity.
        """
    def modify_player(self, player):
        #Nothing happens in this room
        pass

class GainLoot(Tile):
    def __init__(self, x, y, item1, item2, item3):
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        super().__init__(x,y)

    def add_loot(self, player):
        player.inventory.append(self.item, self.item2, self.item3)

    def modify_player(self, player):
        self.add_loot(player)
        player.update_attack()
        player.update_defense()
        player.update_health()

class FindTier2Room(GainLoot):
    def __init__(self, x, y):
        super().__init__(x, y, items.Longsword(), items.Heater(), items.Chainmail())

    def intro_text(self):
        return"""
        You enter what appears to be a kitchen. You look around the room finding a Longsword, a Heater shield and a Hauberk off the corpse of a warrior with a cleaver stuck through its skull!
        """
class FindTier3Room(GainLoot):
    def __init__(self, x, y):
        super().__init__(x, y, items.Enchanted(), items.Kite(), items.Bulwark())

    def intro_text(self):
        return"""
        You enter a room fitted with racks of weaponry and shelves of armor. After a thorough lookover, you find an Enchanted Longsword, a Kite Shield, and a set of armor from the fabled Knights of the Bulwark!
        """
class FindMysticRoom(GainLoot):
    def __init__(self, x, y):
        super().__init__(x, y, items.MysticSword(), items.MysitcArmor(), items.MysticShield())

    def intro_text(self):
        return"""
        The Ogre collapses onto the ground being defeated by your hand. You lean over to catch your breath after the long battle with the creature. Suddenly a bright purple light shines and disappears as quickly as it appears. In its spot sits an elegant chest. You slowly approach it, still reeling from the brightness from the mysterious light. Taking the lid into your hands, you throw open the chest to reveal the Mystic Knight armor set and sword!
        """

class BehemothDefeated(Tile):
    def intro_text(self):
        return"""
        It was a difficult battle, but you stand victorious. Battered, but victorious and not dead. The city stands safe from a greater danger that would have ended the city you have sworn to protect. You turn towards the heavy double doors and begin your leave from the now silent dungeon.

        Congratulations, you have won!
        """
    def modify_player(self, player):
        player.victory = True

class EnemyEncounter(Tile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, hero):
        if self.enemy.is_alive():
            hero.health = hero.health - self.enemy.attack
            print("The enemy does {} damage. You have {} HP remaining.".format(self.enemy.attack, hero.health))

    def available_actions(self):
        if self.enemy.is_alive():
            return[actions.Flee(room = self), actions.Attack(enemy = self.enemy)]
        else:
            return self.adjacent_moves()

class EmptyRoom(Tile):
    def intro_text(self):
        return"""
        An unremarkable room with nothing of value or intrigue that you can see. You press on with your quest.
        """
    def modify_player(self, player):
        #nothing happens
        pass

class SaunaRoom(Tile):
    def intro_text(self):
        return"""
        You enter a warm room, turning out to be a natural sauna. You remove your armor and weapon, taking a seat out of the sight of the entrance and relaxing for several minutes.
        """
    # def modify_player(self, player):
        #function to restore health

class DeathRoom(Tile):
    def intro_text(self):
        return"""
        You cautiously enter the room and see no immediate threat. Closing the door behind you, you take a step forward and activate a hidden switch. A thick arrow jets out from a hole in the wall in front of you and punctures through your neck. You collapse to the floor, holding your neck as dark blood pours out from the hole the arrow created. But alas, you accept your fate and perish in the dark dungeon.
        """

    def modify_player(self, player):
        player.death = True
        sleep(4)
        exit()

class SkeletonRoom(EnemyEncounter):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Skeleton())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
A pile of bones rattle and assemble into the shape of a human. Its eyes glow red and charges at you, sword raised!
            """
        else:
            return """
The bones of the fallen skeleton warrior lay on the ground with the skull shattered by the heel of your boot.
            """

class GoblinRoom(EnemyEncounter):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Goblin())

    def intro_text(self):
        if self.enemy.is_alive():
            return"""
A small human-like creature bursts out from corner of the room, its eyes showing signs of hysteria and menance as it stares at you. He lets out a loud cackle and lunges at you!
            """
        else:
            return """
The corpse of the goblin lays dead on the floor in a puddle of its own drool and blood.
            """

class SorcererRoom(EnemyEncounter):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Sorcerer())

    def intro_text(self):
        if self.enemy.is_alive():
            return"""
            You approach a room in the hallway with glowing green light emanating through the edges of the door. You slowly crack the door open seeing a thin man shouting an incantation in a foreign tongue that you do not recognize. The man becomes aware of your presence when the door you hide behind makes a loud creak. He turns to you, raising his hands up and two green orbs fill them as you kick the door open and draw out your weapon.
            """
        else:
            return"""
            Such a terrible waste of life, the man lays dead over a bed of open books and scrolls covered in his own blood.
            """

class OgreRoom(EnemyEncounter):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
            return"""
            You stumble through the portal, and right in front of a giant Ogre! He lets out an oddly childish laugh and raises his club and swings it downard. You managed to roll out of the way of the 
            """
        else:
            return"""
            The giant humanoid lays dead on the ground.
            """

class BehemothRoom(EnemyEncounter):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Behemoth())

    def intro_text(self):
        if self.enemy.is_alive():
            return"""
            You approach a set large of heavy wooden doors that are the size of a large house. A loud growl is heard along with what sounds like chains being dragged and tossed across the room. You have a feeling that once you enter that room, you may not come back out.
            """
            player_confirm= input("Are you sure you want to enter? y/n ")
            if player_confirm == "y":
                return """
                You exhale and press your hands against the set of doors, pushing it open and entering to find the cause of the quakes: a giant Behemoth. It spots you entering the room and growls loudly at you and hunches down, ready to pounce its next meal.
            """
            elif player_confirm == "n":
                return"""
                There's no shame in retreating. You fall back to the previous room for now.
                """
