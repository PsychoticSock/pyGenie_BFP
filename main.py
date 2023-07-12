from dat_file_locations import Dat
from dat_structure import DatStructure
from decompress_sample import DecompressSample


current_dat = Dat.SWGB
batch = False

if batch:
    for dat in Dat:
        print(dat.name)
        current_dat = dat
        DecompressSample(current_dat)  # Make decompresed data available for hex editor


        datfile = DatStructure.from_file(current_dat.decompressed_path(), strict=False)

else:
    DecompressSample(current_dat)  # Make decompresed data available for hex editor

    datfile = DatStructure.from_file(current_dat.decompressed_path(), strict=False)

print(datfile.civ_count)
print(datfile.civ)
print(datfile.unit_headers)