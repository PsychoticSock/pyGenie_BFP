from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int8, int16, int32

class MapUnit(BaseStruct):
    unit_id: int                    = Retriever(int32,  default=0)
    host_terrain: int               = Retriever(int32,  default=0)
    group_placing: int              = Retriever(int8,   default=0)
    scale_flag: int                 = Retriever(int8,   default=0)
    padding1: int                   = Retriever(int16,  default=0)
    objects_per_group: int          = Retriever(int32,  default=0)
    fluctuation: int                = Retriever(int32,  default=0)
    groups_per_player: int          = Retriever(int32,  default=0)
    group_radius: int               = Retriever(int32,  default=0)
    own_at_start: int               = Retriever(int32,  default=0)
    set_place_for_all_players: int  = Retriever(int32,  default=0)
    min_distance_to_players: int    = Retriever(int32,  default=0)
    max_distance_to_players: int    = Retriever(int32,  default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)