from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int8, uint16, int16, str16, int32, Array16, FixedLenStr, float32

from dat_file_locations import Dat
from sections.units.unit_data import UnitData


class Civ(BaseStruct):
    @staticmethod
    def set_resources_count(_, instance: Civ):
        Retriever.set_repeat(Civ.resources , instance, instance.resources_count)

    player_type: int              = Retriever(int8,                                                                                       default=0)
    name_len_debug_1: int           = Retriever(uint16,         Version(Dat.AOE1DE.ver()),            Version(Dat.AOE1DE.ver()),          default=0)
    name_len_debug_2: int           = Retriever(uint16,         Version(Dat.AOE2_DE_START.ver()),     Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    civ_name_1: str               = Retriever(str16,            Version(Dat.AOE1DE.ver()),            Version(Dat.AOE1DE.ver()),          default=0)
    civ_name_2: str               = Retriever(str16,            Version(Dat.AOE2_DE_START.ver()),     Version(Dat.AOE2_DE_LATEST.ver()),  default=0)

    civ_name_3: str               = Retriever(FixedLenStr[20],  Version(Dat.AOE1_1997.ver()),         Version(Dat.AOE1DE_ORIGINAL.ver()), default=0)
    civ_name_4: str               = Retriever(FixedLenStr[20],  Version(Dat.AOE2_AOK_1999.ver()),     Version(Dat.SWGB_EXPANSION.ver()),  default=0)

    resources_count: int          = Retriever(uint16,                                                                                     default=0, on_set=[set_resources_count])
    tech_tree_id: int             = Retriever(int16,                                                                                      default=0)

    team_bonus_id: int            = Retriever(int16, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),                 default=0)

    name2: int                    = Retriever(FixedLenStr[20], Version(Dat.SWGB.ver()), Version(Dat.SWGB_EXPANSION.ver()),                default=0)
    unique_unit_techs: list[int]  = Retriever(int16, Version(Dat.SWGB.ver()), Version(Dat.SWGB_EXPANSION.ver()),                          default=0, repeat=4)

    resources: list[float]        = Retriever(float32,                                                                                    default=0)

    icon_set: int                 = Retriever(int8,                                                                                       default=0)
    unit_offsets: int             = Retriever(Array16[int32],                                                                             default=[])   # If an entry is    b"\00\00\00\00" then a unit is non-existent for that civ,
                                                                                                                                                        # if present it is  b"\01\00\00\00"
    #unit_data: UnitData           = Retriever(UnitData, default=UnitData())


    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

