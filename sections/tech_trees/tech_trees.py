from __future__ import annotations


from class_for_copying import DatFileObject
from binary_file_parser import Retriever, BaseStruct, Version, RetrieverCombiner
from binary_file_parser.types import uint8, uint16, int32

from dat_file_locations import Dat
from sections.tech_trees.age_tech_tree import AgeTechTree
from sections.tech_trees.building_connection import BuildingConnection
from sections.tech_trees.research_connection import TechConnection
from sections.tech_trees.unit_connection import UnitConnection


class TechTrees(BaseStruct, DatFileObject):
    @staticmethod
    def set_age_connection_count(_, instance: TechTrees):
        Retriever.set_repeat(TechTrees.age_connections, instance, instance.age_connection_count)
    @staticmethod
    def set_building_connection_count(_, instance: TechTrees):
        Retriever.set_repeat(TechTrees.building_connections, instance, instance.building_connection_count)
    @staticmethod
    def set_unit_connection_count(_, instance: TechTrees):
        try:
            Retriever.set_repeat(TechTrees.unit_connections, instance, instance.unit_connection_count)
        except:
            print("Failed to execute: set_unit_connection_count")
    @staticmethod
    def set_tech_connection_count(_, instance: TechTrees):
        Retriever.set_repeat(TechTrees.tech_connections, instance, instance.tech_connection_count)

    time_slice: int                             = Retriever(int32,                                                                              default=0)
    unit_kill_rate: int                         = Retriever(int32,                                                                              default=0)
    unit_kill_total: int                        = Retriever(int32,                                                                              default=0)
    unit_hitpoint_rate: int                     = Retriever(int32,                                                                              default=0)
    unit_hitpoint_total: int                    = Retriever(int32,                                                                              default=0)
    razing_kill_rate: int                       = Retriever(int32,                                                                              default=0)
    razing_kill_total: int                      = Retriever(int32,                                                                              default=0)

    age_connection_count: int                   = Retriever(uint8,                                                                              default=0, on_set=[set_age_connection_count])
    building_connection_count: int              = Retriever(uint8,                                                                              default=0, on_set=[set_building_connection_count])

    unit_connection_count_1: int                = Retriever(uint16,    Version(Dat.SWGB.ver()),             Version(Dat.SWGB_EXPANSION.ver()),  default=0)
    unit_connection_count_2: int                = Retriever(uint8,     Version(Dat.AOE1_1997.ver()),        Version(Dat.AOE2_HD_DLC.ver()),     default=0)
    unit_connection_count_3: int                = Retriever(uint8,     Version(Dat.AOE2_DE_START.ver()),    Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    unit_connection_count: int                  = RetrieverCombiner([unit_connection_count_1, unit_connection_count_2, unit_connection_count_3])

    tech_connection_count: int                  = Retriever(uint8,                                                                              default=0, on_set=[set_unit_connection_count])
    total_unit_tech_groups: int                 = Retriever(int32,                                                                              default=0, on_set=[set_tech_connection_count])

    age_connections: AgeTechTree                = Retriever(AgeTechTree,                                                                        default=AgeTechTree())
    building_connections: BuildingConnection    = Retriever(BuildingConnection,                                                                 default=BuildingConnection())
    unit_connections: UnitConnection            = Retriever(UnitConnection,                                                                     default=UnitConnection())
    tech_connections: TechConnection            = Retriever(TechConnection, default=TechConnection())

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

