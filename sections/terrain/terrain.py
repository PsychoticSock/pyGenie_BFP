from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int8, uint8, int32, int16, str16, uint16, FixedLenStr, uint32, Bytes

from dat_file_locations import Dat
from sections.terrain.frame_data import FrameData
from sections.terrain.terrain_animation import TerrainAnimation


class Terrain(BaseStruct):
    def set_repeat_terrain(_, instance: Terrain):
        hardcoded_terrain_count = 0
        if instance.struct_ver == Dat.SWGB.ver():
            #print("SWGB: 55 terrains")
            hardcoded_terrain_count = Dat.SWGB.terrain_count()
        if instance.struct_ver >= Dat.AOE2_DE_START.ver():
            #print("AOE2DE: 200 terrains")
            hardcoded_terrain_count = Dat.AOE2_DE_START.terrain_count()
        if instance.struct_ver == Dat.AOE1DE.ver():
            hardcoded_terrain_count = Dat.AOE1DE.terrain_count()
            #print(f"AOE1DE: {hardcoded_terrain_count} terrains")
        if instance.struct_ver == Dat.AOE2_AOK_1999.ver():
            hardcoded_terrain_count = Dat.AOE2_AOK_1999.terrain_count()
        if instance.struct_ver == Dat.AOE2_CONQUERORS_2000.ver()[:-1]:
            hardcoded_terrain_count = Dat.AOE2_CONQUERORS_2000.terrain_count()
        if instance.struct_ver == Dat.AOE2_CONQUERORS_10C.ver()[:-1]:
            hardcoded_terrain_count = Dat.AOE2_CONQUERORS_10C.terrain_count()
            #print(f"AOK: {hardcoded_terrain_count} terrains")
        if instance.struct_ver == Dat.AOE2_HD_BASE.ver():
            hardcoded_terrain_count = Dat.AOE2_HD_BASE.terrain_count()
            #print(f"AOE2 HD no expansions: {hardcoded_terrain_count} terrains")
        if instance.struct_ver == Dat.AOE2_HD_DLC.ver():
            hardcoded_terrain_count = Dat.AOE2_HD_DLC.terrain_count()
            #print(f"AOE2 HD with DLC: {hardcoded_terrain_count} terrains")
        if instance.struct_ver == Dat.AOE1_1997.ver():
            hardcoded_terrain_count = Dat.AOE1_1997.terrain_count()
            #print(f"AOE1: {hardcoded_terrain_count} terrains")

        Retriever.set_repeat(Terrain.borders, instance, hardcoded_terrain_count)

    enabled: int                            = Retriever(int8,                                                                                  default=0)
    random: int                             = Retriever(int8,                                                                                  default=0)
    is_water_AOE1DE: int                    = Retriever(int8,            min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),           default=0)
    hide_in_editor_AOE1DE: int              = Retriever(int8,            min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),           default=0)
    string_id_AOE1DE: int                   = Retriever(int32,           min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),           default=0)
    is_water_AOE2DE: int                    = Retriever(int8,            min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)
    hide_in_editor_AOE2DE: int              = Retriever(int8,            min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)
    string_id_AOE2DE: int                   = Retriever(int32,           min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)
    blend_priority_de_AOE1DE: int           = Retriever(int16,           min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),           default=0)
    blend_type_de_AOE1DE: int               = Retriever(int16,           min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),           default=0)
    internal_name_len_debug_AOE1DE: int     = Retriever(uint16,          min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),           default=0)
    internal_name_AOE1DE: str               = Retriever(str16,           min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),           default=0)
    filename_len_debug_AOE1DE: int          = Retriever(uint16,          min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),           default=0)
    filename_AOE1DE: str                    = Retriever(str16,           min_ver=Dat.AOE1DE.ver(),         max_ver=Dat.AOE1DE.ver(),           default=0)
    internal_name_len_debug_AOE2DE: int     = Retriever(uint16,          min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)
    internal_name_AOE2DE: str               = Retriever(str16,           min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)
    filename_len_debug_AOE2DE: int          = Retriever(uint16,          min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)
    filename_AOE2DE: str                    = Retriever(str16,           min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)

    internal_name_AOE1: str                 = Retriever(FixedLenStr[13], min_ver=Dat.AOE1_1997.ver(),      max_ver=Dat.AOE1DE_CLASSIC.ver(),   default=0)
    filename_AOE1: str                      = Retriever(FixedLenStr[13], min_ver=Dat.AOE1_1997.ver(),      max_ver=Dat.AOE1DE_CLASSIC.ver(),   default=0)
    internal_name_HD: str                   = Retriever(FixedLenStr[13], min_ver=Dat.AOE2_AOK_1999.ver(),  max_ver=Dat.AOE2_HD_DLC.ver(),      default=0)
    filename_HD: str                        = Retriever(FixedLenStr[13], min_ver=Dat.AOE2_AOK_1999.ver(),  max_ver=Dat.AOE2_HD_DLC.ver(),      default=0)
    internal_name_SWGB: str                 = Retriever(FixedLenStr[17], min_ver=Dat.SWGB.ver(),           max_ver=Dat.SWGB_EXPANSION.ver(),   default=0)
    filename_SWGB: str                      = Retriever(FixedLenStr[17], min_ver=Dat.SWGB.ver(),           max_ver=Dat.SWGB_EXPANSION.ver(),   default=0)
    internal_name_AOE2DE: str               = Retriever(str16,           min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)
    filename_AOE2DE: str                    = Retriever(str16,           min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)

    slp_id: int                             = Retriever(int32,                                                                                 default=0)
    shape_ptr: int                          = Retriever(int32,                                                                                 default=0)
    sound_id: int                           = Retriever(int32,                                                                                 default=0)

    wwise_sound_id_AOE2DE: int              = Retriever(uint32,          min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)
    wwise_stop_sound_id_AOE2DE: int         = Retriever(uint32,          min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)


    blend_priority: int                     = Retriever(int32,           min_ver=Dat.AOE2_AOK_1999.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)
    blend_mode: int                         = Retriever(int32,           min_ver=Dat.AOE2_AOK_1999.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)

    overlay_mask_name_len_debug:  int       = Retriever(uint16,          min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)
    overlay_mask_name: int                  = Retriever(str16,           min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)

    map_color_hi: int                       = Retriever(uint8,                                                                                 default=0)
    map_color_med: int                      = Retriever(uint8,                                                                                 default=0)
    map_color_low: int                      = Retriever(uint8,                                                                                 default=0)
    map_color_cliff_lt: int                 = Retriever(uint8,                                                                                 default=0)
    map_color_cliff_rt: int                 = Retriever(uint8,                                                                                 default=0)
    passable_terrain: int                   = Retriever(int8,                                                                                  default=0)
    impassable_terrain: int                 = Retriever(int8,                                                                                  default=0)

    terrain_animation: TerrainAnimation     = Retriever(TerrainAnimation,                                                                      default=TerrainAnimation())
    elevation_graphics: FrameData           = Retriever(FrameData,                                                                             default=FrameData(),         repeat=19)

    terrain_replacement_id: int             = Retriever(int16,                                                                                 default=0)
    terrain_to_draw0: int                   = Retriever(int16,                                                                                 default=0)
    terrain_to_draw1: int                   = Retriever(int16,                                                                                 default=0)

    _                                       = Retriever(Bytes[0],                                                                              default=b"",     on_set=[set_repeat_terrain])
    borders: list[int]                      = Retriever(int16,           min_ver=Dat.AOE1_1997.ver(),      max_ver=Dat.SWGB_EXPANSION.ver(),   default=0,                   repeat=0)

    terrain_unit_masked_density: list[int]  = Retriever(int16,           min_ver=Dat.AOE2_DE_START.ver(),                                      default=[],                  repeat=30)

    terrain_unit_id: int                    = Retriever(int16,                                                                                 default=0,                   repeat=30)
    terrain_unit_density: int               = Retriever(int16,                                                                                 default=0,                   repeat=30)
    terrain_placement_flag: int             = Retriever(int8,                                                                                  default=0,                   repeat=30)
    terrain_units_used_count: int           = Retriever(int16,                                                                                 default=0)

    phantom_aoe1_HD_DLC: int                = Retriever(int16,            min_ver=Dat.AOE1_1997.ver(),      max_ver=Dat.AOE2_HD_DLC.ver(),     default=())
    phantom_aoe2de: int                     = Retriever(int16,            min_ver=Dat.AOE2_DE_START.ver(),  max_ver=Dat.AOE2_DE_LATEST.ver(),  default=())

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)



