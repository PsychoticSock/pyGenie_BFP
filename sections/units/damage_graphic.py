from __future__ import annotations


from class_for_copying import DatFileObject
from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int8, int16


class DamageGraphic(BaseStruct, DatFileObject):
    graphic_id: int      = Retriever(int16,   default=0)
    damage_percent: int  = Retriever(int8,    default=0)
    old_apply_mode: int  = Retriever(int8,    default=0)
    apply_mode: int      = Retriever(int8,    default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

