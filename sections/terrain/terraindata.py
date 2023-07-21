from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int8, uint8, int32, int16, uint16, uint32, Bytes, float32

from dat_file_locations import Dat
from sections.borders.borders import TerrainBorder
from sections.terrain.terrain import Terrain
from sections.terrain.tilesize import TileSize


class TerrainData(BaseStruct):
    def set_repeat_terrain(_, instance: Terrain):
        hardcoded_terrain_count = 0
        if instance.struct_ver > (0,):
            if instance.struct_ver == Dat.SWGB.ver():
                print("SWGB: 55 terrains")
                hardcoded_terrain_count = Dat.SWGB.terrain_count()
            if instance.struct_ver >= Dat.AOE2_DE_START.ver():
                print("AOE2DE: 200 terrains")
                hardcoded_terrain_count = Dat.AOE2_DE_START.terrain_count()
            if instance.struct_ver == Dat.AOE1DE.ver():
                hardcoded_terrain_count = Dat.AOE1DE.terrain_count()
                print(f"AOE1DE: {hardcoded_terrain_count} terrains")
            if instance.struct_ver == Dat.AOE2_AOK_1999.ver():
                hardcoded_terrain_count = Dat.AOE2_AOK_1999.terrain_count()
                print(f"AOK: {hardcoded_terrain_count} terrains")
            if instance.struct_ver == Dat.AOE2_CONQUERORS_2000.ver()[:-1]:
                hardcoded_terrain_count = Dat.AOE2_CONQUERORS_2000.terrain_count()
                print(f"AOC_2000: {hardcoded_terrain_count} terrains")
            if instance.struct_ver == Dat.AOE2_CONQUERORS_10C.ver()[:-1]:
                hardcoded_terrain_count = Dat.AOE2_CONQUERORS_10C.terrain_count()
                print(f"AOC_2000: {hardcoded_terrain_count} terrains")
            if instance.struct_ver == Dat.AOE2_HD_BASE.ver():
                hardcoded_terrain_count = Dat.AOE2_HD_BASE.terrain_count()
                print(f"AOE2 HD no expansions: {hardcoded_terrain_count} terrains")
            if instance.struct_ver == Dat.AOE2_HD_DLC.ver():
                hardcoded_terrain_count = Dat.AOE2_HD_DLC.terrain_count()
                print(f"AOE2 HD with DLC: {hardcoded_terrain_count} terrains")
            if instance.struct_ver == Dat.AOE1_1997.ver():
                hardcoded_terrain_count = Dat.AOE1_1997.terrain_count()
                print(f"AOE1: {hardcoded_terrain_count} terrains")

        Retriever.set_repeat(TerrainData.terrains, instance, hardcoded_terrain_count)

    virt_function_ptr: int          = Retriever(int32,                                                                          default=0)
    map_pointer: int                = Retriever(int32,                                                                          default=0)
    map_width: int                  = Retriever(int32,                                                                          default=0)
    map_height: int                 = Retriever(int32,                                                                          default=0)
    world_width: int                = Retriever(int32,                                                                          default=0)
    world_height: int               = Retriever(int32,                                                                          default=0)
    tile_sizes: TileSize            = Retriever(TileSize,                                                                       default=TileSize(), repeat=19)
    padding1: int                   = Retriever(int16,                                                                          default=0)

    _                               = Retriever(Bytes[0],                                                                       default=b"", on_set=[set_repeat_terrain])
    terrains: Terrain               = Retriever(Terrain,                                                                        default=Terrain())
    terrain_border: TerrainBorder   = Retriever(TerrainBorder,  min_ver=Dat.AOE1_1997.ver(), max_ver=Dat.SWGB_EXPANSION.ver(),  default=TerrainBorder(), repeat=16)

    map_row_offset: int             = Retriever(int32,          min_ver=Dat.AOE1_1997.ver(), max_ver=Dat.SWGB_EXPANSION.ver(),  default=0)

    map_min_x: int                  = Retriever(float32,        min_ver=Dat.AOE2_AOK_1999.ver(),                                default=0)
    map_min_y: int                  = Retriever(float32,        min_ver=Dat.AOE2_AOK_1999.ver(),                                default=0)
    map_max_x: int                  = Retriever(float32,        min_ver=Dat.AOE2_AOK_1999.ver(),                                default=0)
    map_max_y: int                  = Retriever(float32,        min_ver=Dat.AOE2_AOK_1999.ver(),                                default=0)
    map_max_xplus1: int             = Retriever(float32,        min_ver=Dat.AOE2_AOK_1999.ver(),                                default=0)
    map_min_yplus1: int             = Retriever(float32,        min_ver=Dat.AOE2_AOK_1999.ver(),                                default=0)

    terrain_count_additional: int   = Retriever(uint16,                                                                         default=0)
    borders_used: int               = Retriever(uint16,                                                                         default=0)
    max_terrain: int                = Retriever(int16,                                                                          default=0)
    tile_width: int                 = Retriever(int16,                                                                          default=0)
    tile_height: int                = Retriever(int16,                                                                          default=0)
    tile_half_height: int           = Retriever(int16,                                                                          default=0)
    tile_half_width: int            = Retriever(int16,                                                                          default=0)
    elev_height: int                = Retriever(int16,                                                                          default=0)
    current_row: int                = Retriever(int16,                                                                          default=0)
    current_column: int             = Retriever(int16,                                                                          default=0)
    block_beginn_row: int           = Retriever(int16,                                                                          default=0)
    block_end_row: int              = Retriever(int16,                                                                          default=0)
    block_begin_column: int         = Retriever(int16,                                                                          default=0)
    block_end_column: int           = Retriever(int16,                                                                          default=0)

    search_map_ptr: int             = Retriever(int32,          min_ver=Dat.AOE2_AOK_1999.ver(),                                default=0)
    search_map_rows_ptr: int        = Retriever(int32,          min_ver=Dat.AOE2_AOK_1999.ver(),                                default=0)
    any_frame_change: int           = Retriever(int8,           min_ver=Dat.AOE2_AOK_1999.ver(),                                default=0)

    any_frame_change_aoe1: int      = Retriever(int32,          max_ver=Dat.AOE1DE.ver(),                                       default=0)
    search_map_ptr_aoe1: int        = Retriever(int32,          max_ver=Dat.AOE1DE.ver(),                                       default=0)
    search_map_rows_ptr_aoe1: int   = Retriever(int32,          max_ver=Dat.AOE1DE.ver(),                                       default=0)

    map_visible_flag: int           = Retriever(int8,                                                                           default=0)
    fog_flag: int                   = Retriever(int8,                                                                           default=0)

    terrain_blob0_swgb: int         = Retriever(uint8,          Version(Dat.SWGB.ver()),    Version(Dat.SWGB.ver()),            default=0, repeat=25)
    terrain_blob1_swgb: int         = Retriever(uint32,         Version(Dat.SWGB.ver()),    Version(Dat.SWGB.ver()),            default=0, repeat=157)

    terrain_blob0_aoe1: int         = Retriever(uint8,          max_ver=Dat.AOE1DE.ver(),                                       default=0, repeat=2)
    terrain_blob1_aoe1: int         = Retriever(uint32,         max_ver=Dat.AOE1DE.ver(),                                       default=0, repeat=5)

    terrain_blob0: int              = Retriever(uint8,          min_ver=Dat.AOE2_AOK_1999.ver(), max_ver=Dat.AOE2_HD_DLC.ver(), default=0, repeat=21,)
    terrain_blob1: int              = Retriever(uint32,         min_ver=Dat.AOE2_AOK_1999.ver(), max_ver=Dat.AOE2_HD_DLC.ver(), default=0, repeat=157)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)



