from abc import ABC, abstractmethod
from typing import Any
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
        if isinstance(self.creature, Creature):
            return (True)
        return (False)

    def act(self) -> None:
        if self.is_valid():
            self.creature.attack()
        else:
            raise NotCreatureError


class AggressiveStrategy(BattleStrategy):

    def __init__(self, creature: Any) -> None:
        self.creature: Any = creature

    def is_valid(self) -> bool:
        if isinstance(self.creature, TransformCapability):
            return (True)
        return (False)

    def act(self) -> None:
        if (self.is_valid()):
            self.creature.transform()
            self.creature.attack()
            self.creature.revert()
        else:
            raise NotTransformCreatureError


class DefensiveStrategy(BattleStrategy):

    def __init__(self, creature: Any) -> None:
        self.creature: Any = creature

    def is_valid(self) -> bool:
        if isinstance(self.creature, HealCapability):
            return (True)
        return (False)

    def act(self) -> None:
        if (self.is_valid()):
            self.creature.attack()
            self.creature.heal()
        else:
            raise NotHealingCreatureError


class NotCreatureError(Exception):
    """Base class for act-related errors."""
    def __init__(self) -> None:
        super().__init__("Not a creature. Can't attack !!!")


class NotTransformCreatureError(Exception):
    """Base class for act-related errors."""
    def __init__(self) -> None:
        super().__init__("Not a transform creature. Can't transform before attack !!!")


class NotHealingCreatureError(Exception):
    """Base class for act-related errors."""
    def __init__(self) -> None:
        super().__init__("Not a healing creature. Can't heal after attack !!!")
