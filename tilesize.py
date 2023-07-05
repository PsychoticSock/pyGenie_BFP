from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int16, int32

class TileSize(BaseStruct):
    width: int      = Retriever(int16, default=0)
    height: int     = Retriever(int16, default=0)
    delta_z: int    = Retriever(int16, default=0)