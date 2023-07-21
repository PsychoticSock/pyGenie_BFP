from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int16, int32


class GraphicDeltas(BaseStruct):
    graphic_id: int     = Retriever(int16,      default=0)
    padding_1: int      = Retriever(int16,      default=0)
    sprite_ptr: int     = Retriever(int32,      default=0)
    offset_x: int       = Retriever(int16,      default=0)
    offset_y: int       = Retriever(int16,      default=0)
    display_angle: int  = Retriever(int16,      default=0)
    padding_2: int      = Retriever(int16,      default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)
