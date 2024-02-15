from __future__ import annotations

from class_for_copying import DatFileObject
from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import FixedLenStr


class FileHeader(BaseStruct, DatFileObject):

    # @formatter:off
    game_version: str  = Retriever(FixedLenStr[8],  default=7.7)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, initialise_defaults=True, **retriever_inits):
        super().__init__(struct_ver, parent, initialise_defaults=initialise_defaults, **retriever_inits)



