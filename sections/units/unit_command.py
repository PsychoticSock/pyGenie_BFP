from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int8, int16, uint32, float32

from dat_file_locations import Dat


class UnitCommand(BaseStruct):
    command_used: int                       = Retriever(int16,                                                                       default=0)
    command_id: int                         = Retriever(int16,                                                                       default=0)
    is_default: int                         = Retriever(int8,                                                                        default=0)

    command_ability: int                    = Retriever(int16,                                                                       default=0)

    class_id: int                           = Retriever(int16,                                                                       default=0)
    unit_id: int                            = Retriever(int16,                                                                       default=0)
    terrain_id: int                         = Retriever(int16,                                                                       default=0)
    resource_in: int                        = Retriever(int16,                                                                       default=0)

    resource_multiplier: int                = Retriever(int16,                                                                       default=0)
    resource_out: int                       = Retriever(int16,                                                                       default=0)
    unused_resource: int                    = Retriever(int16,                                                                       default=0)
    work_value1: float                      = Retriever(float32,                                                                     default=0)
    work_value2: float                      = Retriever(float32,                                                                     default=0)
    work_range: float                       = Retriever(float32,                                                                     default=0)
    search_mode: int                        = Retriever(int8,                                                                        default=0)
    searchime: float                        = Retriever(float32,                                                                     default=0)
    enableargeting: int                     = Retriever(int8,                                                                        default=0)
    combat_level_flag: int                  = Retriever(int8,                                                                        default=0)
    gatherype: int                          = Retriever(int16,                                                                       default=0)
    work_mode2: int                         = Retriever(int16,                                                                       default=0)
    target_diplomacy: int                   = Retriever(int8,                                                                        default=0)

    carry_check: int                        = Retriever(int8,                                                                        default=0)
    state_build: int                        = Retriever(int8,                                                                        default=0)

    move_sprite_id: int                     = Retriever(int16,                                                                       default=0)
    proceed_sprite_id: int                  = Retriever(int16,                                                                       default=0)
    work_sprite_id: int                     = Retriever(int16,                                                                       default=0)
    carry_sprite_id: int                    = Retriever(int16,                                                                       default=0)
    resource_gather_sound_id: int           = Retriever(int16,                                                                       default=0)
    resource_deposit_sound_id: int          = Retriever(int16,                                                                       default=0)

    wwise_resource_gather_sound_id: int     = Retriever(uint32, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()), default=0)
    wwise_resource_deposit_sound_id: int    = Retriever(uint32, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()), default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

