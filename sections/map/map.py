from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import int32, uint32

from sections.map.map_elevation import MapElevation
from sections.map.map_land import MapLand
from sections.map.map_terrain import MapTerrain
from sections.map.map_unit import MapUnit


class MapDetails(BaseStruct):
    @staticmethod
    def set_MapLand_count(_, instance: MapDetails):
        Retriever.set_repeat(MapDetails.base_zones, instance, instance.base_zone_count)
    def set_MapTerrain_count(_, instance: MapDetails):
        Retriever.set_repeat(MapDetails.map_terrains, instance, instance.map_terrain_count)
    def set_MapUnit_count(_, instance: MapDetails):
        Retriever.set_repeat(MapDetails.map_units, instance, instance.map_unit_count)
    def set_MapElevation_Count(_, instance: MapDetails):
        Retriever.set_repeat(MapDetails.map_elevations, instance, instance.map_elevation_count)

    border_south_west: int          = Retriever(int32,          default=0)
    border_north_west: int          = Retriever(int32,          default=0)
    border_north_east: int          = Retriever(int32,          default=0)
    border_south_east: int          = Retriever(int32,          default=0)
    border_usage: int               = Retriever(int32,          default=0)
    water_shape: int                = Retriever(int32,          default=0)
    base_terrain: int               = Retriever(int32,          default=0)
    land_coverage: int              = Retriever(int32,          default=0)
    unused_id: int                  = Retriever(int32,          default=0)

    base_zone_count: int            = Retriever(uint32,         default=0, on_set=[set_MapLand_count])
    base_zone_ptr: int              = Retriever(int32,          default=0)

    base_zones: MapLand             = Retriever(MapLand,        default=MapLand(), repeat=0)

    map_terrain_count: int          = Retriever(uint32,         default=0, on_set=[set_MapTerrain_count])
    map_terrain_ptr: int            = Retriever(int32,          default=0)
    map_terrains: MapTerrain        = Retriever(MapTerrain,     default=MapTerrain(), repeat=0)

    map_unit_count: int             = Retriever(uint32,         default=0, on_set=[set_MapUnit_count])
    map_unit_ptr: int               = Retriever(int32,          default=0)
    map_units: MapUnit              = Retriever(MapUnit,        default=MapUnit(), repeat=0)

    map_elevation_count: int        = Retriever(uint32,         default=0, on_set=[set_MapElevation_Count])
    map_elevation_ptr: int          = Retriever(int32,          default=0)
    map_elevations: MapElevation    = Retriever(MapElevation,   default=MapElevation(), repeat=0)