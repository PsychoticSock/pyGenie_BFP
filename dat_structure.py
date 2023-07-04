from __future__ import annotations

from dat_file_locations import Dat

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import ByteStream, uint16, uint32

from file_header import FileHeader
from graphics import Graphics
from player_colour import PlayerColour
from sounds import Sounds
from terrain_tables import TerrainTables


class DatStructure(BaseStruct):
    @staticmethod
    def set_terrain_restriction_count(_, instance: DatStructure):
        Retriever.set_repeat(DatStructure.float_ptr_terrain_tables, instance, instance.terrain_restriction_count)
        Retriever.set_repeat(DatStructure.terrain_pass_graphics_ptrs, instance, instance.terrain_restriction_count)
        Retriever.set_repeat(DatStructure.terrain_tables, instance, instance.terrain_restriction_count)

    @staticmethod
    def set_terrain_count(_, instance: DatStructure):
        pass

    # @formatter:off
    file_header: FileHeader                 = Retriever(FileHeader,                                                 default=FileHeader()) #, remaining_compressed=True)  # Need to remove this is BFP supports compression
    civ_count_swgb:                   int   = Retriever(uint16, Version(Dat.SWGB.ver()), Version(Dat.SWGB.ver()),   default=0)
    unknown_swgb_01:                  int   = Retriever(uint32, Version(Dat.SWGB.ver()), Version(Dat.SWGB.ver()),   default=0)
    unknown_swgb_02:                  int   = Retriever(uint32, Version(Dat.SWGB.ver()), Version(Dat.SWGB.ver()),   default=0)
    blend_mode_count_swgb:            int   = Retriever(uint32, Version(Dat.SWGB.ver()), Version(Dat.SWGB.ver()),   default=0)
    blend_mode_count_max_swgb:        int   = Retriever(uint32, Version(Dat.SWGB.ver()), Version(Dat.SWGB.ver()),   default=0)
    terrain_restriction_count:        int   = Retriever(uint16,                                                     default=0, on_set=[set_terrain_restriction_count])
    terrain_count:                    int   = Retriever(uint16,                                                     default=0)
    float_ptr_terrain_tables:   list[int]   = Retriever(uint32,                                                     default=0)
    terrain_pass_graphics_ptrs: list[int]   = Retriever(uint32, min_ver=Version(Dat.AOE2_AOK_1999.ver()),
                                                                        max_ver=Version(Dat.AOE2_DE_LATEST.ver()),  default=0)  # This version information might be wrong but just a placeholder for now
    terrain_tables:   list[TerrainTables]   = Retriever(TerrainTables,                                              default=TerrainTables(), repeat=0)
    player_colour:           PlayerColour   = Retriever(PlayerColour,                                               default=PlayerColour())
    sounds:                        Sounds   = Retriever(Sounds,                                                     default=Sounds())
    graphics:                    Graphics   = Retriever(Graphics,                                                     default=Graphics())




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
        return Version(tuple(map(int, ver_str.split("."))))

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, initialise_defaults=True, **retriever_inits):
        super().__init__(struct_ver, parent, initialise_defaults=initialise_defaults, **retriever_inits)