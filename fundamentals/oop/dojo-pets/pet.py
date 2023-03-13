import random

class Pet:
    def  __init__(self, name, type, tricks=["sit", "come"], health=10, energy=25, sound="rawr"):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f"{self.name} took a nap. Energy restored by 25")
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} ate all the food. Energy restored by 5, Health restored by 10")
        return self
    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f"{self.name} had lots of fun playing! Health restored by 5")
        return self
    # noise() - prints out the pet's sound
    def noise(self):
        print(f"{self.name} says '{self.sound}'")
        return self

class Doggo(Pet):
    def __init__(self, name, type, tricks=["sit", "come", "roll over", "shake", "hugs"], health=20, energy=50, sound="woof", emotion="happy"):
        super().__init__(name, type, tricks, health, energy, sound)
        self.emotion = emotion
    def goodboy(self):
        trick = random.randint(0,len(self.tricks)-1)
        print(f"{self.name} showed off the trick: {self.tricks[trick]}")

toaster = Doggo("Toaster","dog")

# print(isinstance(toaster, Doggo))