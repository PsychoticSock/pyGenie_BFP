from dat_file_locations import Dat
from dat_structure import DatStructure
from decompress_sample import DecompressSample


current_dat = Dat.AOE2_DE_LATEST
batch = False

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

    datfile = DatStructure.from_file(current_dat.decompressed_path(), strict=False)


datfile.to_file(f"D:/AOE2Modding/sample_dats/output/{current_dat.name}_2.dat")

try:
    print("Done")
    print("Version=", datfile.struct_ver)
    print(datfile.civs)
except:
    print("Item not found to print")
