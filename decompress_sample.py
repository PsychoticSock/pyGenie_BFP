import zlib

import local_paths
from dat_file_locations import Dat

def DecompressSample(datversion: Dat):
    with open(str(datversion.filepath()), 'rb') as f:
        content = f.read()
    decompressed_content = zlib.decompress(content, -zlib.MAX_WBITS)
        #print(decompressed_content[:100])
    oname = local_paths.decompressed_path + datversion.version_label
    with open(oname, 'wb') as r:
        r.write(decompressed_content)