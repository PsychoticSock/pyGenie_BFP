from __future__ import annotations


from class_for_copying import DatFileObject
from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import str16, int16, uint16


class UnitLine(BaseStruct, DatFileObject):
    @staticmethod
    def set_unit_ids_count(_, instance: UnitLine):
        Retriever.set_repeat(UnitLine.unit_ids , instance, instance.unit_ids_count)

    id: int                 = Retriever(int16,      default=0)
    name  : int             = Retriever(str16,      default=0)
    unit_ids_count: int     = Retriever(uint16,     default=0, on_set=[set_unit_ids_count])
    unit_ids  : int         = Retriever(int16,      default=0, repeat=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

