from AOE1_1997_strings import terrain_AOE1_1997
from AOE1DE_strings import terrain_AOE1DE
from AOK_1999_strings import terrain_AOK_1999
from AOE2_CONQUERORS_10C import terrain_AOC_10C
from AOE2_HD_BASE_strings import terrain_HD_BASE
from AOE2_HD_DLC_strings import terrain_HD_DLC
from SWGB_strings import terrain_SWGB
from SWGB_EXPANSION_strings import terrain_SWGB_EXPANSION
from DE_START_strings import terrain_DE_START
from DE_LATEST_strings import terrains_DE_LATEST

import numpy as np

SWGB_EXP_DIFFERENCES = np.setdiff1d(terrain_SWGB_EXPANSION, terrain_SWGB)

AOK_excluded = terrain_AOC_10C + terrain_HD_BASE + terrain_HD_DLC
AOC_excluded = terrain_AOK_1999 + terrain_HD_BASE + terrain_HD_DLC
HD_BASE_excluded = terrain_AOK_1999 + terrain_AOC_10C + terrain_HD_DLC
HD_DLC_excluded = terrain_AOK_1999 + terrain_AOC_10C + terrain_HD_BASE

AOK_DIFFERENCES = np.setdiff1d(terrain_AOK_1999, AOK_excluded)
AOC_DIFFERENCES = np.setdiff1d(terrain_AOC_10C, AOC_excluded)
HD_BASE_DIFFERENCES = np.setdiff1d(terrain_HD_BASE, HD_BASE_excluded)
HD_DLC_DIFFERENCES = np.setdiff1d(terrain_HD_DLC, HD_DLC_excluded)
#print(AOK_DIFFERENCES) # roads not in other versions
#print(AOC_DIFFERENCES)
#print(HD_BASE_DIFFERENCES)
#print(HD_DLC_DIFFERENCES) # lots of extra terrains

print("the following strings are only in AOK, not AOC", np.setdiff1d(terrain_AOK_1999, terrain_AOC_10C))
print("the following strings are only in AOC, not HD_BASE", np.setdiff1d(terrain_AOC_10C, terrain_HD_BASE))
print("the following strings are only in HD_BASE, not AOC", np.setdiff1d(terrain_HD_BASE, terrain_AOC_10C))

#Map pointers are different between AOC and HD_BASE

print("the following strings are only in AOK, not HD_BASE", np.setdiff1d(terrain_AOK_1999, terrain_HD_BASE))
print("the following strings are only in HD_BASE, not AOK", np.setdiff1d(terrain_HD_BASE, terrain_AOK_1999))
#print(np.setdiff1d(terrain_HD_BASE, terrain_HD_DLC))
print("the following strings are only in HD_DLC, not HD_BASE",np.setdiff1d(terrain_HD_DLC, terrain_HD_BASE))

#    AOE2_AOK_1999               = ("sample_dats/empires2_aok_1999.dat",                                  5.7, (5, 7))     # VER 5.7
#    AOE2_CONQUERORS_2000        = ("sample_dats/empires2_x1_aoc_2000.dat",                               5.7, (5, 7))     # VER 5.7
#    AOE2_CONQUERORS_10C         = ("sample_dats/empires2_x1_p1_aoc10c.dat",                              5.7, (5, 7))     # VER 5.7
#    AOE2_HD_BASE                = ("sample_dats/empires2_x1_p1_hd_base.dat",                             5.7, (5, 7))     # VER 5.7
#    AOE2_HD_DLC                 = ("sample_dats/empires2_x2_p1_hd_withDLC.dat",                          5.7, (5, 7))     # VER 5.7

#First check for strings only present in DLC - if present, it's DLC
#Next check for strings only present in AOK - if present, it's AOK
#If neither of these were present, it is AOC or HD

HD_BASE_FINGERPRINT   = "00 00 00 00 67 5F 72 64 31 00 00 00 00 00 00 00 00 AA 3A 00 00 00 00 00 00 FF FF FF FF 78"
AOK_FINGERPRINT       = "00 00 00 00 67 5F 73 6E 31 AA 3A 00 00 00 00 00 00 FF FF FF FF 00 00 00 00 00 00 00 00 25"
DE_LATEST_FINGERPRINT = "60 0A 05 00 67 5F 72 64 31 AA 3A 00 00 00 00 00 00 FF FF FF FF 00 00 00 00 00 00 00 00 9E" # but different version in file header
HD_DLC_FINGERPRINT    = "00 00 00 00 67 5F 70 61 6C 31 00 00 00 00 00 00 00 FF FF FF FF 00 00 00 00 FE 00 00 00 4F"