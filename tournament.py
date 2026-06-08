#!/usr/bin/env python3


from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy, DefensiveStrategy


def ft_battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    for fighter in opponents:
        pass
            

def ft_tournament() -> None:

    fcf = FlameFactory()
    acf = AquaFactory()
    hcf = HealingCreatureFactory()
    tcf = TransformCreatureFactory()

    nos = NormalStrategy()
    ags = AggressiveStrategy()
    dfs = DefensiveStrategy()

    print("Tournament 0 (basic)")
    ft_battle([(fcf, nos), (hcf, dfs)])
    print("")

    print("Tournament 1 (error)")
    
    print("")

    print("Tournament 2 (multiple)")
    
    print("")

if __name__ == "__main__":
    ft_tournament()
