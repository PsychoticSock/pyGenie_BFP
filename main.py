import copy

from datetime import datetime

import zlib
import cProfile, pstats

from binary_file_parser.retrievers import Retriever

from class_for_copying import DatFileObject
from dat_file_locations import Dat
from dat_structure import DatStructure
from decompress_sample import DecompressSample
from sections.units import unit_data, type_10
from sections.units.unit_data import UnitData
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

        #print("unit_headers_count:", len(datfile.unit_headers))
        #print("Unit_Lines", datfile.unit_lines)
        #print("unit_headers:", datfile.unit_headers)

        for civ, data in enumerate(datfile.civs):
            test = copy.deepcopy(datfile.civs[civ].unit_data[82])
            datfile.civs[civ].unit_data.insert(86, test)
            test2 = copy.deepcopy(datfile.unit_headers[82])
            datfile.unit_headers.insert(86, test2)
        datfile.unit_headers_count = len(datfile.unit_headers)

    #    castle = DatUnitWrapper(datfile, civ, 82)
            #castle.hit_points = 20000
            #castle.standing_graphic_1_id = 666
            #castle.dead_unit_id = 123

        #    print(f"castle2 copy start for civ {civ}")
            #print(datetime.now().strftime("%H:%M:%S"))
            #castle2 = copy.deepcopy(castle)
            #print(f"castle2 copied for civ {civ}")
            #print(datetime.now().strftime("%H:%M:%S"))
            #datfile.civs[civ].unit_data.append(castle2)
            #print(f"castle2 appended for civ {civ}")
            #print(datetime.now().strftime("%H:%M:%S"))


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
