from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int8, uint8, int16, float32, Bytes, int32

from dat_file_locations import Dat

class Type30(BaseStruct):
    move_graphics: int                            = Retriever(int16,     default=0)
    run_graphics: int                             = Retriever(int16,     default=0)
    turn_speed: float                             = Retriever(float32,   default=0)  #Rotation speed
    old_size_class: int                           = Retriever(int8,      default=0)  #Size class
    trail_unit_id: int                            = Retriever(int16,     default=0)
    trail_options: int                            = Retriever(uint8,     default=0)  #Trail mode
    trail_spacing: float                          = Retriever(float32,   default=0)  #Trail density
    old_move_algorithm: int                       = Retriever(int8,      default=0)  #Move algorithm


    turn_radius: float                            = Retriever(float32, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    turn_radius_speed: float                      = Retriever(float32, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    max_yaw_per_sec_moving: float                 = Retriever(float32, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    stationary_yaw_revolution_time: float         = Retriever(float32, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    max_yaw_per_sec_stationary: float             = Retriever(float32, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)

    min_collision_size_multiplier: float          = Retriever(float32, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=0)


    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

