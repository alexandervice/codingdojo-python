import random

class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        if Pirate.super_move():
            self.health += 15
            self.speed += 1
            self.strength += 5
        else:
            ninja.health -= self.strength
        return self
    
    @staticmethod
    def super_move():
        attack_type = random.randint(0,1)
        if attack_type == 1:
            return True
        else: 
            return False
