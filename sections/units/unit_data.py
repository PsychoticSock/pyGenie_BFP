from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int8, uint16, int16, str16, int32, Array16, FixedLenStr, float32

#from sections.units.Type10 import Type10
from sections.units.attacking_unit import AttackingUnit
from sections.units.type_10 import Type10
from sections.units.type_20 import Type20
from sections.units.type_25 import Type25
from sections.units.type_30 import Type30
from sections.units.type_40 import Type40
from sections.units.type_60 import Type60
from sections.units.type_70 import Type70


class UnitData(BaseStruct):
    @staticmethod
    def enable_type_properties(_, instance: UnitData):
        if instance.unit_type >= 20:
            Retriever.set_repeat(UnitData.type_20, instance, 1)
        if instance.unit_type >= 25:
            Retriever.set_repeat(UnitData.type_25, instance, 1)
        if instance.unit_type >= 30:
            Retriever.set_repeat(UnitData.type_30, instance, 1)
        if instance.unit_type >= 40:
            Retriever.set_repeat(UnitData.type_40, instance, 1)
        if instance.unit_type == 60:
            Retriever.set_repeat(UnitData.type_60, instance, 1)
        if instance.unit_type > 60:
            Retriever.set_repeat(UnitData.attacking_type, instance, 1)
        if instance.unit_type >= 70:
            Retriever.set_repeat(UnitData.type_70, instance, 1)
        #if instance.unit_type >= 80:
        #    Retriever.set_repeat(UnitData.type_80, instance, 1)
        #if instance.unit_type >= 90:
        #    Retriever.set_repeat(UnitData.type_90, instance, 1)

    unit_type: int = Retriever(int8, default=0, on_set=[enable_type_properties])

    type_10: int         = Retriever(Type10,        default=Type10())
    type_20: int         = Retriever(Type20,        default=Type20(),        repeat=-1)
    type_25: int         = Retriever(Type25,        default=Type25(),        repeat=-1)
    type_30: int         = Retriever(Type30,        default=Type30(),        repeat=-1)
    type_40: int         = Retriever(Type40,        default=Type40(),        repeat=-1)
    type_60: int         = Retriever(Type60,        default=Type60(),        repeat=-1)
    attacking_type: int  = Retriever(AttackingUnit, default=AttackingUnit(), repeat=-1)
    type_70: int         = Retriever(Type70,        default=Type70(),        repeat=-1)
    #type_80: int    = Retriever(Type80, default=Type80(), repeat=-1)
    #type_90: int    = Retriever(Type90, default=Type90(), repeat=-1)"""

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

