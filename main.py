import copy
import os
import zlib
import cProfile, pstats

from dat_file_locations import Dat
from dat_structure import DatStructure
from decompress_sample import DecompressSample
from sections.units import unit_data, type_10
from unitdatwrapper import DatUnitWrapper

current_dat = Dat.AOE2_AOK_1999
batch = False

def compress(bytes_: bytes) -> bytes:
    compressed = zlib.compress(bytes_, zlib.Z_DEFAULT_COMPRESSION, -zlib.MAX_WBITS)
    return compressed




if batch:
    for dat in Dat:
        print(dat.name)
        current_dat = dat
        DecompressSample(current_dat)  # Make decompresed data available for hex editor

        datfile = DatStructure.from_file(current_dat.decompressed_path(), strict=True)

        # try:
        #    print(datfile.tech_trees)
        # except:
        #    print("Item not found to print")

else:
    DecompressSample(current_dat)  # Make decompresed data available for hex editor

    record_performance = False
    if record_performance:
        profiler = cProfile.Profile()
        profiler.enable()

    make_dat = True
    if make_dat:
    #cProfile.run("datfile = DatStructure.from_file(current_dat.decompressed_path(), strict=False)")
        datfile = DatStructure.from_file(current_dat.decompressed_path(), strict=False)

        for civ in range(0,5):
            gaia_castle = DatUnitWrapper(datfile, civ, 81)
            print("hitpoints here:", gaia_castle.hit_points)

            #gaia_castle.change_hp(10000)
            gaia_castle.hit_points = 20000
            gaia_castle.standing_graphic_1_id = 666

            print("Class: ", gaia_castle.unit_class)
            gaia_castle.dead_unit_id = 123

            print("dat hitpoints", civ, datfile.civs[civ].unit_data[81].type_10.hit_points)

    #print(datfile.civs[0].unit_data[234].type_10.hit_points)
    #datfile.civs[0].unit_data[234].type_10.hit_points = 15000
    #print(datfile.civs[0].unit_data[234].type_10.hit_points )
    print("Dat File Read")



    if record_performance:
        profiler.disable()
        stats = pstats.Stats(profiler).sort_stats('time')

        stats.print_callees()

        print("name: ")
        print(stats.sort_stats('name'))
        print("all stats: ")
        stats.print_stats()
        print("cumulative (top 10): ")
        stats.sort_stats('cumulative').print_stats(10)
        print("time (top 10): ")
        stats.sort_stats('time').print_stats(10)

        stats.dump_stats("D:/AOE2Modding/pyGenieUtils.prof")

    if make_dat:
        datfile.to_file(f"D:/AOE2Modding/sample_dats/output/{current_dat.name}_2.dat")

write_test_dat = True
if write_test_dat == True:

    r = open(f"D:/AOE2Modding/sample_dats/output/{current_dat.name}_2.dat", 'rb')
    to_compress = r.read()
    compressed = compress(to_compress)


    f = open(f'D:/AOE2Modding/sample_dats/output/{current_dat.name}_output.dat', 'wb')
    f.write(compressed)
    f.close()



#try:
#    print(datfile.civs)
#except:
#    print("Item not found to print")
