from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int32, int16, uint16, uint8, FixedLenStr

from dat_file_locations import DatVersion
from sound_item import SoundItem


class Sound(BaseStruct):
    @staticmethod
    def set_sound_item_count(_, instance: Sound):
        Retriever.set_repeat(Sound.sound_items, instance, instance.file_count)

    sound_id: int                  = Retriever(int16)
    play_delay: int                = Retriever(uint16)
    file_count: int                = Retriever(uint16)
    cache_time: int                = Retriever(int32, default=300000)

    total_probability_AOE1DE: int  = Retriever(int16, Version(DatVersion.AOE1DE.version_tuple()), Version(DatVersion.AOE1DE.version_tuple()))
    total_probability_AOE2DE: int  = Retriever(int16, Version(DatVersion.AOE2_DE_START.version_tuple()), Version(DatVersion.AOE2_DE_LATEST.version_tuple()))

    sound_items: list[SoundItem]   = Retriever(SoundItem, default=SoundItem(), on_set=[set_sound_item_count])

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

