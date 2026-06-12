from abc import ABC, abstractmethod
from typing import Any
from ex0.Creature import Creature
from ex1.capability import HealCapability, TransformCapability


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Any) -> None:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature):
            return (True)
        return (False)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
        else:
            raise NotCreatureError(creature)


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Any) -> bool:
        if isinstance(creature, TransformCapability):
            return (True)
        return (False)

    def act(self, creature: Any) -> None:
        if (self.is_valid(creature)):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise NotTransformCreatureError(creature)


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Any) -> bool:
        if isinstance(creature, HealCapability):
            return (True)
        return (False)

    def act(self, creature: Any) -> None:
        if (self.is_valid(creature)):
            print(creature.attack())
            print(creature.heal())
        else:
            raise NotHealingCreatureError(creature)


class CreatureError(Exception):
    """Base class for creature errors."""


class NotCreatureError(CreatureError):
    """Base class for creature errors."""
    def __init__(self, creature: Creature) -> None:
        super().__init__(f"Invalid Creature ’{type(creature).__name__}’ " +
                         "for this normal strategy")


class NotTransformCreatureError(CreatureError):
    """Base class for creature errors."""
    def __init__(self, creature: Creature) -> None:
        super().__init__(f"Invalid Creature ’{type(creature).__name__}’ " +
                         "for this aggressive strategy")


class NotHealingCreatureError(CreatureError):
    """Base class for creature errors."""
    def __init__(self, creature: Creature) -> None:
        super().__init__(f"Invalid Creature ’{type(creature).__name__}’ " +
                         "for this healing strategy")
