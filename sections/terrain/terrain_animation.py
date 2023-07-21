from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int8, int16, float32


class TerrainAnimation(BaseStruct):
    is_animated:int            = Retriever(int8,        default=0)
    animation_frame_count:int  = Retriever(int16,       default=0)
    pause_frame_count:int      = Retriever(int16,       default=0)
    interval: float            = Retriever(float32,     default=0)
    pause_between_loops:float  = Retriever(float32,     default=0)
    frame:int                  = Retriever(int16,       default=0)
    draw_frame:int             = Retriever(int16,       default=0)
    animate_last:float         = Retriever(float32,     default=0)
    frame_changed:int          = Retriever(int8,        default=0)
    drawn:int                  = Retriever(int8,        default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)
