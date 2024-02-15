from __future__ import annotations


from class_for_copying import DatFileObject
from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int8, int32, Array8

from dat_file_locations import Dat
from sections.tech_trees.other_connection import OtherConnection


class TechConnection(BaseStruct, DatFileObject):
    id: int                             = Retriever(int32,                                                                                          default=0)
    status: int                         = Retriever(int8,                                                                                           default=0)
    upper_building: int                 = Retriever(int32,                                                                                          default=0)

    buildings: list[int]                = Retriever(Array8[int32], Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),             default=0)
    units: list[int]                    = Retriever(Array8[int32], Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),             default=0)
    techs: list[int]                    = Retriever(Array8[int32], Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),             default=0)

    # NB, there are possibly some AOK betas that have the above with a repeat of 40 instead of as an array.

    connected_slots_used: int           = Retriever(int32,                                                                                          default=0)

    #####################

    other_connected_ids_1: list[int]    = Retriever(int32,          Version(Dat.SWGB.ver()),             Version(Dat.SWGB_EXPANSION.ver()),         default=0,                  repeat=20)
    other_connections_1: list[OtherConnection] = Retriever(OtherConnection, Version(Dat.SWGB.ver()), Version(Dat.SWGB_EXPANSION.ver()),             default=OtherConnection(),  repeat=20)
    # other_connected_ids_2: list[int]   = Retriever(int32,          Version(Dat.AOE1_1997.ver()),        Version(Dat.AOE1DE.ver()),                default=0,                  repeat=5)   # AOK Beta possibly
    # other_connections_2: list[int]    = Retriever(int32,          Version(Dat.AOE1_1997.ver()),        Version(Dat.AOE1DE.ver()),                 default=int,                    repeat=5) # AOK Beta possibly

    other_connected_ids_3: list[int]    = Retriever(int32,          Version(Dat.AOE2_AOK_1999.ver()),    Version(Dat.AOE2_HD_DLC.ver()),            default=0,                  repeat=10)
    other_connections_3: list[OtherConnection] = Retriever(OtherConnection, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_HD_DLC.ver()),       default=OtherConnection(),  repeat=10)
    other_connected_ids_4: list[int]    = Retriever(int32,          Version(Dat.AOE2_DE_START.ver()),    Version(Dat.AOE2_DE_LATEST.ver()),         default=0,                  repeat=10)

    other_connections_4: list[OtherConnection] = Retriever(OtherConnection, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),    default=OtherConnection(),  repeat=10)
    vertical_line: int                = Retriever(int32,          Version(Dat.AOE2_AOK_1999.ver()),    Version(Dat.AOE2_DE_LATEST.ver()),           default=0)

    location_in_age: int                = Retriever(int32,                                                                                          default=0)
    line_mode: int                      = Retriever(int32,                                                                                          default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

