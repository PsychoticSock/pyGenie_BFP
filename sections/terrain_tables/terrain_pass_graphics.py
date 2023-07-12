from binary_file_parser import BaseStruct, Retriever, Version, RetrieverCombiner
from binary_file_parser.types import float32, int32

from dat_file_locations import Dat


class TerrainPassGraphics(BaseStruct):

    # @formatter:off
    slp_id_exit_tile: int           = Retriever(int32,                                                                     default=1)
    slp_id_enter_tile: int          = Retriever(int32,                                                                     default=1)
    slp_id_walk_tile: int           = Retriever(int32,                                                                     default=1)
    replication_amount_aoe1_HD: int = Retriever(int32,   min_ver=Dat.AOE1DE.ver(), max_ver=Dat.AOE2_HD_DLC.ver(),          default=1)
    walk_sprite_rate: float         = Retriever(float32, min_ver=Version(Dat.SWGB.ver()), max_ver=Version(Dat.SWGB.ver()), default=1)
    replication_amount_DE: int      = Retriever(int32,   min_ver=Dat.AOE2_DE_LATEST.ver(),                                 default=1)
    replication_amount: int         = RetrieverCombiner([replication_amount_aoe1_HD, replication_amount_DE])

    def __init__(self, struct_ver: Version=Version((0,)), parent: BaseStruct=None, idx: int=-1, initialise_defaults: bool=True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

