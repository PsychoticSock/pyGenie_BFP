from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import uint32, int8, uint8, int16, uint16, float32

from dat_file_locations import Dat
from sections.graphics.graphic_attack_sounds import GraphicAttackSounds
from sections.graphics.graphic_deltas import GraphicDeltas

from class_for_copying import DatFileObject

class GraphicDataCommon(BaseStruct, DatFileObject):
    @staticmethod
    def set_delta_count(_, instance: GraphicDataCommon):
        Retriever.set_repeat(GraphicDataCommon.deltas, instance, instance.delta_count)

    def set_attack_sound_count(_, instance: GraphicDataCommon):
        if instance.attack_sound_used:
            Retriever.set_repeat(GraphicDataCommon.attack_sounds, instance, instance.angle_count)

    slp_id: int                              = Retriever(uint32,                                  default=0)
    is_loaded: int                           = Retriever(int8,                                    default=0)
    old_color_flag: int                      = Retriever(int8,                                    default=0)
    layer: int                               = Retriever(int8,                                    default=0)
    player_color_force_id: int               = Retriever(int8,                                    default=0)
    adapt_color: int                         = Retriever(int8,                                    default=0)
    transparent_selection: int               = Retriever(uint8,                                   default=0)
    coordinates: list[int]                   = Retriever(uint16,                                  default=[0,0,0,0], repeat=4)
    delta_count: int                         = Retriever(uint16,                                  default=0,                     on_set=[set_delta_count])
    sound_id: int                            = Retriever(int16,                                   default=-1)
    wwise_sound_id: int                      = Retriever(uint32, min_ver=Dat.AOE2_DE_START.ver(), default=0)

    attack_sound_used: bool                  = Retriever(uint8,                                   default=0)
    frame_count: int                         = Retriever(uint16,                                  default=0)
    angle_count: int                         = Retriever(uint16,                                  default=0, on_set=[set_attack_sound_count])

    speed_adjust: float                      = Retriever(float32,                                 default=0)
    frame_rate: float                        = Retriever(float32,                                 default=0)
    replay_delay: float                      = Retriever(float32,                                 default=0)
    sequence_type: int                       = Retriever(uint8,                                   default=0)
    graphic_id: int                          = Retriever(int16,                                   default=0)
    mirroring_mode: int                      = Retriever(uint8,                                   default=0)

    editor_flag: int                         = Retriever(int8,   min_ver=Dat.AOE2_AOK_1999.ver(), default=0)

    deltas: list[GraphicDeltas]              = Retriever(GraphicDeltas,                           default=GraphicDeltas())

    attack_sounds: list[GraphicAttackSounds] = Retriever(GraphicAttackSounds,                     default=GraphicAttackSounds(), repeat=0)

    def __init__(self, struct_ver: Version = Version((0,)), parent: BaseStruct = None, idx: int = -1,
                 initialise_defaults: bool = True, **retriever_inits):
        super().__init__(struct_ver, parent, idx, initialise_defaults, **retriever_inits)
