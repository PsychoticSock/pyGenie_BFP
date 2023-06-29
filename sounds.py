from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import uint16

from dat_file_locations import DatVersion
from player_colour_data import PlayerColourData_ROR_AOE1DE, PlayerColourData_AOE2_SWGB
from sound import Sound


class Sounds(BaseStruct):
    @staticmethod
    def set_sound_count(_, instance: Sounds):
        Retriever.set_repeat(Sounds.sound_data, instance, instance.sound_count)

    sound_count: int            = Retriever(uint16, default=15, on_set=[set_sound_count])
    sound_data: list[Sound]     = Retriever(Sound, min_ver=DatVersion.AOE1_1997.version_tuple(), max_ver=DatVersion.AOE2_DE_LATEST.version_tuple(),    default=Sound())

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)


