from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int32, uint32

class MapInfo(BaseStruct):
    map_id: int                         = Retriever(int32,  default=0)
    border_south_west: int              = Retriever(int32,  default=0)
    border_north_west: int              = Retriever(int32,  default=0)
    border_north_east: int              = Retriever(int32,  default=0)
    border_south_east: int              = Retriever(int32,  default=0)
    border_usage: int                   = Retriever(int32,  default=0)
    water_shape: int                    = Retriever(int32,  default=0)
    base_terrain: int                   = Retriever(int32,  default=0)
    land_coverage: int                  = Retriever(int32,  default=0)
    unused_id: int                      = Retriever(int32,  default=0)
    base_zone_count: int                = Retriever(uint32, default=0)
    base_zone_ptr: int                  = Retriever(int32,  default=0)
    map_terrain_count: int              = Retriever(uint32, default=0)
    map_terrain_ptr: int                = Retriever(int32,  default=0)
    map_unit_count: int                 = Retriever(uint32, default=0)
    map_unit_ptr: int                   = Retriever(int32,  default=0)
    map_elevation_count: int            = Retriever(uint32, default=0)
    map_elevation_ptr: int              = Retriever(int32,  default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)