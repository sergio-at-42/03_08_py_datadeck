from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(self, creature_name: str, creature_type: str) -> None:
        self.name: str = creature_name
        self.type: str = creature_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def concrete(self) -> str:
        return (f"{self.name} is a {self.type} type Creature")


class Flameling(Creature):

    def attack(self) -> str:
        return (f"{self.name} uses Ember!")


class Pyrodon(Creature):

    def attack(self) -> str:
        return (f"{self.name} uses Flamethrower!")


class Aquabub(Creature):

    def attack(self) -> str:
        return (f"{self.name} uses Water Gun!")


class Torragon(Creature):

    def attack(self) -> str:
        return (f"{self.name} uses Hydro Pump!")
