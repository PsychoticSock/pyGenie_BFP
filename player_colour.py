from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import uint16

from dat_file_locations import DatVersion
from player_colour_data import PlayerColourData_ROR_AOE1DE, PlayerColourData_AOE2_SWGB


class PlayerColour(BaseStruct):
    @staticmethod
    def set_player_colour_count(_, instance: PlayerColour):
        Retriever.set_repeat(PlayerColour.player_colour_data_ROR_AOE1DE, instance, instance.player_colour_count)
        Retriever.set_repeat(PlayerColour.player_colour_data_AOE2_SWGB, instance, instance.player_colour_count)

    player_colour_count: int = Retriever(uint16, default=15, on_set=[set_player_colour_count])
    player_colour_data_ROR_AOE1DE: list[PlayerColourData_ROR_AOE1DE]   = Retriever(PlayerColourData_ROR_AOE1DE, min_ver=DatVersion.AOE1_1997.version_tuple(), max_ver=DatVersion.AOE1DE.version_tuple(),    default=PlayerColourData_ROR_AOE1DE())
    player_colour_data_AOE2_SWGB:   list[PlayerColourData_AOE2_SWGB]   = Retriever(PlayerColourData_AOE2_SWGB,  min_ver=DatVersion.AOE2_AOK_1999.version_tuple(), max_ver=DatVersion.AOE2_DE_LATEST.version_tuple(),   default=PlayerColourData_AOE2_SWGB())


    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)


