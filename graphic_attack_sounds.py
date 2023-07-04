from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version

from sound_prop import DE2SoundProp, SoundProp


class GraphicAttackSounds(BaseStruct):
    sound_props_AOE2DE: list[DE2SoundProp]  = Retriever(DE2SoundProp, default=DE2SoundProp())
    sound_props: list[SoundProp]            = Retriever(SoundProp, repeat=3, default=DE2SoundProp())

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)


