from binary_file_parser import Version

from dat_file_locations import Dat
from dat_fingerprints import HD_BASE_TERRAIN_FINGERPRINT, AOK_TERRAIN_FINGERPRINT, DE_LATEST_TERRAIN_FINGERPRINT, HD_DLC_TERRAIN_FINGERPRINT
from dat_structure import DatStructure
from decompress_sample import DecompressSample


current_dat = Dat.AOE2_CONQUERORS_2000

DecompressSample(current_dat)  # Make decompresed data available for hex editor


datfile = DatStructure.from_file(current_dat.decompressed_path(), strict=False)

print(datfile.terrains)