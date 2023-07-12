from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version, RetrieverCombiner
from binary_file_parser.types import int8, uint16, int16, uint32, str16, int32, Array16, FixedLenStr, float32

from dat_file_locations import Dat

class Type10(BaseStruct):
    name_length_1: int           = Retriever(uint16, Version(Dat.AOE1_1997.ver()), Version(Dat.AOE1DE_ORIGINAL.ver()),      default=0)
    name_length_2: int           = Retriever(uint16, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.SWGB_EXPANSION.ver()),   default=0)

    name_length: int             = RetrieverCombiner([name_length_1, name_length_2])

    unit_id: int                 = Retriever(int16,                                                                         default=0)

    language_dll_name_1: int     = Retriever(uint32, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),   default=0)
    language_dll_creation_1: int = Retriever(uint32, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),   default=0)

    language_dll_name_2: int     = Retriever(uint16, Version(Dat.AOE1_1997.ver()),     Version(Dat.AOE1DE_ORIGINAL.ver()),  default=0)
    language_dll_creation_2: int = Retriever(uint16, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.SWGB_EXPANSION.ver()),   default=0)


    unit_class: int              = Retriever(int16,                                                                         default=0)
    idle_graphic_0: int          = Retriever(int16,                                                                         default=0)
    idle_graphic_1: int          = Retriever(int16,  Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),   default=0)

    dying_graphic: int           = Retriever(int16,         default=0)
    undead_graphic: int          = Retriever(int16,         default=0)
    death_mode: int              = Retriever(int8,          default=0)
    hit_points: int              = Retriever(int16,         default=0)
    line_of_sight: float32       = Retriever(float32,       default=0)
    garrison_capacity: int       = Retriever(int8,          default=0)
    radius_x: float32            = Retriever(float32,       default=0)
    radius_y: float32            = Retriever(float32,       default=0)
    radius_z: float32            = Retriever(float32,       default=0)
    train_sound_id: int          = Retriever(int16,         default=0)



    damage_sound_id_1: int       = Retriever(uint32, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),   default=0)
    damage_sound_id_2: int       = Retriever(uint16, Version(Dat.AOE1_1997.ver()),     Version(Dat.AOE1DE_ORIGINAL.ver()),  default=0)

    dead_unit_id: int            = Retriever(int16,                                                                         default=0)

    blood_unit_id_1: int         = Retriever(int16, Version(Dat.AOE1DE.ver()),      Version(Dat.AOE1DE.ver()),              default=0)
    blood_unit_id_2: int         = Retriever(int16, Version(Dat.AOE2_DE_START.ver()),   Version(Dat.AOE2_DE_LATEST.ver()),      default=0)

    placement_mode: int          = Retriever(int8,                                                                          default=0)
    can_be_built_on: int         = Retriever(int8,                                                                          default=0)
    icon_id: int                 = Retriever(int16,                                                                         default=0)
    hidden_in_editor: int        = Retriever(int8,                                                                          default=0)
    old_portrait_icon_id: int    = Retriever(int16,                                                                         default=0)
    enabled: int                 = Retriever(int8,                                                                          default=0)

    disabled_1: int              = Retriever(int8,  Version(Dat.AOE1DE.ver()),      Version(Dat.AOE1DE.ver()),              default=0)
    disabled_2: int              = Retriever(int8,  Version(Dat.AOE1DE.ver()),      Version(Dat.AOE1DE.ver()),              default=0)

    placement_side_terrain0: int16
    placement_side_terrain1: int16
    placement_terrain0: int16
    placement_terrain1: int16
    clearance_size_x: float
    "),
    clearance_size_y: float
    "),
    # determines the maxmimum elevation difference for terrain under the unit
    elevation_mode:
    raw_type = "int8_t",
               type_name = "elevation_modes",
                           lookup_dict = ELEVATION_MODES
    )),
    visible_in_fog:
    raw_type = "int8_t",
               type_name = "fog_visibility",
                           lookup_dict = FOG_VISIBILITY
    )),
    terrain_restriction:
    raw_type = "int16_t",  # determines on what type of ground the unit can be placed/walk
               type_name = "ground_type",  # is actually the id of the terrain_restriction entry!
                           lookup_dict = TERRAIN_RESTRICTIONS
    )),
    # determines whether the unit can fly
    fly_mode: int8
    resource_capacity: int16
    # when animals rot, their resources decay
    resource_decay: float
    "),
    blast_defense_level:
    # receive blast damage from units that have lower or same
    # blast_attack_level.
    raw_type = "int8_t",
               type_name = "blast_types",
                           lookup_dict = BLAST_DEFENSE_TYPES
    )),
    combat_level:
    raw_type = "int8_t",
               type_name = "combat_levels",
                           lookup_dict = COMBAT_LEVELS
    )),
    interaction_mode:
    # what can be done with this unit?
    raw_type = "int8_t",
               type_name = "interaction_modes",
                           lookup_dict = INTERACTION_MODES
    )),
    map_draw_level:
    # how does the unit show up on the minimap?
    raw_type = "int8_t",
               type_name = "minimap_modes",
                           lookup_dict = MINIMAP_MODES
    )),
    unit_level:
    # selects the available ui command buttons for the unit
    raw_type = "int8_t",
               type_name = "command_attributes",
                           lookup_dict = UNIT_LEVELS
    )),
    attack_reaction: float
    "),
    # palette color id for the minimap
    minimap_color: int8
    # help text for this unit, stored in the translation dll.
    language_dll_help: int32
    language_dll_hotkey_text: int32
    # language dll dependent (kezb lazouts!)
    hot_keys: int32
    recyclable: int8
    enable_auto_gather: int8
    doppelgaenger_on_death: int8
    resource_gather_drop: int8
    ])

    if game_version.edition.game_id not in ("ROR", "AOE1DE"):
    # bit 0 == 1 && val != 7: mask shown behind buildings,
    # bit 0 == 0 && val != {6, 10}: no mask displayed,
    # val == {-1, 7}: in open area mask is partially displayed
    # val == {6, 10}: building, causes mask to appear on units behind it
        data_format.extend([
            occlusion_mode: uint8
    obstruction_type:
    raw_type = "int8_t",
               type_name = "obstruction_types",
                           lookup_dict = OBSTRUCTION_TYPES
    )),
    obstruction_class: int8

    # bitfield of unit attributes:
    # bit 0: allow garrison,
    # bit 1: don't join formation,
    # bit 2: stealth unit,
    # bit 3: detector unit,
    # bit 4: mechanical unit,
    # bit 5: biological unit,
    # bit 6: self-shielding unit,
    # bit 7: invisible unit
    trait: uint8
    civilization_id: int8
    # leftover from trait+civ variable
    attribute_piece: int16
    ])
    elif game_version.edition.game_id == "AOE1DE":
    data_format.extend([
        obstruction_type:
    raw_type = "int8_t",
               type_name = "obstruction_types",
                           lookup_dict = OBSTRUCTION_TYPES
    )),
    obstruction_class: int8
    ])

    data_format.extend([
        selection_effect:
    # things that happen when the unit was selected
    raw_type = "int8_t",
               type_name = "selection_effects",
                           lookup_dict = SELECTION_EFFECTS
    )),
    # 0: default, -16: fish trap, farm, 52: deadfarm, OLD-*, 116: flare,
    # whale, dolphin -123: fish
    (READ, "editor_selection_color", StorageType.ID_MEMBER, "uint8
     selection_shape_x:                  float"),
     selection_shape_y:                  float"),
     selection_shape_z:                  float"),
     ])

    if game_version.edition.game_id == "AOE2DE":
        data_format.extend([
            (READ, "scenario_trigger_data0", StorageType.ID_MEMBER, "uint32
            (READ, "scenario_trigger_data1", StorageType.ID_MEMBER, "uint32
             ])

            data_format.extend([
                resource_storage:
        ref_type = ResourceStorage,
                   length = 3,
    )),
    (READ, "damage_graphic_count", StorageType.INT_MEMBER, "int8
     damage_graphics:
     ref_type=DamageGraphic,
     length="damage_graphic_count",
     )),
    selection_sound_id: int16
    dying_sound_id: int16
    ])

    if game_version.edition.game_id == "AOE2DE":
        data_format.extend([
            wwise_creation_sound_id: uint32
    wwise_damage_sound_id: uint32
    wwise_selection_sound_id: uint32
    wwise_dying_sound_id: uint32
    ])

    data_format.extend([
        old_attack_mode: (  # obsolete, as it's copied when converting the unit
        raw_type="int8_t",  # things that happen when the unit was selected
    type_name="attack_modes",
    lookup_dict=ATTACK_MODES
    )),
    # leftover from alpha. would et units change terrain under them
    convert_terrain: int8
    ])

    if game_version.edition.game_id in ("AOE1DE", "AOE2DE"):
        data_format.extend([
            name_len_debug: uint16
        (READ, "name_len", StorageType.INT_MEMBER, "uint16
    name: char[name_len]
    "),
    ])

    else:
    data_format.extend([
        name: char[name_length]
    "),
    ])

    if game_version.edition.game_id == "SWGB":
        data_format.extend([
            (READ, "name2_length", StorageType.INT_MEMBER, "uint16
             name2:                  char[name2_length]"),
             unit_line_id:               int16
             min_tech_level:                 int8

             data_format.append  id1:        int16_t"))

             if game_version.edition.game_id not in ("ROR", "AOE1DE"):
        data_format.append
    id2: int16_t
    "))
    elif game_version.edition.game_id == "AOE1DE":
    data_format.telemetry_id:               int16_t
    "))


return data_format


def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)
