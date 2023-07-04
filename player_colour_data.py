from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int32, int16, uint16, uint8, FixedLenStr


class PlayerColourData_AOE2_SWGB(BaseStruct):

    # @formatter:off
    id: int                      = Retriever(int32,  default=0)
    player_color_base: int       = Retriever(int32,  default=0)
    outline_color: int           = Retriever(int32,  default=0)
    unit_selection_color1: int   = Retriever(int32,  default=0)
    unit_selection_color2: int   = Retriever(int32,  default=0)
    minimap_color1: int          = Retriever(int32,  default=0)
    minimap_color2: int          = Retriever(int32,  default=0)
    minimap_color3: int          = Retriever(int32,  default=0)
    statistics_text_color: int   = Retriever(int32,  default=0)

    def __init__(self, struct_ver: Version=Version((0,)), parent: BaseStruct=None, idx: int=-1, initialise_defaults: bool=True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

class PlayerColourDataAOE1(BaseStruct):

    # @formatter:off
    colour_name: int     = Retriever(FixedLenStr[30], default=0)
    id: int              = Retriever(int16,           default=0)
    resource_id: int     = Retriever(uint16,          default=0)
    minimap_color: int   = Retriever(uint8,           default=0)
    type: int            = Retriever(uint8,           default=0)


    def __init__(self, struct_ver: Version=Version((0,)), parent: BaseStruct=None, idx: int=-1, initialise_defaults: bool=True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)