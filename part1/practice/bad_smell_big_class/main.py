# Воин в состоянии защищаться от врагов, атаковать и передвигаться по полю
class Warrior:
    def attack(self):
        pass

    def defense(self):
        pass

    def move(self):
        pass

# Лекарь может защищаться, лечить воина и панически спасаться бегством
class Healer:
    def defense(self):
        pass

    def move(self):
        pass

    def heal(self):
        pass

# Дерево может защищаться (попробуй разруби сходу) и гореть в огне
class Tree:
    def defense(self):
        pass

    def on_fire(self):
        pass

# Ловушка не может ничего кроме как атаковать того, кто на нее наступит
class Trap:
    def attack(self):
        pass

if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()