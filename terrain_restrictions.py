from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import float32



class TerrainRestrictions(BaseStruct):
    accessible_dmgmultiplier: int   = Retriever(float32,    default=1)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, initialise_defaults=True, **retriever_inits):
        super().__init__(struct_ver, parent, initialise_defaults=initialise_defaults, **retriever_inits)
