from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int32

class MapElevation(BaseStruct):
    proportion: int         = Retriever(int32,  default=0)
    terrain: int            = Retriever(int32,  default=0)
    clump_count: int        = Retriever(int32,  default=0)
    base_terrain: int       = Retriever(int32,  default=0)
    base_elevation: int     = Retriever(int32,  default=0)
    tile_spacing: int       = Retriever(int32,  default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)