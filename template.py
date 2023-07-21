from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int32, uint32

from dat_file_locations import Dat

class ClassName(BaseStruct):
    @staticmethod
    def set____count(_, instance: ClassName):
        pass
        #Retriever.set_repeat(ClassName.retrievername2 , instance, instance.retrievername1)

    retrievername1: int = Retriever(uint32, default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

