from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version, RetrieverCombiner
from binary_file_parser.types import int8, uint8, int16, float32, Array16

from dat_file_locations import Dat
from sections.units.hit_type import HitType


class AttackingUnit(BaseStruct):
    default_armor_1: int            = Retriever(uint8, Version(Dat.AOE1_1997.ver()), Version(Dat.AOE1DE_ORIGINAL.ver()),            default=0)
    default_armor_2: int            = Retriever(int16, Version(Dat.AOE1DE.ver()), Version(Dat.AOE1DE.ver()),                        default=0)
    default_armor_3: int            = Retriever(uint8, Version(Dat.AOE2_AOK_1999.ver()),    Version(Dat.AOE2_AOK_1999.ver()),       default=0)
    default_armor_4: int            = Retriever(int16, Version(Dat.AOE2_CONQUERORS_2000.ver()),    Version(Dat.AOE2_HD_DLC.ver()),  default=0)
    default_armor_5: int            = Retriever(int16, Version(Dat.SWGB.ver()), Version(Dat.SWGB_EXPANSION.ver()),                  default=0)

    default_armor_6: int            = Retriever(int16, Version(Dat.AOE2_DE_START.ver()),    Version(Dat.AOE2_DE_LATEST.ver()),      default=0)
    default_armor: int              = RetrieverCombiner([default_armor_1, default_armor_2, default_armor_3, default_armor_4, default_armor_5])  #Base armor

    attacks_1: list[int]            = Retriever(Array16[HitType], Version(Dat.AOE1_1997.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=[])
    armors_1: list[int]             = Retriever(Array16[HitType], Version(Dat.AOE1_1997.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=[])


    boundary_id: int                = Retriever(int16,                                                                              default=0)

    bonus_damage_resistance: float  = Retriever(float32, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),       default=0)

    weapon_range_max: float         = Retriever(float32,                                                                            default=0)
    blast_range: float              = Retriever(float32,                                                                            default=0)
    attack_speed: float             = Retriever(float32,                                                                            default=0)         # = "reload time"
    projectile_id0: int             = Retriever(int16,                                                                              default=0)
    accuracy: int                   = Retriever(int16,                                                                              default=0)
    break_off_combat: int           = Retriever(int8,                                                                               default=0)
    frame_delay: int                = Retriever(int16,                                                                              default=0)
    weapon_offset: float            = Retriever(float32,                                                                            default=0, repeat=3)
    blast_level_offence: int        = Retriever(uint8,                                                                              default=0)
    weapon_range_min: float         = Retriever(float32,                                                                            default=0)

    accuracy_dispersion: float      = Retriever(float32, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),       default=0)

    attack_sprite_id: int           = Retriever(int16,                                                                              default=0)
    melee_armor_displayed: int      = Retriever(int16,                                                                              default=0)
    attack_displayed: int           = Retriever(int16,                                                                              default=0)
    range_displayed: float          = Retriever(float32,                                                                            default=0)
    reload_time_displayed: float    = Retriever(float32,                                                                            default=0)
    blast_damage: float             = Retriever(float32, Version(Dat.AOE2_DE_LATEST.ver()), Version(Dat.AOE2_DE_LATEST.ver()),      default=0)  # This will need changing later - was added recently

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

