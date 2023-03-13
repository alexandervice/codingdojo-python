import random

class Ninja:
    shuriken = []
    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        Ninja.shuriken.append(1)
        if Ninja.super_move():
            for stars in range(len(Ninja.shuriken)):
                pirate.health -= self.speed*Ninja.shuriken[stars]
        else:
            pirate.health -= self.strength
        return self
    
    @staticmethod
    def super_move():
        attack_type = random.randint(0,1)
        if attack_type == 1:
            return True
        else:
            return False
