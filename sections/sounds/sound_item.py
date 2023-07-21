from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int32, int16, uint16, FixedLenStr, str16

from dat_file_locations import Dat


class SoundItem(BaseStruct):

    # @formatter:off
    name_len_debug_aoe1de: int  = Retriever(uint16,          min_ver=Dat.AOE1DE.ver(),          max_ver=Dat.AOE1DE.ver(),           default=0)
    sound_name_aoe1de: str      = Retriever(str16,           min_ver=Dat.AOE1DE.ver(),          max_ver=Dat.AOE1DE.ver(),           default=0)
    name_len_debug_aoe2de: int  = Retriever(uint16,          min_ver=Dat.AOE2_DE_START.ver(),   max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)
    sound_name_aoe2de: str      = Retriever(str16,           min_ver=Dat.AOE2_DE_START.ver(),   max_ver=Dat.AOE2_DE_LATEST.ver(),   default=0)
    filename_SWGB: str          = Retriever(FixedLenStr[27], Version(Dat.SWGB.ver()),           Version(Dat.SWGB.ver()),            default=0)
    filename: str               = Retriever(FixedLenStr[13], min_ver=Dat.AOE1_1997.ver(),       max_ver=Dat.AOE1_RoR_1998.ver(),    default=0)
    filename2: str              = Retriever(FixedLenStr[13], min_ver=Dat.AOE2_AOK_1999.ver(),   max_ver=Dat.AOE2_HD_DLC.ver(),      default=0)

    resource_id: int            = Retriever(int32)
    probablilty: int            = Retriever(int16)

    civilization_id: int        = Retriever(int16,           min_ver=Version(Dat.AOE2_AOK_1999.ver()),
                                                             max_ver=Version(Dat.AOE2_DE_LATEST.ver()),                             default=0)
    icon_set: int               = Retriever(int16,           min_ver=Version(Dat.AOE2_AOK_1999.ver()),
                                                             max_ver=Version(Dat.AOE2_DE_LATEST.ver()),                             default=0)

    def __init__(self, struct_ver: Version=Version((0,)), parent: BaseStruct=None, idx: int=-1, initialise_defaults: bool=True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)