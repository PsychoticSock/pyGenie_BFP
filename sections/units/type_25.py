from __future__ import annotations

from binary_file_parser import BaseStruct, Version

from class_for_copying import DatFileObject


class Type25(BaseStruct, DatFileObject):
    pass

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

