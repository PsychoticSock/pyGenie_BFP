from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version

from terrain_pass_graphics import TerrainPassGraphics
from terrain_restrictions import TerrainRestrictions


class TerrainTables(BaseStruct):

    terrain_restrictions: int = Retriever(TerrainRestrictions, default=TerrainRestrictions())
    terrain_pass_graphics: list[TerrainPassGraphics] = Retriever(TerrainPassGraphics, default=TerrainPassGraphics())

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        if parent is not None:
            Retriever.set_repeat(TerrainTables.terrain_restrictions, self, parent.terrain_count)
            Retriever.set_repeat(TerrainTables.terrain_pass_graphics, self, parent.terrain_count)
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)


