from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import uint16

from sound import Sound


class Sounds(BaseStruct):
    @staticmethod
    def set_sound_count(_, instance: Sounds):
        Retriever.set_repeat(Sounds.sound_data, instance, instance.sound_count)

    sound_count: int            = Retriever(uint16,     default=0,         on_set=[set_sound_count])
    sound_data: list[Sound]     = Retriever(Sound,      default=Sound())

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)


