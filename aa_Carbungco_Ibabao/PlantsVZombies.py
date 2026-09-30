class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    def attack(self, zombie):
        print(f"\n{self.name} attacks {zombie.name} for {self.damage} damage")
        zombie.take_damage(self.damage)
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
        print(f"\n{self.name} took {amount} damage. Health left: {self.health}")

class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance
    def move(self):
        if self.distance > 0:
            self.distance -= 1
        print(f"\n{self.name} walked closer. Distance now: {self.distance}")
    def attack(self, plant):
        print(f"\n{self.name} attacks {plant.name} for {self.damage} damage")
        plant.take_damage(self.damage)
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
        print(f"\n{self.name} took {amount} damage. Health left: {self.health}")

def play_game():
    plant1 = Plant("Squash",75,15)
    plant2 = Plant("Chili",65,20)
    zombie = Zombie("Dr. Zomboss",150,30,3)
    plants = {plant1, plant2}
    turn = 1
    while True:
        print(f"\n--- Turn {turn} ---")
        for plant in plants:
            if plant.health > 0:
                plant.attack(zombie)
                if zombie.health <= 0:
                    print(f"\n{zombie.name} died! Plants win!")
                    return
        if zombie.distance > 0:
            zombie.move()
        else:
            target = target = next((p for p in plants if p.health > 0), None)
            if target:
                zombie.attack(target)
        if all(p.health <= 0 for p in plants):
            print(f"\nBoth plants are down! {zombie.name} wins!")
            return
        print(f"\nEnd of turn {turn}")
        for p in plants:
            print(f"\n{p.name} Health: {p.health}")
        print(f"\n{zombie.name} Health: {zombie.health}")
        turn += 1

if __name__ == "__main__":
    play_game()
