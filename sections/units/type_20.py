from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import float32, float16


class Type20(BaseStruct):
    speed: float = Retriever(float32, default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

