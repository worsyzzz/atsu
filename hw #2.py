import random
class Heroes:
    def  __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        self.hp += 100
        return f"Hp plus 100"
    def attack(self):
        return f"{self.name} attack someone"

class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name,hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows < 1 :
            return "У вас недостаточно стрел"
        self.arrows -= 1
        if random.randint(1,100) < self.precision:
            return  f"{self.name} попал в цель"
        else:
            return f"{self.name} не попал"

    def rest(self):
        self.arrows += 5
        return f"Колличество стрел увеличилось до {self.arrows}"

    def status(self):
        return f"Имя: {self.name}\n Здоровье: {self.hp}, Колличество стрел: {self.arrows}, Точность:{self.precision}"



archer1 = Archer("Max", 200, 15, 80)
print(archer1.attack())
print(archer1.rest())
print(archer1.status())

print(archer1.action)