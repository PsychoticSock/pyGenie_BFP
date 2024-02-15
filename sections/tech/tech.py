from __future__ import annotations


from class_for_copying import DatFileObject
from binary_file_parser import Retriever, BaseStruct, Version, RetrieverCombiner
from binary_file_parser.types import int8, int16, uint16, int32, uint32, str16, bool16

from dat_file_locations import Dat
from sections.units.resource_cost import TechResourceCost


class Tech(BaseStruct, DatFileObject):
    required_techs_1: list[int]                     = Retriever(int16,  Version(Dat.AOE2_AOK_1999.ver()),   Version(Dat.AOE2_DE_LATEST.ver()),      default=0, repeat=6)
    required_techs_2: list[int]                     = Retriever(int16,  Version(Dat.AOE1_1997.ver()),       Version(Dat.AOE1DE.ver()),     default=0, repeat=4)
    required_techs: list[int]                       = RetrieverCombiner([required_techs_1, required_techs_2])

    research_resource_costs: list[TechResourceCost] = Retriever(TechResourceCost,                                                                       default=TechResourceCost(), repeat=3)

    required_tech_count: int                        = Retriever(int16,                                                                              default=0)

    civilization_id: int                            = Retriever(int16,   Version(Dat.AOE2_AOK_1999.ver()),    Version(Dat.AOE2_DE_LATEST.ver()),    default=0)
    full_tech_mode: int                             = Retriever(int16,  Version(Dat.AOE2_AOK_1999.ver()),   Version(Dat.AOE2_DE_LATEST.ver()),     default=0)
    research_location_id: int                       = Retriever(int16,                                                                              default=0)

    language_dll_name_1: int                        = Retriever(uint32,  Version(Dat.AOE2_DE_START.ver()),   Version(Dat.AOE2_DE_LATEST.ver()),     default=0)
    language_dll_description_1: int                 = Retriever(uint32,  Version(Dat.AOE2_DE_START.ver()),   Version(Dat.AOE2_DE_LATEST.ver()),     default=0)
    language_dll_name_2: int                        = Retriever(uint16,  Version(Dat.AOE1_1997.ver()),       Version(Dat.SWGB_EXPANSION.ver()),     default=0)
    language_dll_description_2: int                 = Retriever(uint16,  Version(Dat.AOE1_1997.ver()),       Version(Dat.SWGB_EXPANSION.ver()),     default=0)

    research_time: int                              = Retriever(int16,                                                                              default=0)
    tech_effect_id: int                             = Retriever(int16,                                                                              default=0)
    tech_type: int                                  = Retriever(int16,                                                                              default=0)
    icon_id: int                                    = Retriever(int16,                                                                              default=0)
    button_id: int                                  = Retriever(int8,                                                                               default=0)
    language_dll_help: int                          = Retriever(int32,                                                                              default=0)
    language_dll_techtree: int                      = Retriever(int32,                                                                              default=0)
    hotkey: int                                     = Retriever(int32,                                                                              default=0)

    name_length_debug_1: int                        = Retriever(uint16, Version(Dat.AOE1DE.ver()),          Version(Dat.AOE1DE.ver()),              default=0)
    name_1: str                                     = Retriever(str16,  Version(Dat.AOE1DE.ver()),          Version(Dat.AOE1DE.ver()),              default="")
    name_length_debug_2: int                        = Retriever(uint16, Version(Dat.AOE2_DE_START.ver()),   Version(Dat.AOE2_DE_LATEST.ver()),      default=0)
    name_2: str                                     = Retriever(str16,  Version(Dat.AOE2_DE_START.ver()),   Version(Dat.AOE2_DE_LATEST.ver()),      default="")


    repeatable: int                                 = Retriever(int8,   Version(Dat.AOE2_DE_START.ver()),     Version(Dat.AOE2_DE_LATEST.ver()),    default=0)

    name_3: str                                     = Retriever(str16,  Version(Dat.AOE1_1997.ver()),        Version(Dat.AOE1DE_ORIGINAL.ver()),    default="")
    name_4: str                                     = Retriever(str16,  Version(Dat.AOE2_AOK_1999.ver()),    Version(Dat.SWGB_EXPANSION.ver()),     default="")

    name: str                                       = RetrieverCombiner([name_1, name_2, name_3, name_4])

    swgb_name_2: str                                = Retriever(str16, Version(Dat.SWGB.ver()),             Version(Dat.SWGB_EXPANSION.ver()),      default="")

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

