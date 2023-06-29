from enum import Enum

import local_paths


class DatVersion(Enum):
    @property
    def version_label(self):
        return self.name
    def filepath(self) -> str:
        return self.value[0]
    def version_number(self) -> str:
        return self.value[1]
    def version_tuple(self) -> tuple:
        return self.value[2]
    def decompressed_path(self) -> str:
        return local_paths.decompressed_path + self.name
    AOE1_1997                   = ("D:/AOE2Modding/sample_dats/empires_aoe1_1997.dat",                                  3.7, (3, 7))     # VER 3.7
    AOE1DE                      = ("D:/AOE2Modding/sample_dats/empires_aoe1de_msstore.dat",                             4.5, (4, 5))     # VER 4.5
    AOE1DE_CLASSIC              = ("D:/AOE2Modding/sample_dats/empires_classic_aoe1de_msstore.dat",                     3.7, (3, 7))     # VER 3.7
    AOE1_RoR_1998               = ("D:/AOE2Modding/sample_dats/empires_ror_1998.dat",                                   3.7, (3, 7))     # VER 3.7
    AOE2_AOK_1999               = ("D:/AOE2Modding/sample_dats/empires2_aok_1999.dat",                                  5.7, (5, 7))     # VER 5.7
    AOE2_CONQUERORS_2000        = ("D:/AOE2Modding/sample_dats/empires2_x1_aoc_2000.dat",                               5.7, (5, 7))     # VER 5.7
    AOE2_CONQUERORS_10C         = ("D:/AOE2Modding/sample_dats/empires2_x1_p1_aoc10c.dat",                              5.7, (5, 7))     # VER 5.7
    AOE2_HD_BASE                = ("D:/AOE2Modding/sample_dats/empires2_x1_p1_hd_base.dat",                             5.7, (5, 7))     # VER 5.7
    AOE2_HD_DLC                 = ("D:/AOE2Modding/sample_dats/empires2_x2_p1_hd_withDLC.dat",                          5.7, (5, 7))     # VER 5.7
    AOE1DE_ORIGINAL             = ("D:/AOE2Modding/sample_dats/empires-orig_aoe1de_msstore.dat",                        3.7, (3, 7))     # VER 3.7
    SWGB                        = ("D:/AOE2Modding/sample_dats/GENIE_swgb_gog.dat",                                     5.9, (5, 9))     # VER 5.9
    SWGB_EXPANSION              = ("D:/AOE2Modding/sample_dats/genie_x1_swgbcc_gog.dat",                                5.9, (5, 9))     # VER 5.9
    AOE2DE_ROR                  = ("D:/AOE2Modding/sample_dats/AOE2DE Return Of Rome.dat",                              7.7, (7, 7))     # VER 7.7
    AOE2_DE_START              = ("D:/Games/Steam/steamapps/common/AoE2DE/resources/_common/dat/empires2_x2_p1.dat",   7.1, (7, 1))     # VER 7.1  (I have guessed this for now)
    AOE2_DE_LATEST              = ("D:/Games/Steam/steamapps/common/AoE2DE/resources/_common/dat/empires2_x2_p1.dat",   7.7, (7, 7))     # VER 7.7  (Or latest)
