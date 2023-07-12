from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version, RetrieverCombiner
from binary_file_parser.types import Array16

from dat_file_locations import Dat
from sections.player_color.player_color_data import PlayerColorData1, PlayerColorData2


class PlayerColour(BaseStruct):

    player_colour_data_ror_aoe1de: list[PlayerColorData1]       = Retriever(Array16[PlayerColorData1], min_ver=Dat.AOE1_1997.ver(),
                                                                                                        max_ver=Dat.AOE1DE.ver(), default=[])
    player_colour_data_aeo2_swgb: list[PlayerColorData2]        = Retriever(Array16[PlayerColorData2], min_ver=Dat.AOE2_AOK_1999.ver(),
                                                                                                        max_ver=Dat.AOE2_DE_LATEST.ver(), default=[])

    player_colour_data: list                                    = RetrieverCombiner([player_colour_data_ror_aoe1de, player_colour_data_aeo2_swgb])

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)


