from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import uint8, float32

from sections.units.attacking_unit import AttackingUnit


class Type60(BaseStruct):

    attacking_type: int  = Retriever(AttackingUnit, default=AttackingUnit(), repeat=1)

    projectile_type: int         = Retriever(uint8,      default=0)
    smart_mode: int              = Retriever(uint8,      default=0)
    drop_animation_mode: int     = Retriever(uint8,      default=0)
    penetration_mode: int        = Retriever(uint8,      default=0)
    area_of_effect_special: int  = Retriever(uint8,      default=0)
    projectile_arc: float        = Retriever(float32,   default=0)


    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

