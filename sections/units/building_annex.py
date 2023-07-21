from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int16, float32


class BuildingAnnex(BaseStruct):
    unit_id: int        = Retriever(int16, default=0)
    misplaced0: int     = Retriever(float32, default=0)
    misplaced1: int     = Retriever(float32, default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)
