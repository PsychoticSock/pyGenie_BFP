from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int32


class MapTerrain(BaseStruct):
    proportion: int         = Retriever(int32,  default=0)
    terrain_id: int         = Retriever(int32,  default=0)
    number_of_clumps: int   = Retriever(int32,  default=0)
    edge_spacing: int       = Retriever(int32,  default=0)
    placement_zone: int     = Retriever(int32,  default=0)
    clumpiness: int         = Retriever(int32,  default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)