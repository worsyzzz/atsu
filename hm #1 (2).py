class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.hp}")

    def is_adult(self):
        return self.lvl >= 10


hero1 = Hero("Артур", 10, 100)
hero2 = Hero("Леон", 5, 80)
hero3 = Hero("София", 12, 120)

print(f"{hero1.name} взрослый? {hero1.is_adult()}")
print(f"{hero2.name} взрослый? {hero2.is_adult()}")
print(f"{hero3.name} взрослый? {hero3.is_adult()}")
