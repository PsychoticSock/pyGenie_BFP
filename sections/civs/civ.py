from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version, RetrieverCombiner
from binary_file_parser.types import int8, uint8, uint16, int16, str16, int32, Array16, FixedLenStr, float32

from dat_file_locations import Dat
from sections.units.unit_data import UnitData


class Civ(BaseStruct):
    @staticmethod
    def set_resources_count(_, instance: Civ):
        Retriever.set_repeat(Civ.resources , instance, instance.resources_count)
    @staticmethod
    def set_unit_data_repeat(_, instance: Civ):
        if instance.struct_ver > (0,0):
            print(f"{instance.civ_name} civ has {len([x for x in instance.unit_offsets if x > 0])} units")
            Retriever.set_repeat(Civ.unit_data , instance, len([x for x in instance.unit_offsets if x > 0]))#

    player_type: int              = Retriever(int8,                                                                                       default=0)
    name_len_debug_1: int         = Retriever(uint16,           Version(Dat.AOE1DE.ver()),            Version(Dat.AOE1DE.ver()),          default=0)
    name_len_debug_2: int         = Retriever(uint16,           Version(Dat.AOE2_DE_START.ver()),     Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    civ_name_1: str               = Retriever(str16,            Version(Dat.AOE1DE.ver()),            Version(Dat.AOE1DE.ver()),          default=0)
    civ_name_2: str               = Retriever(str16,            Version(Dat.AOE2_DE_START.ver()),     Version(Dat.AOE2_DE_LATEST.ver()),  default=0)

    civ_name_3: str               = Retriever(FixedLenStr[20],  Version(Dat.AOE1_1997.ver()),         Version(Dat.AOE1DE_ORIGINAL.ver()), default=0)
    civ_name_4: str               = Retriever(FixedLenStr[20],  Version(Dat.AOE2_AOK_1999.ver()),     Version(Dat.SWGB_EXPANSION.ver()),  default=0)

    civ_name: str                 = RetrieverCombiner([civ_name_1, civ_name_2, civ_name_3, civ_name_4])

    resources_count: int          = Retriever(uint16,                                                                                     default=0, on_set=[set_resources_count])
    tech_tree_id: int             = Retriever(int16,                                                                                      default=0)

    team_bonus_id: int            = Retriever(int16,            Version(Dat.AOE2_AOK_1999.ver()),     Version(Dat.AOE2_DE_LATEST.ver()),  default=0)

    name2: str                    = Retriever(FixedLenStr[20],  Version(Dat.SWGB.ver()),              Version(Dat.SWGB_EXPANSION.ver()),  default=0)
    unique_unit_techs: list[int]  = Retriever(int16,            Version(Dat.SWGB.ver()),              Version(Dat.SWGB_EXPANSION.ver()),  default=0, repeat=4)

    resources: list[float]        = Retriever(float32,                                                                                    default=0)

    icon_set: int                 = Retriever(uint8,                                                                                       default=0)
    unit_offsets: list[int]       = Retriever(Array16[int32],                                                                             default=[], on_set=[set_unit_data_repeat])
    # If an entry is    b"\00\00\00\00" then a unit is non-existent for that civ,
    # if present it is  b"\01\00\00\00"

    unit_data: list[UnitData]     = Retriever(UnitData, default=UnitData())



    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

