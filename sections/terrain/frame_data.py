from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int16

from class_for_copying import DatFileObject

class FrameData(BaseStruct, DatFileObject):
    frame_count: int    = Retriever(int16,      default=0)
    angle_count: int    = Retriever(int16,      default=0)
    shape_id: int       = Retriever(int16,      default=0)

def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
             initialise_defaults: bool = True, **retriever_inits):
    super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)
