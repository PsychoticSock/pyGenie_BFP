from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version

from dat_file_locations import Dat
from sections.sounds.sound_prop import DE2SoundProp, SoundProp


class GraphicAttackSounds(BaseStruct):
    sound_props: list[SoundProp]            = Retriever(SoundProp, min_ver=Dat.AOE1_1997.ver(), max_ver=Dat.SWGB.ver(), repeat=3, default=SoundProp())
    sound_props_AOE2DE: list[DE2SoundProp]  = Retriever(DE2SoundProp, min_ver=Dat.AOE2_DE_START.ver(), default=DE2SoundProp())

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)


