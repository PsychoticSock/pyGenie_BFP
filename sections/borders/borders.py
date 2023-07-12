from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever


from binary_file_parser.types import uint8, int8, int16, int32, FixedLenStr

from sections.terrain.frame_data import FrameData
from sections.terrain.terrain_animation import TerrainAnimation


class TerrainBorder(BaseStruct):


    enabled: int                        = Retriever(int8,               default=0)
    random: int                         = Retriever(int8,               default=0)
    internal_name: str                  = Retriever(FixedLenStr[13], default=0)
    filename: int                       = Retriever(FixedLenStr[13],    default=0)
    slp_id: int                         = Retriever(int32,              default=0)
    shape_ptr: int                      = Retriever(int32,              default=0)
    sound_id: int                       = Retriever(int32,              default=0)
    color: int                          = Retriever(uint8,              default=0, repeat=3)

    terrain_animation: TerrainAnimation = Retriever(TerrainAnimation,   default=TerrainAnimation())
    frames: FrameData                      = Retriever(FrameData,       default=FrameData(), repeat=19*12)

    draw_tile: int                          = Retriever(int16,          default=0)
    underlay_terrain: int                   = Retriever(int16,          default=0)
    border_style: int                       = Retriever(int16,          default=0)