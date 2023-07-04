from dat_file_locations import Dat
from dat_structure import DatStructure
from decompress_sample import DecompressSample

current_dat = Dat.AOE2_DE_LATEST

DecompressSample(current_dat)  # Make decompresed data available for hex editor

datfile = DatStructure.from_file(current_dat.decompressed_path(), strict=False)

print(datfile)