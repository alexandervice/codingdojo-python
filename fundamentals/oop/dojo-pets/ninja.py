import pet

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet_name ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet_name = pet_name
    
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet_name.play()
        if isinstance(self.pet_name, pet.Doggo):
            self.pet_name.goodboy()
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        if self.pet_food[0] > 0:
            print(f"{self.first_name} gave {self.pet_name.name} the {self.pet_food[1]}")
            self.pet_name.eat()
            self.pet_food[0] -= 1
            return self
        if self.treats[0] > 0:
            print(f"{self.first_name} gave {self.pet_name.name} the {self.treats[1]}")
            self.pet_name.eat()
            self.treats[0] -=1
            return self
        print(f"Oh no, you are out of pet food and treats!")
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet_name.noise()
        return self

alex = Ninja("Alex", "Vice", [2, "cheese"], [1,"dog food"], pet.toaster)

alex.walk().feed().feed().feed().feed().bathe()