#!/usr/bin/env python3


from ex1 import HealingCreatureFactory, TransformCreatureFactory


def ft_capacitor() -> None:

    hcf = HealingCreatureFactory()

    print("Testing Creature with healing capability")
    print("base:")
    base_hc = hcf.create_base()
    evolved_hc = hcf.create_evolved()
    print(base_hc.concrete())
    print(base_hc.attack())
    print(base_hc.heal())
    print("evolved:")
    print(evolved_hc.concrete())
    print(evolved_hc.attack())
    print(evolved_hc.heal())
    print("")

    tcf = TransformCreatureFactory()

    print("Testing Creature with transform capability")
    print("base:")
    base_tc = tcf.create_base()
    evolved_tc = tcf.create_evolved()
    print(base_tc.concrete())
    print(base_tc.attack())
    print(base_tc.transform())
    print(base_tc.attack())
    print(base_tc.revert())
    print("evolved:")
    print(evolved_tc.concrete())
    print(evolved_tc.attack())
    print(evolved_tc.transform())
    print(evolved_tc.attack())
    print(evolved_tc.revert())
    print("")


if __name__ == "__main__":
    ft_capacitor()
