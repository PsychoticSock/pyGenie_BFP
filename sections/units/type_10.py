from __future__ import annotations


from class_for_copying import DatFileObject
from binary_file_parser import Retriever, BaseStruct, Version, RetrieverCombiner
from binary_file_parser.types import uint8, int8, uint16, int16, uint32, int32, float32, Bytes, Array8, str16

from dat_file_locations import Dat
from sections.units.damage_graphic import DamageGraphic
from sections.units.resource_storage import ResourceStorage


class Type10(BaseStruct, DatFileObject):
    @staticmethod
    def set_name_length_1(_, instance: Type10):
        Retriever.set_repeat(Type10.name_3, instance, instance.name_length_1)
    @staticmethod
    def set_name_length_2(_, instance: Type10):
        Retriever.set_repeat(Type10.name_4, instance, instance.name_length_2)

    name_length_1: int                      = Retriever(uint16, Version(Dat.AOE1_1997.ver()), Version(Dat.AOE1DE_ORIGINAL.ver()),                 default=0, on_set=[set_name_length_1])
    name_length_2: int                      = Retriever(uint16, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.SWGB_EXPANSION.ver()),              default=0, on_set=[set_name_length_2])

    name_length: int                        = RetrieverCombiner([name_length_1, name_length_2])

    unit_id: int                            = Retriever(int16,                                                                                    default=0)

    language_dll_name_1: int                = Retriever(uint32, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),              default=0)
    language_dll_creation_1: int            = Retriever(uint32, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()),              default=0)

    language_dll_name_2: int                = Retriever(uint16, Version(Dat.AOE1_1997.ver()),     Version(Dat.SWGB_EXPANSION.ver()),              default=0)
    language_dll_creation_2: int            = Retriever(uint16, Version(Dat.AOE1_1997.ver()), Version(Dat.SWGB_EXPANSION.ver()),                  default=0)



    unit_class: int                         = Retriever(int16,                                                                                    default=0)
    idle_graphic_0: int                     = Retriever(int16,                                                                                    default=0)
    idle_graphic_1: int                     = Retriever(int16,  Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),              default=0)

    dying_graphic: int                      = Retriever(int16,                                                                                    default=0)
    undead_graphic: int                     = Retriever(int16,                                                                                    default=0)
    death_mode: int                         = Retriever(int8,                                                                                     default=0)
    hit_points: int                         = Retriever(int16,                                                                                    default=0)
    line_of_sight: float                    = Retriever(float32,                                                                                  default=0)
    garrison_capacity: int                  = Retriever(int8,                                                                                     default=0)
    radius_x: float                         = Retriever(float32,                                                                                  default=0)
    radius_y: float                         = Retriever(float32,                                                                                  default=0)
    radius_z: float                         = Retriever(float32,                                                                                  default=0)
    train_sound_id: int                     = Retriever(int16,                                                                                    default=0)



    damage_sound_id_1: int                  = Retriever(int16, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),               default=0)

    dead_unit_id: int                       = Retriever(int16,                                                                                    default=0)

    blood_unit_id_1: int                    = Retriever(int16, Version(Dat.AOE1DE.ver()),      Version(Dat.AOE1DE.ver()),                         default=0)
    blood_unit_id_2: int                    = Retriever(int16, Version(Dat.AOE2_DE_START.ver()),   Version(Dat.AOE2_DE_LATEST.ver()),             default=0)

    placement_mode: int                     = Retriever(int8,                                                                                     default=0)
    can_be_built_on: int                    = Retriever(int8,                                                                                     default=0)
    icon_id: int                            = Retriever(int16,                                                                                    default=0)
    hidden_in_editor: int                   = Retriever(int8,                                                                                     default=0)
    old_portrait_icon_id: int               = Retriever(int16,                                                                                    default=0)
    enabled: int                            = Retriever(int8,                                                                                     default=0)

    disabled: int                           = Retriever(int8,  Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()),               default=0)

    placement_side_terrain0: int            = Retriever(int16,                                                                                    default=0)
    placement_side_terrain1: int            = Retriever(int16,                                                                                    default=0)
    placement_terrain0: int                 = Retriever(int16,                                                                                    default=0)
    placement_terrain1: int                 = Retriever(int16,                                                                                    default=0)
    clearance_size_x: float                 = Retriever(float32,                                                                                  default=0)
    clearance_size_y: float                 = Retriever(float32,                                                                                  default=0)

    elevation_mode: int                     = Retriever(int8,                                                                                     default=0)
    visible_in_fog: int                     = Retriever(int8,                                                                                     default=0)


    terrain_restriction: int                = Retriever(int16,                                                                                    default=0)

    fly_mode: int                           = Retriever(int8,                                                                                     default=0)
    resource_capacity: int                  = Retriever(int16,                                                                                    default=0)
    resource_decay: float                   = Retriever(float32,                                                                                  default=0)

    blast_defense_level: int                = Retriever(int8,                                                                                     default=0)
    combat_level: int                       = Retriever(int8,                                                                                     default=0)

    interaction_mode: int                   = Retriever(int8,                                                                                     default=0)

    map_draw_level: int                     = Retriever(int8,                                                                                     default=0)

    unit_level: int                         = Retriever(int8,                                                                                     default=0)

    attack_reaction: float                  = Retriever(float32,                                                                                  default=0)

    minimap_color: int                      = Retriever(int8,                                                                                     default=0)

    language_dll_help: int                  = Retriever(int32,                                                                                    default=0)
    language_dll_hotkey_text: int           = Retriever(int32,                                                                                    default=0)

    hot_keys:   int                         = Retriever(int32,                                                                                    default=0)
    recyclable: int                         = Retriever(int8,                                                                                     default=0)
    enable_auto_gather: int                 = Retriever(int8,                                                                                     default=0)
    doppelgaenger_on_death: int             = Retriever(int8,                                                                                     default=0)
    resource_gather_drop: int               = Retriever(int8,                                                                                     default=0)

    occlusion_mode: int                     = Retriever(uint8,    Version(Dat.AOE2_AOK_1999.ver()),           Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    obstruction_type_1: int                 = Retriever(int8,   Version(Dat.AOE2_AOK_1999.ver()),           Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    obstruction_class_1: int                = Retriever(int8,   Version(Dat.AOE2_AOK_1999.ver()),           Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    trait: int                              = Retriever(uint8,    Version(Dat.AOE2_CONQUERORS_2000.ver()),    Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    civilization_id: int                    = Retriever(int8,     Version(Dat.AOE2_CONQUERORS_2000.ver()),    Version(Dat.AOE2_DE_LATEST.ver()),  default=0)
    attribute_piece: int                    = Retriever(int16,    Version(Dat.AOE2_CONQUERORS_2000.ver()),    Version(Dat.AOE2_DE_LATEST.ver()),  default=0)


    obstruction_type_2: int                 = Retriever(int8,     Version(Dat.AOE1DE.ver()),         Version(Dat.AOE1DE.ver()),                 default=0)
    obstruction_class_2: int                = Retriever(int8,     Version(Dat.AOE1DE.ver()),         Version(Dat.AOE1DE.ver()),                 default=0)

    selection_effect: int                   = Retriever(int8,                                                                                     default=0)
    editor_selection_color: int             = Retriever(uint8,                                                                                    default=0)
    selection_shape_x: float                = Retriever(float32,                                                                                  default=0)
    selection_shape_y: float                = Retriever(float32,                                                                                  default=0)
    selection_shape_z: float                = Retriever(float32,                                                                                  default=0)


    scenario_trigger_data0: int             = Retriever(uint32,   Version(Dat.AOE2_DE_START.ver()),  Version(Dat.AOE2_DE_LATEST.ver()),           default=0)
    scenario_trigger_data1: int             = Retriever(uint32,   Version(Dat.AOE2_DE_START.ver()),  Version(Dat.AOE2_DE_LATEST.ver()),           default=0)

    resource_storage: list[ResourceStorage] = Retriever(ResourceStorage,                                                                default=ResourceStorage(), repeat=3)
    damage_graphics: list[DamageGraphic]    = Retriever(Array8[DamageGraphic],                                                             default=[])


    selection_sound_id:  int                = Retriever(int16,                                                                                   default=0)
    dying_sound_id: int                     = Retriever(int16,                                                                                   default=0)

    wwise_train_sound_id: int               = Retriever(uint32,  Version(Dat.AOE2_DE_START.ver()),  Version(Dat.AOE2_DE_LATEST.ver()),           default=0) #wwise_creation_sound_id
    wwise_damage_sound_id: int              = Retriever(uint32,  Version(Dat.AOE2_DE_START.ver()),  Version(Dat.AOE2_DE_LATEST.ver()),           default=0)
    wwise_selection_sound_id: int           = Retriever(uint32,  Version(Dat.AOE2_DE_START.ver()),  Version(Dat.AOE2_DE_LATEST.ver()),           default=0)
    wwise_dying_sound_id: int               = Retriever(uint32,  Version(Dat.AOE2_DE_START.ver()),  Version(Dat.AOE2_DE_LATEST.ver()),           default=0)


    old_attack_mode: int                    = Retriever(int8,                                                                                    default=0)
    convert_terrain: int                    = Retriever(int8,                                                                                    default=0)

    name_len_debug_1: int                   = Retriever(uint16, Version(Dat.AOE1DE.ver()), Version(Dat.AOE1DE.ver()), default=0)
    name_len_debug_2: int                   = Retriever(uint16, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()), default=0)
    name_1: str                             = Retriever(str16, Version(Dat.AOE1DE.ver()), Version(Dat.AOE1DE.ver()), default=0)
    name_2: str                             = Retriever(str16, Version(Dat.AOE2_DE_START.ver()), Version(Dat.AOE2_DE_LATEST.ver()), default=0)


    name_3: str                             = Retriever(Bytes[1], Version(Dat.AOE1_1997.ver()), Version(Dat.AOE1DE_ORIGINAL.ver()), default=0)   # Definitely wrong type here
    name_4: str                             = Retriever(Bytes[1], Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.SWGB_EXPANSION.ver()), default=0)  # Definitely wrong type here


    name_5: str                              = Retriever(str16, Version(Dat.SWGB.ver()), Version(Dat.SWGB_EXPANSION.ver()),     default=0)
    unit_line_id: int                       = Retriever(int16, Version(Dat.SWGB.ver()), Version(Dat.SWGB_EXPANSION.ver()),     default=0)
    min_tech_level: int                     = Retriever(int8,  Version(Dat.SWGB.ver()), Version(Dat.SWGB_EXPANSION.ver()),      default=0)
    id1: int                                = Retriever(int16,  default=0)

    id2: int                                = Retriever(int16, Version(Dat.AOE2_AOK_1999.ver()), Version(Dat.AOE2_DE_LATEST.ver()), default=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                     initialise_defaults: bool = True, **retriever_inits):
            super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)
