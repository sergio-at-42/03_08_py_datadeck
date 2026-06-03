from ex0.Creature import Creature
from abc import ABC, abstractmethod


class HealCapability(ABC):

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):

    state: str = ""

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):

    def attack(self) -> str:
        return (f"{self.name} uses Vine Whip!")

    def heal(self) -> str:
        return (f"{self.name} heals itself for a small amount")


class Bloomelle(Creature, HealCapability):

    def attack(self) -> str:
        return (f"{self.name} uses Petal Dance!")

    def heal(self) -> str:
        return (f"{self.name} heals itself and others for a large amount")


class Shiftling(Creature, TransformCapability):

    def attack(self) -> str:
        return (f"{self.name} {self.state}")

    def transform(self) -> str:
        self.state = "performs a boosted strike!"
        return (f"{self.name} shifts into a sharper form!")

    def revert(self) -> str:
        self.state = "attacks normally."
        return (f"{self.name} returns to normal.")


class Morphagon(Creature, TransformCapability):

    def attack(self) -> str:
        return (f"{self.name} {self.state}")

    def transform(self) -> str:
        self.state = "unleashes a devastating morph strike!"
        return (f"{self.name} morphs into a dragonic battle form!")

    def revert(self) -> str:
        self.state = "attacks normally."
        return (f"{self.name} stabilizes its form.")
