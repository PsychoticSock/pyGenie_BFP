from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import uint16

from dat_file_locations import Dat
from player_colour_data import PlayerColourDataAOE1, PlayerColourData_AOE2_SWGB


class PlayerColour(BaseStruct):
    @staticmethod
    def set_player_colour_count(_, instance: PlayerColour):
        Retriever.set_repeat(PlayerColour.ror_aoe1de, instance, instance.player_colour_count)
        Retriever.set_repeat(PlayerColour.aeo2_swgb, instance, instance.player_colour_count)

    player_colour_count: int                    = Retriever(uint16,                                                       default=15, on_set=[set_player_colour_count])
    ror_aoe1de: list[PlayerColourDataAOE1]      = Retriever(PlayerColourDataAOE1,   min_ver=Dat.AOE1_1997.ver(),
                                                                                    max_ver=Dat.AOE1DE.ver(),             default=PlayerColourDataAOE1())
    aeo2_swgb: list[PlayerColourData_AOE2_SWGB] = Retriever(PlayerColourData_AOE2_SWGB, min_ver=Dat.AOE2_AOK_1999.ver(),
                                                                                        max_ver=Dat.AOE2_DE_LATEST.ver(), default=PlayerColourData_AOE2_SWGB())


    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)


