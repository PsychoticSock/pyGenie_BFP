from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version, RetrieverCombiner
from binary_file_parser.types import int8, uint8, int16, float32, Array16

from dat_file_locations import Dat
from sections.units.hit_type import HitType


class Type60(BaseStruct):
    projectile_type: int         = Retriever(int8,      default=0)
    smart_mode: int              = Retriever(int8,      default=0)
    drop_animation_mode: int     = Retriever(int8,      default=0)
    penetration_mode: int        = Retriever(int8,      default=0)
    area_of_effect_special: int  = Retriever(int8,      default=0)
    projectile_arc: float        = Retriever(float32,   default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

