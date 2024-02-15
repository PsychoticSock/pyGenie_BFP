from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int16, uint32

from class_for_copying import DatFileObject


class DE2SoundProp(BaseStruct, DatFileObject):
    sound_delay0: int = Retriever(int16,    default=0)
    sound_id0: int      = Retriever(int16,  default=0)
    wwise_sound0: int   = Retriever(uint32, default=0)
    sound_delay1: int   = Retriever(int16,  default=0)
    sound_id1: int      = Retriever(int16,  default=0)
    wwise_sound1: int   = Retriever(uint32, default=0)
    sound_delay2: int   = Retriever(int16,  default=0)
    sound_id2: int      = Retriever(int16,  default=0)
    wwise_sound2: int   = Retriever(uint32, default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)


class SoundProp(BaseStruct, DatFileObject):
    sound_delay: int    = Retriever(int16,  default=0)
    sound_id: int       = Retriever(int16,  default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)


