from abc import ABC, abstractmethod


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self) -> bool:
        return (True)

    @abstractmethod
    def act(self) -> None:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self) -> bool:
        return (True)

    def act(self) -> None:
        pass


class AggressiveStrategy(BattleStrategy):

    def is_valid(self) -> bool:
        return (True)

    def act(self) -> None:
        pass


class DefensiveStrategy(BattleStrategy):

    def is_valid(self) -> bool:
        return (True)

    def act(self) -> None:
        pass


class ActError(Exception):
    """Base class for act-related errors."""
    def __init__(self) -> None:
        super().__init__("Not enough water in tank")
