from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import uint16, uint32


from dat_file_locations import Dat
from graphic import GraphicDataDE, GraphicDataSWGB, GraphicDataAOE1, GraphicDataCommon

class Graphics(BaseStruct):
    @staticmethod
    def set_graphic_pointer_count(_, instance: Graphics):
        Retriever.set_repeat(Graphics.graphic_pointers, instance, instance.graphic_count)
    @staticmethod
    def set_graphic_item_count(_, instance: Graphics):
        Retriever.set_repeat(Graphics.graphics_data_de1, instance, sum(instance.graphic_pointers))  #instance.graphic_count)
        Retriever.set_repeat(Graphics.graphics_data_de2, instance, sum(instance.graphic_pointers))  #instance.graphic_count)
        Retriever.set_repeat(Graphics.graphics_data_swgb, instance, sum(instance.graphic_pointers)) #instance.graphic_count)
        Retriever.set_repeat(Graphics.graphics_data_aoe1, instance, sum(instance.graphic_pointers)) #instance.graphic_count)

    graphic_count: int                            = Retriever(uint16,                                            default=0, on_set=[set_graphic_pointer_count])
    graphic_pointers: list[int]                   = Retriever(uint32,                                            default=0, on_set=[set_graphic_item_count])  # If a pointer is set to 0, makes the entry "nonexistent"
    graphics_data_de1: list[GraphicDataDE]        = Retriever(GraphicDataDE,   min_ver=Dat.AOE1DE.ver(),
                                                                           max_ver=Dat.AOE2_HD_DLC.ver(),        default=GraphicDataDE())
    graphics_data_de2: list[GraphicDataDE]        = Retriever(GraphicDataDE,   min_ver=Dat.AOE2_DE_START.ver(),
                                                                           max_ver=Dat.AOE2_DE_LATEST.ver(),     default=GraphicDataDE())
    graphics_data_swgb: list[GraphicDataSWGB]     = Retriever(GraphicDataSWGB, min_ver=Dat.SWGB.ver(),
                                                                           max_ver=Dat.SWGB.ver(),               default=GraphicDataSWGB())

    graphics_data_aoe1: list[GraphicDataAOE1]     = Retriever(GraphicDataAOE1,   min_ver=Dat.AOE1_1997.ver(),
                                                                           max_ver=Dat.AOE1DE_CLASSIC.ver(),     default=GraphicDataDE())

