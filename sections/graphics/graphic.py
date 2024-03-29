from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import uint16, FixedLenStr, str16

from dat_file_locations import Dat
from sections.graphics.graphic_data_common import GraphicDataCommon


from class_for_copying import DatFileObject

class GraphicDataDE(BaseStruct, DatFileObject):

    name_len_debug: int                              = Retriever(uint16,                                     default=0)
    graphic_name: str                                = Retriever(str16,                                      default=0)
    filename_len_debug: int                          = Retriever(uint16,                                     default=0)
    graphic_filename: str                            = Retriever(str16,                                      default=0)
    particle_effect_name_len_debug: int              = Retriever(uint16,   min_ver=Dat.AOE2_DE_START.ver(),  default=0)
    particle_effect_name: str                        = Retriever(str16,    min_ver=Dat.AOE2_DE_START.ver(),  default=0)
    first_frame: int                                 = Retriever(uint16,   Version(Dat.AOE1DE.ver()),
                                                                           Version(Dat.AOE1DE.ver()),        default=0)

    graphics_data_common: list[GraphicDataCommon] = Retriever(GraphicDataCommon, default=GraphicDataCommon())

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):

        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)


class GraphicDataSWGB(BaseStruct, DatFileObject):

    graphic_internal_name: str                       = Retriever(FixedLenStr[25],                              default=0)
    graphic_sprite_name: str                         = Retriever(FixedLenStr[25],                              default=0)
    graphics_data_common: list[GraphicDataCommon]    = Retriever(GraphicDataCommon,                            default=GraphicDataCommon())

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)


class GraphicDataAOE1_2(BaseStruct, DatFileObject):
    graphic_internal_name: str                       = Retriever(FixedLenStr[21],                              default=0)
    graphic_sprite_name: str                         = Retriever(FixedLenStr[13],                              default=0)
    graphics_data_common: list[GraphicDataCommon]    = Retriever(GraphicDataCommon,                            default=GraphicDataCommon())

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

