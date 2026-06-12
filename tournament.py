#!/usr/bin/env python3


from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy, \
    DefensiveStrategy, CreatureError


def ft_battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    first: bool = True
    print("[ ", end="")
    for f, s in opponents:
        if not first:
            print(", ", end="")
        else:
            first = False
        print(f"({type(f.create_base()).__name__}", end="")
        print(f"+{type(s).__name__.removeprefix("Strategy")})", end="")
    print(" ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print("")
    # for (factory1, strategy1) in opponents[:-1]:
    for i in range(len(opponents) - 1):
        (factory1, strategy1) = opponents[i]
        fighter1 = factory1.create_base()
        # for (factory2, strategy2) in opponents[1:]:
        for j in range(i + 1, len(opponents)):
            (factory2, strategy2) = opponents[j]
            fighter2 = factory2.create_base()
            try:
                print("* Battle *")
                print(fighter1.concrete())
                print("vs.")
                print(fighter2.concrete())
                print("now fight!")
                strategy1.act(fighter1)
                strategy2.act(fighter2)
            except CreatureError as e:
                print("Battle error, aborting tournament:", end=" ")
                print(e)
            finally:
                print("")


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
    ft_battle([(fcf, ags), (hcf, dfs)])
    print("")

    print("Tournament 2 (multiple)")
    ft_battle([(acf, nos), (hcf, dfs), (tcf, ags)])
    print("")

    print("Tournament 3 (multiple + error)")
    ft_battle([(fcf, ags), (acf, nos), (hcf, dfs), (tcf, ags)])
    print("")


if __name__ == "__main__":
    ft_tournament()
