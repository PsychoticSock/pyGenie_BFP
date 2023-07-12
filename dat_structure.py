from __future__ import annotations

from dat_file_locations import Dat

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import ByteStream, int16, uint16, uint32, Array16, Array32

from sections.civs.civ import Civ
from sections.effects.effect_bundle import EffectBundle
from file_header import FileHeader
from sections.graphics.graphics import Graphics
from sections.map.maps import Maps
from sections.player_color.player_colour import PlayerColour
from sections.sounds.sounds import Sounds
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

    # @formatter:off
    file_header: FileHeader                 = Retriever(FileHeader,                                                 default=FileHeader()) #, remaining_compressed=True)  # Need to remove this is BFP supports compression
    civ_count_swgb: int                     = Retriever(uint16, Version(Dat.SWGB.ver()), Version(Dat.SWGB.ver()),   default=0)
    unknown_swgb_01: int                    = Retriever(uint32, Version(Dat.SWGB.ver()), Version(Dat.SWGB.ver()),   default=0)
    unknown_swgb_02: int                    = Retriever(uint32, Version(Dat.SWGB.ver()), Version(Dat.SWGB.ver()),   default=0)
    blend_mode_count_swgb: int              = Retriever(uint32, Version(Dat.SWGB.ver()), Version(Dat.SWGB.ver()),   default=0)
    blend_mode_count_max_swgb: int          = Retriever(uint32, Version(Dat.SWGB.ver()), Version(Dat.SWGB.ver()),   default=0)
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

    maps: Maps                              = Retriever(Maps,                                                       default=Maps())

    effectbundles: list[EffectBundle]       = Retriever(Array32[EffectBundle],                                      default=[])

    unit_lines: list[UnitLine]              = Retriever(Array16[UnitLine],   Version(Dat.SWGB.ver()),
                                                                                Version(Dat.SWGB.ver()),            default=[])
    unit_headers: list[UnitHeader]          = Retriever(Array32[UnitHeader], Version(Dat.AOE2_AOK_1999.ver()),
                                                                                Version(Dat.AOE2_DE_LATEST.ver()),  default=[])

    civ_count: int                          = Retriever(int16,                                                      default=0)
    civ: Civ                                = Retriever(Civ, Version(Dat.AOE2_AOK_1999.ver()),
                                                        Version(Dat.AOE2_DE_LATEST.ver()),  default=Civ())

    #civs: list[Civ]                         = Retriever(Array32[Civ], Version(Dat.AOE2_AOK_1999.ver()),
    #                                                    Version(Dat.AOE2_DE_LATEST.ver()),  default=[])


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