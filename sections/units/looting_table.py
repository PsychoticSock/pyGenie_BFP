from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int8


class LootingTable(BaseStruct):
    stone_loot_switch: int      = Retriever(int8,       default=0)
    wood_loot_switch: int       = Retriever(int8,       default=0)
    ore_loot_switch: int        = Retriever(int8,       default=0)
    gold_loot_switch: int       = Retriever(int8,       default=0)
    food_loot_switch: int       = Retriever(int8,       default=0)
    goods_loot_switch: int      = Retriever(int8,       default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)
