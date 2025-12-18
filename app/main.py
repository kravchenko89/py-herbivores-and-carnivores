# write your code here
class Animal:
    alive = []
    def __init__(self, name: str) -> str:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return (f"Name: {self.name}, health: {self.health}, "
                f"hidden: {self.hidden}")

    def die(self):
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Сarnivore(Animal):
    def bite(self, other:str) -> None:
        if not isinstance(other, Herbivore):
            return

        if other.hidden or other.health <= 0:
            return

        other.health -= 50

        if other.health <= 0:
            other.health = 0
            other.die()