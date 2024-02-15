from __future__ import annotations


from class_for_copying import DatFileObject

from class_for_copying import DatFileObject
from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int8, int16, float32, int32, Bytes

from dat_file_locations import Dat
from sections.units.resource_cost import ResourceCost


class Type70(BaseStruct, DatFileObject):
    resource_cost: list[ResourceCost]       = Retriever(ResourceCost,                                                                       default=ResourceCost(), repeat=3)
    creation_time: int                      = Retriever(int16,                                                                              default=0)
    train_location_i: int                   = Retriever(int16,                                                                              default=0)
    creation_button_id: int                 = Retriever(int8,                                                                               default=0)


    heal_timer: float                   = Retriever(float32, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),           default=0)

    rear_attack_modifier: float         = Retriever(float32, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.SWGB_EXPANSION.ver()),           default=0)

    flank_attack_modifier: float        = Retriever(float32, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),           default=0)
    creatable_type: int                 = Retriever(int8,    Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),           default=0)
    hero_mode: int                      = Retriever(int8,    Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),           default=0)
    garrison_graphic: int               = Retriever(int32,   Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),           default=0)


    spawn_graphic_id: int               = Retriever(int16,   Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),           default=0)
    upgrade_graphic_id: int             = Retriever(int16,   Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),           default=0)
    hero_glow_graphic_id: int           = Retriever(int16,   Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),           default=0)
    max_charge: float                   = Retriever(float32, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),           default=0)
    charge_regen_rate: float            = Retriever(float32, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),           default=0)
    charge_cost: int                    = Retriever(int16,   Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),           default=0)
    charge_type: int                    = Retriever(int16,   Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),           default=0)

    unknown_12_bytes: bytes                   = Retriever(Bytes[12], Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),   default=0)

    projectile_min_count: float                 = Retriever(float32, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),   default=0)
    projectile_max_count: int                   = Retriever(int8,    Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),   default=0)
    projectile_spawning_area_width: float       = Retriever(float32,  Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    projectile_spawning_area_length: float      = Retriever(float32,  Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    projectile_spawning_area_randomness: float  = Retriever(float32,  Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    projectile_id1: int                         = Retriever(int32,    Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    special_graphic_id: int                     = Retriever(int32,    Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    special_activation: int                     = Retriever(int8,     Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0) # Special Ability


    pierce_armor_displayed: int                 = Retriever(int16,                                                                          default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

