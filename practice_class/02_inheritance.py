class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    
    # methods
    def attack(self, amount):
        print("The monster has attacked")
        print(f"{amount} damage was dealt")
        self.energy -= 20

    def move(self, speed):
        print("The monster has moved")
        print(f"It has a speed of {speed}")

class Shark(Monster):
    def __init__(self, speed, health, energy):
        # Monster.__init__(self, health, energy) # Don't use anymore
        super().__init__(health, energy)
        self.speed = speed

    def bite(self):
        print("The shark has bitten")

    def move(self):
        print("The shark has moved")
        print(f"The speed of the shark is {self.speed}")

class Scorpion(Monster):
    def __init__(self, scorpion_health, scorpion_energy, poison_dmg):
        super().__init__(health = scorpion_health, energy = scorpion_energy)
        self.poison_dmg = poison_dmg
    def attack(self):
        print("The scorpion has attacked")
        print(f"The scorpion has dealt {self.poison_dmg} poison dmg")

scorpion = Scorpion(scorpion_health=20, scorpion_energy=10, poison_dmg=50)
print(scorpion.health)