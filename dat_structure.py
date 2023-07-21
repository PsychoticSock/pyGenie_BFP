from __future__ import annotations

from dat_file_locations import Dat

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import ByteStream, int8, uint16, uint32, Array16, Array32, Bytes

from sections.civs.civ import Civ
from sections.effects.effect_bundle import EffectBundle
from file_header import FileHeader
from sections.graphics.graphics import Graphics
from sections.map.maps import Maps
from sections.player_color.player_colour import PlayerColour
from sections.sounds.sounds import Sounds
from sections.tech.tech import Tech
from sections.tech_trees.tech_trees import TechTrees
from sections.terrain.terraindata import TerrainData
from sections.terrain_tables.terrain_tables import TerrainTables
from sections.units.unit_header import UnitHeader
from sections.units.unit_line import UnitLine


class DatStructure(BaseStruct):
    @staticmethod
    def set_terrain_restriction_count(_, instance: DatStructure):
        Retriever.set_repeat(DatStructure.float_ptr_terrain_tables, instance, instance.terrain_restriction_count)
        Retriever.set_repeat(DatStructure.terrain_pass_graphics_ptrs, instance, instance.terrain_restriction_count)
        Retriever.set_repeat(DatStructure.terrain_tables, instance, instance.terrain_restriction_count)

    @staticmethod
    def check_AOC_subversion(_, instance: DatStructure):
        current_version = (instance.struct_ver)
        if(5,7)<=instance.struct_ver<(5,8):
            if instance.maps.random_map_ptr == 237568256:
                if(sum(instance.float_ptr_terrain_tables) < 1000):
                    # AOE2 HD (No expansions)
                    current_version = (5,7,2,3)
                else:
                    # print("AOC_10c")
                    # AOE2: The Conquerors 1.0c
                    current_version = (5, 7, 2, 2)
            if instance.maps.random_map_ptr == 41867488:
                # AOE2: The Conquerors 2000
                current_version = (5, 7, 2, 1)
        instance.struct_ver=current_version

    # @formatter:off
    file_header: FileHeader                 = Retriever(FileHeader,                                                 default=FileHeader()) #, remaining_compressed=True)  # Need to remove this is BFP supports compression
    civ_count_swgb: int                     = Retriever(uint16, Version(Dat.SWGB.ver()), Version(Dat.SWGB_EXPANSION.ver()),   default=0)
    unknown_swgb_01: int                    = Retriever(uint32, Version(Dat.SWGB.ver()), Version(Dat.SWGB_EXPANSION.ver()),   default=0)
    unknown_swgb_02: int                    = Retriever(uint32, Version(Dat.SWGB.ver()), Version(Dat.SWGB_EXPANSION.ver()),   default=0)
    blend_mode_count_swgb: int              = Retriever(uint32, Version(Dat.SWGB.ver()), Version(Dat.SWGB_EXPANSION.ver()),   default=0)
    blend_mode_count_max_swgb: int          = Retriever(uint32, Version(Dat.SWGB.ver()), Version(Dat.SWGB_EXPANSION.ver()),   default=0)
    terrain_restriction_count: int          = Retriever(uint16,                                                     default=0, on_set=[set_terrain_restriction_count])
    terrain_count: int                      = Retriever(uint16,                                                     default=0)
    float_ptr_terrain_tables:   list[int]   = Retriever(uint32,                                                     default=0)
    terrain_pass_graphics_ptrs: list[int]   = Retriever(uint32, min_ver=Version(Dat.AOE2_AOK_1999.ver()),
                                                                        max_ver=Version(Dat.AOE2_DE_LATEST.ver()),  default=0)  # This version information might be wrong but just a placeholder for now
    terrain_tables:   list[TerrainTables]   = Retriever(TerrainTables,                                              default=TerrainTables(), repeat=0)
    player_colour: PlayerColour             = Retriever(PlayerColour,                                               default=PlayerColour())
    sounds: Sounds                          = Retriever(Sounds,                                                     default=Sounds())
    graphics:  Graphics                     = Retriever(Graphics,                                                   default=Graphics())
    terrains:  TerrainData                  = Retriever(TerrainData,                                                default=TerrainData())

    maps: Maps                              = Retriever(Maps,                                                       default=Maps(), on_set=[check_AOC_subversion])

    effectbundles: list[EffectBundle]       = Retriever(Array32[EffectBundle],                                      default=[])

    unit_lines: list[UnitLine]              = Retriever(Array16[UnitLine],   Version(Dat.SWGB.ver()),
                                                                                Version(Dat.SWGB.ver()),            default=[])
    unit_headers: list[UnitHeader]          = Retriever(Array32[UnitHeader], Version(Dat.AOE2_AOK_1999.ver()),
                                                                                Version(Dat.AOE2_DE_LATEST.ver()),  default=[])

    #civ_count: int                          = Retriever(int16,                                                      default=0) # For testing purposes
    #civ: Civ                                = Retriever(Civ, default=Civ(), repeat=1)                                          # For testing purposes
    civs: list[Civ]                         = Retriever(Array16[Civ],                                               default=[])

    unknown_swgb_03: int                    = Retriever(int8, Version(Dat.SWGB.ver()), Version(Dat.SWGB_EXPANSION.ver()),   default=0)

    #tech_count: int                         = Retriever(uint16,                                                     default=0)
    #techs: Tech                             = Retriever(Tech,                                                       default=Tech(), repeat=10)
    techs: list[Tech]                       = Retriever(Array16[Tech], default=Tech())

    unknown_swgb_4: int                    = Retriever(int8, Version(Dat.SWGB.ver()), Version(Dat.SWGB_EXPANSION.ver()),   default=0)

    tech_trees: TechTrees                   = Retriever(TechTrees, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),  default=TechTrees())
    #last_bytes: int                    = Retriever(Bytes[1],   default=0)

    # @formatter:on

    @classmethod
    def get_version(
            cls,
            stream: ByteStream,
            struct_ver: Version = Version((0,)),
            parent: BaseStruct = None,
    ) -> Version:
        ver_str = stream.peek(8).decode('ascii')
        ver_str = ver_str.replace("VER ", '').rstrip('\x00')
        output_ver = Version(tuple(map(int, ver_str.split("."))))
        output_ver = stream.check_if_needs_subversion(output_ver)
        return output_ver

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, initialise_defaults=True, **retriever_inits):
        super().__init__(struct_ver, parent, initialise_defaults=initialise_defaults, **retriever_inits)