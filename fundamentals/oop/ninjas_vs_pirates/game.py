from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)

jack_sparrow.show_stats()


def battle_game():
    if michelangelo.speed > jack_sparrow.speed:
        michelangelo.attack(jack_sparrow)
        if jack_sparrow.health <= 0:
            print(f"Jack Sparrow is dead, Michelangelo wins!!")
            return False
        jack_sparrow.attack(michelangelo)
        if michelangelo.health <= 0:
            print(f"Michelangelo is dead, Jack Sparrow wins!!")
            return False
        jack_sparrow.show_stats()
        # print("")
        michelangelo.show_stats()
        return True
    else:
        jack_sparrow.attack(michelangelo)
        if michelangelo.health <= 0:
            print(f"Michelangelo is dead, Jack Sparrow wins!!")
            return False
        michelangelo.attack(jack_sparrow)
        if jack_sparrow.health <= 0:
            print(f"Jack Sparrow is dead, Michelangelo wins!!")
            return False
        jack_sparrow.show_stats()
        # print("")
        michelangelo.show_stats()
        return True


alive = True
while alive == True:
    alive = battle_game()