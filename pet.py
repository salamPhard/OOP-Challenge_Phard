class Pet():
    def __init__(self, name, hunger, energy, happiness):
        self.name = name
        self.hunger = hunger #0 (full) to 10 (very hungry)
        self.energy = energy # 0 (tired) to 10 (fully rested)
        self.happiness = happiness #0 to 10
        self.tricks = []

    def eat(self, hunger, happiness):
        #Hunger is reduced by 3 but not below 0
        self.hunger = max(0, self.hunger - 3)
        #Happiness is increased by 1
        self.happiness = min(10, self.happiness + 1)

    def sleep(self, energy):
        self.energy = min(10, self.energy + 5) #energy is increased by 5 but not above 10

    def play(self, energy, happiness, hunger):
        self.energy = max(10, self.energy - 2) #energy is decreased by 2
        self.happiness = min(10, self.happiness + 2) #happiness is increased by 2
        self.hunger = min(10, self.hunger + 1) #hunger is increased by 1

    def get_status(self):
        print(f" {self.name}'s status are:")
        print(f" Hunger : {self.hunger}/10")
        print(f" Energy : {self.energy}/10")
        print(f" Happiness : {self.happiness}/10")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} has gotten a new trick called {trick}")
        else:
            print(f"{self.name} already has the added trick")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} has learned the listed tricks: {','.join(self.tricks)}")
        else:
            print(f"{self.name} has not learned any trick")

    def __str__(self):
        return f"{self.name} | Hunger: {self.hunger} | Energy: {self.energy} | Happiness: {self.happiness}"

