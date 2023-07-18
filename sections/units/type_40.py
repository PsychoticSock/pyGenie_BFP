from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version, RetrieverCombiner
from binary_file_parser.types import int8, uint8, int16, float32, int32, uint32, Array16

from dat_file_locations import Dat
from sections.units.unit_command import UnitCommand


class Type40(BaseStruct):
    default_task_id: int               = Retriever(int16, default=0)
    search_radius: float               = Retriever(float32, default=0)
    work_rate: float                   = Retriever(float32, default=0)

    drop_sites_1: list[int]            = Retriever(int16, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()), default=[], repeat=3)
    drop_sites_2: list[int]            = Retriever(int16, Version(Dat.AOE1_1997.ver()), Version(Dat.SWGB_EXPANSION.ver()), default=[], repeat=2)

    drop_sites                         = RetrieverCombiner([drop_sites_1, drop_sites_2])

    task_group: int                    = Retriever(int8, default=0)
    command_sound_id: int              = Retriever(int16, default=0)
    stop_sound_id: int                 = Retriever(int16, default=0)


    wwise_command_sound_id: int        = Retriever(uint32,  Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()), default=0)
    wwise_stop_sound_id: int           = Retriever(uint32, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()), default=0)

    run_pattern: int                   = Retriever(int8, default=0)


    unit_commands_1: list[UnitCommand] = Retriever(Array16[UnitCommand], Version(Dat.AOE1_1997.ver()), Version(Dat.AOE1DE.ver()), default=[])
    unit_commands_2: list[UnitCommand] = Retriever(Array16[UnitCommand], Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()), default=[])

    unit_commands = RetrieverCombiner([unit_commands_1, unit_commands_2])

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

