from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int8, uint8, int32, int16, str16, uint16, FixedLenStr, uint32, FixedLenArray

from dat_file_locations import Dat
from frame_data import FrameData


class Terrain(BaseStruct):
    def set_repeat_terrain(_, instance: Terrain):
        hardcoded_terrain_count = 0
        if instance.struct_ver == (5,9):
            print("SWGB: 55 terrains")
            hardcoded_terrain_count = 55
        if instance.struct_ver >= (7,1):
            print("AOE2DE: 200 terrains")
            hardcoded_terrain_count = 200
        if instance.struct_ver == (4,5):
            print("AOE1DE: 96 terrains")
            hardcoded_terrain_count = 96
        if instance.struct_ver == (5, 7):
            print("AOE2 HD no expansions: 42 terrains")
            hardcoded_terrain_count = 42
        if instance.struct_ver == (5, 7):
            print("AOE2 HD with DLC: 100 terrains")
            hardcoded_terrain_count = 100
        if instance.struct_ver == (5, 7):
            print("AOC: 42 terrains")
            hardcoded_terrain_count = 42
        if instance.struct_ver == (3, 7):
            print("AOE1: 32 terrains")
            hardcoded_terrain_count = 32

        Retriever.set_repeat(Terrain.borders, instance, hardcoded_terrain_count)

    enabled: int                  = Retriever(int8, default=0)
    random: int                   = Retriever(int8, default=0)
    is_water: int                 = Retriever(int8,  min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),                  default=0)
    hide_in_editor: int           = Retriever(int8,  min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),                  default=0)
    string_id: int                = Retriever(int32, min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),                  default=0)
    is_water: int                 = Retriever(int8,  min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),          default=0)
    hide_in_editor: int           = Retriever(int8,  min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),          default=0)
    string_id: int                = Retriever(int32, min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),          default=0)
    blend_priority_de: int           = Retriever(int16, min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),                  default=0)
    blend_type_de: int               = Retriever(int16, min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),                  default=0)
    internal_name_len_debug: int  = Retriever(uint16, min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),                 default=0)
    internal_name: int            = Retriever(str16,  min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),                 default=0)
    filename_len_debug: int       = Retriever(uint16, min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),                 default=0)
    filename: int                 = Retriever(str16,  min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),                 default=0)
    internal_name_len_debug: int  = Retriever(uint16, min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),         default=0)
    internal_name: int            = Retriever(str16,  min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),         default=0)
    filename_len_debug: int       = Retriever(uint16, min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),         default=0)
    filename: int                 = Retriever(str16,  min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),         default=0)

    internal_name: str           = Retriever(FixedLenStr[13], min_ver=Dat.AOE1_1997.ver(), max_ver=Dat.AOE2_HD_DLC.ver(),        default=0)
    filename: str                = Retriever(FixedLenStr[13], min_ver=Dat.AOE1_1997.ver(), max_ver=Dat.AOE2_HD_DLC.ver(),        default=0)
    internal_name: str           = Retriever(FixedLenStr[17], min_ver=Dat.SWGB.ver(), max_ver=Dat.SWGB_EXPANSION.ver(),          default=0)
    filename: str                = Retriever(FixedLenStr[17], min_ver=Dat.SWGB.ver(), max_ver=Dat.SWGB_EXPANSION.ver(),          default=0)
    internal_name: str           = Retriever(FixedLenStr[13], min_ver=Dat.AOE2_DE_START.ver(), max_ver=Dat.AOE2_DE_LATEST.ver(), default=0)
    filename: str                = Retriever(FixedLenStr[13], min_ver=Dat.AOE2_DE_START.ver(), max_ver=Dat.AOE2_DE_LATEST.ver(), default=0)

    slp_id: int                   = Retriever(int32,                                                                              default=0)
    shape_ptr: int                = Retriever(int32,                                                                              default=0)
    sound_id: int                 = Retriever(int32,                                                                              default=0)

    wwise_sound_id: int           = Retriever(uint32, min_ver=Dat.AOE2_DE_START.ver(), max_ver=Dat.AOE2_DE_LATEST.ver(),          default=0)
    wwise_stop_sound_id: int      = Retriever(uint32, min_ver=Dat.AOE2_DE_START.ver(), max_ver=Dat.AOE2_DE_LATEST.ver(),          default=0)


    blend_priority: int           = Retriever(int32, min_ver=Dat.AOE2_AOK_1999.ver(), max_ver=Dat.AOE2_DE_LATEST.ver(),          default=0)
    blend_mode: int               = Retriever(int32, min_ver=Dat.AOE2_AOK_1999.ver(), max_ver=Dat.AOE2_DE_LATEST.ver(),          default=0)

    overlay_mask_name_len_debug:  int = Retriever(uint16, min_ver=Dat.AOE2_DE_START.ver(), max_ver=Dat.AOE2_DE_LATEST.ver(),     default=0)
    overlay_mask_name: int            = Retriever(uint16, min_ver=Dat.AOE2_DE_START.ver(), max_ver=Dat.AOE2_DE_LATEST.ver(),     default=0)

    map_color_hi: int              = Retriever(uint8, default=0)
    map_color_med: int             = Retriever(uint8, default=0)
    map_color_low: int             = Retriever(uint8, default=0)
    map_color_cliff_lt: int        = Retriever(uint8, default=0)
    map_color_cliff_rt: int        = Retriever(uint8, default=0)
    passable_terrain: int          = Retriever(int8, default=0)
    impassable_terrain: int        = Retriever(int8, default=0)

    elevation_graphics: FrameData  = Retriever(FrameData, default=FrameData(), repeat=19)

    terrain_replacement_id: int     = Retriever(int16, default=0)
    terrain_to_draw0: int           = Retriever(int16, default=0)
    terrain_to_draw1: int           = Retriever(int16, default=0)

    terrain_unit_masked_density: list[int] = Retriever(int16, min_ver=Dat.AOE2_DE_START.ver(), repeat=30, default=[])

    borders: list[int]              = Retriever(int16, default=0, repeat=0)

    terrain_unit_id: int             = Retriever(int16, default=0, repeat=30)
    terrain_unit_density: int        = Retriever(int16, default=0, repeat=30)
    terrain_placement_flag: int      = Retriever(int8, default=0, repeat=30)
    terrain_units_used_count: int    = Retriever(int16, default=0)

    phantom: int                     = Retriever(int16, default=())