from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import uint32

from sections.map.map import MapDetails
from sections.map.map_info import MapInfo

from class_for_copying import DatFileObject

class Maps(BaseStruct, DatFileObject):
    @staticmethod
    def set_map_count(_, instance: Maps):
        Retriever.set_repeat(Maps.map_info, instance, instance.random_map_count)
        Retriever.set_repeat(Maps.map_details, instance, instance.random_map_count)

    random_map_count: int   = Retriever(uint32,                 default=0, on_set=[set_map_count])
    random_map_ptr: int     = Retriever(uint32,                 default=0)
    map_info: MapInfo       = Retriever(MapInfo,                default=MapInfo(), repeat=0)
    map_details: MapDetails = Retriever(MapDetails,      default=MapDetails(), repeat=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

