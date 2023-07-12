from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int8, uint16, int16, str16, int32, Array16, FixedLenStr, float32

#from sections.units.Type10 import Type10

class UnitData(BaseStruct):
    @staticmethod
    def turn_off_all(_, instance: UnitData):
        pass#.set_repeat(UnitData.type_20, instance, -1)
            #Retriever.set_repeat(UnitData.type_30, instance, -1)
            #Retriever.set_repeat(UnitData.type_40, instance, -1)
            #Retriever.set_repeat(UnitData.type_50, instance, -1)
            #Retriever.set_repeat(UnitData.type_60, instance, -1)
            #Retriever.set_repeat(UnitData.type_70, instance, -1)
            #Retriever.set_repeat(UnitData.type_80, instance, -1)
            #Retriever.set_repeat(UnitData.type_90, instance, -1)

    @staticmethod
    def enable_type_properties(_, instance: UnitData):
        pass#if instance.unit_type >= 20:
        pass#    Retriever.set_repeat(UnitData.type_20, instance, 1)
        pass#if instance.unit_type >= 30:
        pass#    Retriever.set_repeat(UnitData.type_30, instance, 1)
        pass#if instance.unit_type >= 40:
        pass#    Retriever.set_repeat(UnitData.type_40, instance, 1)
        pass#if instance.unit_type >= 50:
        pass#    Retriever.set_repeat(UnitData.type_50, instance, 1)
        pass#if instance.unit_type >= 60:
        pass#    Retriever.set_repeat(UnitData.type_60, instance, 1)
        pass#if instance.unit_type >= 70:
        pass#    Retriever.set_repeat(UnitData.type_70, instance, 1)
        pass#if instance.unit_type >= 80:
        pass#    Retriever.set_repeat(UnitData.type_80, instance, 1)
        pass#if instance.unit_type >= 90:
        pass#    Retriever.set_repeat(UnitData.type_90, instance, 1)

    unit_type: int = Retriever(int8, default=0, on_set=[turn_off_all, enable_type_properties])

    #type_10: int    = Retriever(Type10, default=Type10())
    #type_20: int    = Retriever(Type20, default=0, repeat=-1)
    #type_30: int    = Retriever(Type30, default=0, repeat=-1)
    #type_40: int    = Retriever(Type40, default=0, repeat=-1)
    #type_50: int    = Retriever(Type50, default=0, repeat=-1)
    #type_60: int    = Retriever(Type60, default=0, repeat=-1)
    #type_70: int    = Retriever(Type70, default=0, repeat=-1)
    #type_80: int    = Retriever(Type80, default=0, repeat=-1)
    #type_90: int    = Retriever(Type90, default=0, repeat=-1)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

