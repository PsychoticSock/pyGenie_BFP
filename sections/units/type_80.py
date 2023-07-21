from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int8, uint8, int16, float32, int32

from dat_file_locations import Dat
from sections.units.building_annex import BuildingAnnex
from sections.units.looting_table import LootingTable


class Type80(BaseStruct):
    construction_graphic_id: int       = Retriever(int16, default=0)
    snow_graphic_id: int               = Retriever(int16,         Version(Dat.AOE2_CONQUERORS_2000.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    destruction_graphic_id: int        = Retriever(int16,         Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    destruction_rubble_graphic_id: int = Retriever(int16,         Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    research_graphic_id: int           = Retriever(int16,         Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    research_complete_graphic_id: int  = Retriever(int16,         Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)

    adjacent_mode: int                 = Retriever(int8,                                                                                default=0)
    graphics_angle: int                = Retriever(int16,                                                                               default=0)
    disappears_when_built: int         = Retriever(int8,                                                                                default=0)
    stack_unit_id: int                 = Retriever(int16,                                                                               default=0)
    foundation_terrain_id: int         = Retriever(int16,                                                                               default=0)
    old_overlay_id: int                = Retriever(int16,                                                                               default=0)
    research_id: int                   = Retriever(int16,                                                                               default=0)

    can_burn: int                      = Retriever(int8,          Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    building_annex: BuildingAnnex      = Retriever(BuildingAnnex, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=BuildingAnnex(), repeat=4)
    head_unit_id: int                  = Retriever(int16,         Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    transform_unit_id: int             = Retriever(int16,         Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    transform_sound_id: int            = Retriever(int16,         Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)

    construction_sound_id: int         = Retriever(int16,                                                                               default=0)

    wwise_construction_sound_id: int   = Retriever(int32,         Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    wwise_transform_sound_id: int      = Retriever(int32,         Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    garrison_type: int                 = Retriever(uint8,         Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    garrison_heal_rate: float          = Retriever(float32,       Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    garrison_repair_rate: float        = Retriever(float32,       Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    salvage_unit_id: int               = Retriever(int16,         Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    salvage_attributes: LootingTable   = Retriever(LootingTable,  Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=LootingTable())

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int                      = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

