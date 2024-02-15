from __future__ import annotations


from class_for_copying import DatFileObject
from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int16, bool8, bool16


class ResourceCost(BaseStruct, DatFileObject):
    type_id: int    = Retriever(int16,      default=0)
    amount: int     = Retriever(int16,      default=0)
    enabled: int    = Retriever(bool16,     default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

class TechResourceCost(BaseStruct, DatFileObject):
    type_id: int    = Retriever(int16,      default=0)
    amount: int     = Retriever(int16,      default=0)
    enabled: bool   = Retriever(bool8,      default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)
