from __future__ import annotations

import zlib

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import FixedLenStr


class FileHeader(BaseStruct):

    # @formatter:off
    game_version: str  = Retriever(FixedLenStr[8],  default=7.7)

    @classmethod
    def decompress(cls, bytes_: bytes) -> bytes:
      return zlib.decompress(bytes_, -zlib.MAX_WBITS)

    @classmethod
    def compress(cls, bytes_: bytes) -> bytes:
      deflate_obj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
      compressed = deflate_obj.compress(bytes_) + deflate_obj.flush()
      return compressed

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, initialise_defaults=True, **retriever_inits):
        super().__init__(struct_ver, parent, initialise_defaults=initialise_defaults, **retriever_inits)




