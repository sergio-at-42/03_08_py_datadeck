from abc import ABC, abstractmethod
from ex0.Creature import Creature
from ex1.capability import HealCapability, TransformCapability


class BattleStrategy(ABC):
    
    @abstractmethod
    def is_valid(self) -> bool:
        pass

    @abstractmethod
    def act(self) -> None:
        pass


class NormalStrategy(BattleStrategy):

    def __init__(self, creature: Creature) -> None:
        self.creature: Creature = creature

    def is_valid(self) -> bool:
        return (True)

    def act(self) -> None:
        self.creature.attack()


class AggressiveStrategy(BattleStrategy):

    def is_valid(self) -> bool:
        if isinstance(self.creature, TransformCapability):
            return (True)
        return (False)

    def act(self) -> None:
        if (self.is_valid()):
            self.creature.transform()
            self.creature.attack()
            self.creature.revert()


class DefensiveStrategy(BattleStrategy):

    def __init__(self, creature: Creature, capability: HealCapability) -> None:
        self.creature: Creature = creature

    def is_valid(self) -> bool:
        if isinstance(self.creature, HealCapability):
            return (True)
        return (False)

    def act(self) -> None:
        if (self.is_valid()):
            self.creature.attack()
            HealCapability.heal()


class ActError(Exception):
    """Base class for act-related errors."""
    def __init__(self) -> None:
        super().__init__("Not enough water in tank")
