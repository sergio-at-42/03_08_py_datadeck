#!/usr/bin/env python3


from ex0 import CreatureFactory, FlameFactory, AquaFactory


def ft_test_factory(creature_factory: CreatureFactory) -> None:
    base_creature = creature_factory.create_base()
    evolved_creature = creature_factory.create_evolved()
    print(base_creature.concrete())
    print(base_creature.attack())
    print(evolved_creature.concrete())
    print(evolved_creature.attack())


def ft_test_batlle(cf1: CreatureFactory, cf2: CreatureFactory) -> None:
    base_creature1 = cf1.create_base()
    base_creature2 = cf2.create_base()
    print(base_creature1.concrete())
    print("vs.")
    print(base_creature2.concrete())
    print("fight!")
    print(base_creature1.attack())
    print(base_creature2.attack())


def ft_battle() -> None:

    ff = FlameFactory()
    af = AquaFactory()

    print("Testing factory")
    ft_test_factory(ff)
    print("")

    print("Testing factory")
    ft_test_factory(af)
    print("")

    print("Testing battle")
    ft_test_batlle(ff, af)


if __name__ == "__main__":
    ft_battle()
