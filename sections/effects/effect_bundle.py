from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version, RetrieverCombiner
from binary_file_parser.types import uint16, str16, FixedLenStr, Array16

from dat_file_locations import Dat
from sections.effects.effect import Effect


class EffectBundle(BaseStruct):

    effect_bundle_name_len_debug_aoe1de: int    = Retriever(uint16,             Version(Dat.AOE1DE.ver()),          Version(Dat.AOE1DE.ver()),         default=0)
    effect_bundle_name_aoe1de: str              = Retriever(str16,              Version(Dat.AOE1DE.ver()),          Version(Dat.AOE1DE.ver()),         default=0)

    effect_bundle_name_len_debug_aoe2de: int    = Retriever(uint16,             Version(Dat.AOE2_DE_START.ver()),   Version(Dat.AOE2_DE_LATEST.ver()), default=0)
    effect_bundle_name_aoe2de: str              = Retriever(str16,              Version(Dat.AOE2_DE_START.ver()),   Version(Dat.AOE2_DE_LATEST.ver()), default="")

    effect_bundle_name_aoe1: str                = Retriever(FixedLenStr[31],    Version(Dat.AOE1_1997.ver()),       Version(Dat.AOE1DE_CLASSIC.ver()), default=0)
    effect_bundle_name_swgb: str                = Retriever(FixedLenStr[31],    Version(Dat.AOE2_AOK_1999.ver()),   Version(Dat.SWGB_EXPANSION.ver()), default=0)

    effect_bundle_name: str                     = RetrieverCombiner([effect_bundle_name_aoe1de,
                                                                     effect_bundle_name_aoe2de,
                                                                     effect_bundle_name_aoe1,
                                                                     effect_bundle_name_swgb])

    effects: list[Effect]                       = Retriever(Array16[Effect],                                                                           default=[])

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)



