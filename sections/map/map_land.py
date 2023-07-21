from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int8, int16, int32


class MapLand(BaseStruct):
    land_id: int            = Retriever(int32,   default=0)
    terrain: int            = Retriever(int32,   default=0)
    land_spacing: int       = Retriever(int32,   default=0)
    base_size: int          = Retriever(int32,   default=0)
    zone: int               = Retriever(int8,    default=0)
    placement_type: int     = Retriever(int8,    default=0)
    padding1: int           = Retriever(int16,   default=0)
    base_x: int             = Retriever(int32,   default=0)
    base_y: int             = Retriever(int32,   default=0)
    land_proportion: int    = Retriever(int8,    default=0)
    by_player_flag: int     = Retriever(int8,    default=0)
    padding2: int           = Retriever(int16,   default=0)
    start_area_radius: int  = Retriever(int32,   default=0)
    terrain_edge_fade: int  = Retriever(int32,   default=0)
    clumpiness: int         = Retriever(int32,   default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)