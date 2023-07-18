from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version, RetrieverCombiner
from binary_file_parser.types import int8, uint8, int16, float32, int32, uint32, Array16

from dat_file_locations import Dat
from sections.units.unit_command import UnitCommand


class Type80(BaseStruct):
    (READ_GEN, None, None, IncludeMembers(cls=LivingUnit)),
            (READ_GEN, "construction_graphic_id", StorageType.ID_MEMBER, "int16_t"),
        ]

        if game_version.edition.game_id not in ("ROR", "AOE1DE"):
            data_format.append((SKIP, "snow_graphic_id", StorageType.ID_MEMBER, "int16_t"))

            if game_version.edition.game_id == "AOE2DE":
                data_format.extend([
                    (READ_GEN, "destruction_graphic_id", StorageType.ID_MEMBER, "int16_t"),
                    (READ_GEN, "destruction_rubble_graphic_id", StorageType.ID_MEMBER, "int16_t"),
                    (READ_GEN, "research_graphic_id", StorageType.ID_MEMBER, "int16_t"),
                    (READ_GEN, "research_complete_graphic_id", StorageType.ID_MEMBER, "int16_t"),
                ])

        data_format.extend([
            # 1=adjacent units may change the graphics
            (SKIP, "adjacent_mode", StorageType.BOOLEAN_MEMBER, "int8_t"),
            (SKIP, "graphics_angle", StorageType.INT_MEMBER, "int16_t"),
            (SKIP, "disappears_when_built", StorageType.BOOLEAN_MEMBER, "int8_t"),
            # second building to place directly on top
            (READ_GEN, "stack_unit_id", StorageType.ID_MEMBER, "int16_t"),
            # change underlying terrain to this id when building completed
            (READ_GEN, "foundation_terrain_id", StorageType.ID_MEMBER, "int16_t"),
            # deprecated terrain-like structures knowns as "Overlays" from alpha
            # AOE used for roads
            (SKIP, "old_overlay_id", StorageType.ID_MEMBER, "int16_t"),
            # research_id to be enabled when building creation
            (READ_GEN, "research_id", StorageType.ID_MEMBER, "int16_t"),
        ])

        if game_version.edition.game_id not in ("ROR", "AOE1DE"):
            data_format.extend([
                (SKIP, "can_burn", StorageType.BOOLEAN_MEMBER, "int8_t"),
                (SKIP, "building_annex", StorageType.ARRAY_CONTAINER, SubdataMember(
                    ref_type=BuildingAnnex,
                    length=4
                )),
                # building at which an annex building is attached to
                (READ_GEN, "head_unit_id", StorageType.ID_MEMBER, "int16_t"),
                # destination unit id when unit shall transform (e.g. unpack)
                (READ_GEN, "transform_unit_id", StorageType.ID_MEMBER, "int16_t"),
                (READ_GEN, "transform_sound_id", StorageType.ID_MEMBER, "int16_t"),
            ])

        data_format.append((READ_GEN, "construction_sound_id", StorageType.ID_MEMBER, "int16_t"))

        if game_version.edition.game_id not in ("ROR", "AOE1DE"):
            if game_version.edition.game_id == "AOE2DE":
                data_format.extend([
                    (READ_GEN, "wwise_construction_sound_id", StorageType.ID_MEMBER, "uint32_t"),
                    (READ_GEN, "wwise_transform_sound_id", StorageType.ID_MEMBER, "uint32_t"),
                ])

            data_format.extend([
                (READ_GEN, "garrison_type", StorageType.BITFIELD_MEMBER, EnumLookupMember(
                    raw_type="int8_t",
                    type_name="garrison_types",
                    lookup_dict=GARRISON_TYPES
                )),
                (READ_GEN, "garrison_heal_rate", StorageType.FLOAT_MEMBER, "float"),
                (SKIP, "garrison_repair_rate", StorageType.FLOAT_MEMBER, "float"),
                # id of the unit used for salvages
                (SKIP, "salvage_unit_id", StorageType.ID_MEMBER, "int16_t"),
                # list of attributes for salvages (looting table)
                (SKIP, "salvage_attributes", StorageType.ARRAY_INT, "int8_t[6]"),
            ])


    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)

