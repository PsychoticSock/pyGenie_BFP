from __future__ import annotations


from class_for_copying import DatFileObject
from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import uint8, Array16

from sections.units.unit_command import UnitCommand


class UnitHeader(BaseStruct, DatFileObject):
    @staticmethod
    def enable_units_command_count(_, instance: UnitHeader):
        if not instance.exists:
            Retriever.set_repeat(UnitHeader.unit_commands, instance, -1)

    exists: int                         = Retriever(uint8, default=0, on_set=[enable_units_command_count])
    unit_commands: list[UnitCommand]    = Retriever(Array16[UnitCommand], default=[])

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

