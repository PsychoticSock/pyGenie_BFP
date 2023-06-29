from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int32, int16, uint16, FixedLenStr, str8, nt_str8

from dat_file_locations import DatVersion


class SoundItem(BaseStruct):
    #@staticmethod
    #def set_name_length(_, instance: SoundItem):
        #pass
        #Retriever.set_repeat(SoundItem.sound_name, instance, instance.name_len)

    # @formatter:off
    name_len_debug_aoe1de: int  = Retriever(uint16,     min_ver=DatVersion.AOE1DE.version_tuple(), max_ver=DatVersion.AOE1DE.version_tuple(), default=0)
    name_len_aoe1de: int        = Retriever(uint16,     min_ver=DatVersion.AOE1DE.version_tuple(), max_ver=DatVersion.AOE1DE.version_tuple(), default=0) #, on_set=[set_name_length])
    sound_name_aoe1de: int      = Retriever(nt_str8,    min_ver=DatVersion.AOE1DE.version_tuple(), max_ver=DatVersion.AOE1DE.version_tuple(), default=0)
    name_len_debug_aoe2de: int  = Retriever(uint16,     min_ver=DatVersion.AOE2_DE_START.version_tuple(), max_ver=DatVersion.AOE2_DE_LATEST.version_tuple(), default=0)
    name_len_aoe2de: int        = Retriever(uint16,     min_ver=DatVersion.AOE2_DE_START.version_tuple(), max_ver=DatVersion.AOE2_DE_LATEST.version_tuple(), default=0) #, on_set=[set_name_length])
    sound_name_aoe2de: int      = Retriever(str8,    min_ver=DatVersion.AOE2_DE_START.version_tuple(), max_ver=DatVersion.AOE2_DE_LATEST.version_tuple(), default=0)

    #########
    filename_SWGB: str      = Retriever(FixedLenStr[27], DatVersion.SWGB.version_tuple(), Version(DatVersion.SWGB.version_tuple()), default=0)
    filename: str           = Retriever(FixedLenStr[13], min_ver=DatVersion.AOE1_1997.version_tuple(), max_ver=DatVersion.AOE2_HD_DLC.version_tuple(), default=0)

    resource_id: int        = Retriever(int32)
    probablilty: int        = Retriever(int16)

    civilization_id: int    = Retriever(int16, min_ver=Version(DatVersion.AOE2_AOK_1999.version_tuple()),
                                                              max_ver=Version(DatVersion.AOE2_DE_LATEST.version_tuple()),                                       default=0)
    icon_set: int           = Retriever(int16, min_ver=Version(DatVersion.AOE2_AOK_1999.version_tuple()),
                                                              max_ver=Version(DatVersion.AOE2_DE_LATEST.version_tuple()),                                       default=0)

    def __init__(self, struct_ver: Version=Version((0,)), parent: BaseStruct=None, idx: int=-1, initialise_defaults: bool=True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)