from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int8, int16, int32, Array8

from dat_file_locations import Dat
from sections.tech_trees.other_connection import OtherConnection


class UnitConnection(BaseStruct):
    id: int                             = Retriever(int32,                                                                                  default=0)
    status: int                         = Retriever(int8,                                                                                   default=0)
    upper_building: int                 = Retriever(int32,                                                                                  default=0)
    connected_slots_used: int           = Retriever(int32,                                                                                  default=0)

    other_connected_ids_1: list[int]    = Retriever(int32,          Version(Dat.SWGB.ver()),             Version(Dat.SWGB_EXPANSION.ver()), default=0, repeat=20)
    other_connections_1: list[OtherConnection] = Retriever(OtherConnection, Version(Dat.SWGB.ver()), Version(Dat.SWGB_EXPANSION.ver()), default=OtherConnection(), repeat=20)

    #other_connected_ids_2: list[int]   = Retriever(int32,          Version(Dat.AOE1_1997.ver()),        Version(Dat.AOE1DE.ver()),         default=0, repeat=5) # Why is this even here in the Openage Struct, I can't find that this data is used...
    # other_connections_2: list[int]    = Retriever(int32,          Version(Dat.AOE1_1997.ver()),        Version(Dat.AOE1DE.ver()),         default=int, repeat=5)

    other_connected_ids_3: list[int]    = Retriever(int32,          Version(Dat.AOE2_AOK_1999.ver()),    Version(Dat.AOE2_HD_DLC.ver()),    default=0, repeat=10)
    other_connections_3: list[OtherConnection] = Retriever(OtherConnection, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_HD_DLC.ver()), default=OtherConnection(), repeat=10)
    other_connected_ids_4: list[int]    = Retriever(int32,          Version(Dat.AOE2_DE_START.ver()),    Version(Dat.AOE2_DE_LATEST.ver()), default=0, repeat=10)

    other_connections_4: list[OtherConnection] = Retriever(OtherConnection, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()), default=OtherConnection(), repeat=10)
    vertical_line: int                = Retriever(int32,          Version(Dat.AOE2_AOK_1999.ver()),    Version(Dat.AOE2_DE_LATEST.ver()),    default=0)

    units_1: list[int]                  = Retriever(Array8[int32],  Version(Dat.AOE2_AOK_1999.ver()),    Version(Dat.AOE2_DE_LATEST.ver()), default=0)
    units_2: list[int]                  = Retriever(Array8[int8],   Version(Dat.AOE1_1997.ver()),        Version(Dat.AOE1DE.ver()),         default=0, repeat=40)

    location_in_age: int                = Retriever(int32,                                                                                  default=0)
    required_research: int              = Retriever(int32,                                                                                  default=0)
    line_mode: int                      = Retriever(int32,                                                                                  default=0)
    enabling_research: int              = Retriever(int32,                                                                                  default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

