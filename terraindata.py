from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int16, int32, Bytes

from tilesize import TileSize
from terrain import Terrain

class TerrainData(BaseStruct):
    def set_repeat_terrain(_, instance: TerrainData):
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

        Retriever.set_repeat(TerrainData.terrains, instance, hardcoded_terrain_count)

    virt_function_ptr: int    = Retriever(int32, default=0)
    map_pointer: int          = Retriever(int32, default=0)
    map_width: int            = Retriever(int32, default=0)
    map_height: int           = Retriever(int32, default=0)
    world_width: int          = Retriever(int32, default=0)
    world_height: int         = Retriever(int32, default=0)
    tile_sizes: TileSize      = Retriever(TileSize, default=TileSize(), repeat=19)
    padding1: int             = Retriever(int16, default=0)

    _                         = Retriever(Bytes[0], default=b"", on_set=[set_repeat_terrain])
    terrains: Terrain         = Retriever(Terrain, default=Terrain())


