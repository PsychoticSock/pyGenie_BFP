from typing import Any

from binary_file_parser import Version

from dat_file_locations import Dat
from dat_structure import DatStructure
from sections.units.resource_storage import ResourceStorage
from sections.units.damage_graphic import DamageGraphic


class graphics_attributes:

    def __init__(self) -> None:
        super().__init__()

    def __setattr__(self, key, value):
        super(graphics_attributes, self).__setattr__(key, value)

    def __repr__(self):
        return "{attrs}".format(
            attrs=" ".join("\t{}:\t\t{!r}\n".format(k, v) for k, v in self.__dict__.items()),
        )



class DatUnitWrapper:
    def __init__(
            self,
            dat: DatStructure,
            civ_id,
            unit_id
    ):

        self._civ_id = civ_id
        self._unit_id = unit_id
        self._dat = dat
        #self.graphics = graphics_attributes()
        #self.unit_type                                              = dat.civs[civ_id].unit_data[unit_id].unit_type
        #self.unit_class                                             = dat.civs[civ_id].unit_data[unit_id].type_10.unit_class


    @property
    def name_length_1(self) -> int:
        """"""
        if Version(Dat.AOE1_1997.ver()) >= self._dat.struct_ver >= Version(Dat.AOE1DE_ORIGINAL.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_length_1

    @name_length_1.setter
    def name_length_1(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_length_1 = value

    @property
    def name_length_2(self) -> int:
        """"""
        if Version(Dat.AOE2_AOK_1999.ver()) >= self._dat.struct_ver >= Version(Dat.SWGB_EXPANSION.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_length_2

    @name_length_2.setter
    def name_length_2(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_length_2 = value

    @property
    def name_length(self) -> int:
        """"""
        if Version(Dat.AOE1_1997.ver()) >= self._dat.struct_ver >= Version(Dat.SWGB_EXPANSION.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_length


    @name_length.setter
    def name_length(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_length = value

    @property
    def unit_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.unit_id

    @unit_id.setter
    def unit_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.unit_id = value

    @property
    def language_dll_name_1(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_DE_START.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.language_dll_name_1

    @language_dll_name_1.setter
    def language_dll_name_1(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.language_dll_name_1 = value

    @property
    def language_dll_creation_1(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_DE_START.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.language_dll_creation_1

    @language_dll_creation_1.setter
    def language_dll_creation_1(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.language_dll_creation_1 = value

    @property
    def language_dll_name_2(self) -> int:
        """"""
        if self._dat.struct_ver <= Version(Dat.SWGB_EXPANSION.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.language_dll_name_2

    @language_dll_name_2.setter
    def language_dll_name_2(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.language_dll_name_2 = value

    @property
    def language_dll_creation_2(self) -> int:
        """"""
        if self._dat.struct_ver <= Version(Dat.SWGB_EXPANSION.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.language_dll_creation_2

    @language_dll_creation_2.setter
    def language_dll_creation_2(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.language_dll_creation_2 = value

    @property
    def unit_class(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.unit_class

    @unit_class.setter
    def unit_class(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.unit_class = value

    @property
    def standing_graphic_0_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.idle_graphic_0

    @standing_graphic_0_id.setter
    def standing_graphic_0_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.idle_graphic_0 = value



    @property
    def standing_graphic_1_id(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_AOK_1999.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.idle_graphic_1

    @standing_graphic_1_id.setter
    def standing_graphic_1_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.idle_graphic_1 = value

    @property
    def dying_graphic_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.dying_graphic

    @dying_graphic_id.setter
    def dying_graphic_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.dying_graphic = value

    @property
    def undead_graphic_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.undead_graphic

    @undead_graphic_id.setter
    def undead_graphic_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.undead_graphic = value

    @property
    def death_mode(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.death_mode

    @death_mode.setter
    def death_mode(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.death_mode = value

    @property
    def hit_points(self) -> int:
        """Stores hit_points of a unit"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.hit_points

    @hit_points.setter
    def hit_points(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.hit_points = value


    @property
    def line_of_sight(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.line_of_sight

    @line_of_sight.setter
    def line_of_sight(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.line_of_sight = value

    @property
    def garrison_capacity(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.garrison_capacity

    @garrison_capacity.setter
    def garrison_capacity(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.garrison_capacity = value

    @property
    def radius_x(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.radius_x

    @radius_x.setter
    def radius_x(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.radius_x = value

    @property
    def radius_y(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.radius_y

    @radius_y.setter
    def radius_y(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.radius_y = value

    @property
    def radius_z(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.radius_z

    @radius_z.setter
    def radius_z(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.radius_z = value

    @property
    def train_sound_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.train_sound_id

    @train_sound_id.setter
    def train_sound_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.train_sound_id = value

    @property
    def damage_sound_id_1(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_AOK_1999.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.damage_sound_id_1

    @damage_sound_id_1.setter
    def damage_sound_id_1(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.damage_sound_id_1 = value

    @property
    def dead_unit_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.dead_unit_id

    @dead_unit_id.setter
    def dead_unit_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.dead_unit_id = value

    @property
    def blood_unit_id_1(self) -> int:
        """"""
        if self._dat.struct_ver == Version(Dat.AOE1DE.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.blood_unit_id_1

    @blood_unit_id_1.setter
    def blood_unit_id_1(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.blood_unit_id_1 = value


    @property
    def blood_unit_id_2(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_DE_START.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.blood_unit_id_2

    @blood_unit_id_2.setter
    def blood_unit_id_2(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.blood_unit_id_2 = value

    @property
    def placement_mode(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.placement_mode

    @placement_mode.setter
    def placement_mode(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.placement_mode = value

    @property
    def can_be_built_on(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.can_be_built_on

    @can_be_built_on.setter
    def can_be_built_on(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.can_be_built_on = value

    @property
    def icon_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.icon_id

    @icon_id.setter
    def icon_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.icon_id = value

    @property
    def hidden_in_editor(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.hidden_in_editor

    @hidden_in_editor.setter
    def hidden_in_editor(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.hidden_in_editor = value

    @property
    def old_portrait_icon_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.old_portrait_icon_id

    @old_portrait_icon_id.setter
    def old_portrait_icon_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.old_portrait_icon_id = value

    @property
    def enabled(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.enabled

    @enabled.setter
    def enabled(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.enabled = value

    @property
    def disabled(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_AOK_1999.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.disabled

    @disabled.setter
    def disabled(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.disabled = value

    @property
    def placement_side_terrain0(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.placement_side_terrain0

    @placement_side_terrain0.setter
    def placement_side_terrain0(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.placement_side_terrain0 = value

    @property
    def placement_side_terrain1(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.placement_side_terrain1

    @placement_side_terrain1.setter
    def placement_side_terrain1(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.placement_side_terrain1 = value

    @property
    def placement_terrain0(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.placement_terrain0

    @placement_terrain0.setter
    def placement_terrain0(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.placement_terrain0 = value

    @property
    def placement_terrain1(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.placement_terrain1

    @placement_terrain1.setter
    def placement_terrain1(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.placement_terrain1 = value

    @property
    def clearance_size_x(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.clearance_size_x

    @clearance_size_x.setter
    def clearance_size_x(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.clearance_size_x = value

    @property
    def clearance_size_y(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.clearance_size_y

    @clearance_size_y.setter
    def clearance_size_y(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.clearance_size_y = value

    @property
    def elevation_mode(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.elevation_mode

    @elevation_mode.setter
    def elevation_mode(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.elevation_mode = value

    @property
    def visible_in_fog(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.visible_in_fog

    @visible_in_fog.setter
    def visible_in_fog(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.visible_in_fog = value

    @property
    def terrain_restriction(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.terrain_restriction

    @terrain_restriction.setter
    def terrain_restriction(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.terrain_restriction = value

    @property
    def fly_mode(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.fly_mode

    @fly_mode.setter
    def fly_mode(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.fly_mode = value

    @property
    def resource_capacity(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.resource_capacity

    @resource_capacity.setter
    def resource_capacity(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.resource_capacity = value

    @property
    def resource_decay(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.resource_decay

    @resource_decay.setter
    def resource_decay(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.resource_decay = value

    @property
    def blast_defense_level(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.blast_defense_level

    @blast_defense_level.setter
    def blast_defense_level(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.blast_defense_level = value

    @property
    def combat_level(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.combat_level

    @combat_level.setter
    def combat_level(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.combat_level = value

    @property
    def interaction_mode(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.interaction_mode

    @interaction_mode.setter
    def interaction_mode(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.interaction_mode = value

    @property
    def map_draw_level(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.map_draw_level

    @map_draw_level.setter
    def map_draw_level(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.map_draw_level = value

    @property
    def unit_level(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.unit_level

    @unit_level.setter
    def unit_level(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.unit_level = value

    @property
    def attack_reaction(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.attack_reaction

    @attack_reaction.setter
    def attack_reaction(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.attack_reaction = value

    @property
    def minimap_color(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.minimap_color

    @minimap_color.setter
    def minimap_color(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.minimap_color = value

    @property
    def language_dll_help(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.language_dll_help

    @language_dll_help.setter
    def language_dll_help(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.language_dll_help = value

    @property
    def language_dll_hotkey_text(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.language_dll_hotkey_text

    @language_dll_hotkey_text.setter
    def language_dll_hotkey_text(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.language_dll_hotkey_text = value

    @property
    def hot_keys(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.hot_keys

    @hot_keys.setter
    def hot_keys(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.hot_keys = value

    @property
    def recyclable(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.recyclable

    @recyclable.setter
    def recyclable(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.recyclable = value

    @property
    def enable_auto_gather(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.enable_auto_gather

    @enable_auto_gather.setter
    def enable_auto_gather(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.enable_auto_gather = value

    @property
    def doppelgaenger_on_death(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.doppelgaenger_on_death

    @doppelgaenger_on_death.setter
    def doppelgaenger_on_death(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.doppelgaenger_on_death = value

    @property
    def resource_gather_drop(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.resource_gather_drop

    @resource_gather_drop.setter
    def resource_gather_drop(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.resource_gather_drop = value

    @property
    def occlusion_mode(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_AOK_1999.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.occlusion_mode

    @occlusion_mode.setter
    def occlusion_mode(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.occlusion_mode = value

    @property
    def obstruction_type_1(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_AOK_1999.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.obstruction_type_1

    @obstruction_type_1.setter
    def obstruction_type_1(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.obstruction_type_1 = value

    @property
    def obstruction_class_1(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_AOK_1999.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.obstruction_class_1

    @obstruction_class_1.setter
    def obstruction_class_1(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.obstruction_class_1 = value


    @property
    def trait(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_CONQUERORS_2000.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.trait

    @trait.setter
    def trait(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.trait = value

    @property
    def civilization_id(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_CONQUERORS_2000.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.civilization_id

    @civilization_id.setter
    def civilization_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.civilization_id = value

    @property
    def attribute_piece(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_CONQUERORS_2000.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.attribute_piece

    @attribute_piece.setter
    def attribute_piece(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.attribute_piece = value


    @property
    def obstruction_type_2(self) -> int:
        """"""
        if self._dat.struct_ver == Version(Dat.AOE1DE.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.obstruction_type_2

    @obstruction_type_2.setter
    def obstruction_type_2(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.obstruction_type_2 = value

    @property
    def obstruction_class_2(self) -> int:
        """"""
        if self._dat.struct_ver == Version(Dat.AOE1DE.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.obstruction_class_2

    @obstruction_class_2.setter
    def obstruction_class_2(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.obstruction_class_2 = value

    @property
    def selection_effect(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.selection_effect

    @selection_effect.setter
    def selection_effect(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.selection_effect = value

    @property
    def editor_selection_color(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.editor_selection_color

    @editor_selection_color.setter
    def editor_selection_color(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.editor_selection_color = value

    @property
    def selection_shape_x(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.selection_shape_x

    @selection_shape_x.setter
    def selection_shape_x(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.selection_shape_x = value

    @property
    def selection_shape_y(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.selection_shape_y

    @selection_shape_y.setter
    def selection_shape_y(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.selection_shape_y = value

    @property
    def selection_shape_z(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.selection_shape_z

    @selection_shape_z.setter
    def selection_shape_z(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.selection_shape_z = value


    @property
    def scenario_trigger_data0(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_DE_START.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.scenario_trigger_data0

    @scenario_trigger_data0.setter
    def scenario_trigger_data0(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.scenario_trigger_data0 = value

    @property
    def scenario_trigger_data1(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_DE_START.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.scenario_trigger_data1

    @scenario_trigger_data1.setter
    def scenario_trigger_data1(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.scenario_trigger_data1 = value

    @property
    def resource_storage(self) -> list[ResourceStorage]:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.resource_storage

    @resource_storage.setter
    def resource_storage(self, value: list[ResourceStorage]):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.resource_storage = value

    @property
    def damage_graphics(self) -> list[DamageGraphic]:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.damage_graphics

    @damage_graphics.setter
    def damage_graphics(self, value: list[DamageGraphic]):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.damage_graphics = value

    @property
    def selection_sound_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.selection_sound_id

    @selection_sound_id.setter
    def selection_sound_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.selection_sound_id = value

    @property
    def dying_sound_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.dying_sound_id

    @dying_sound_id.setter
    def dying_sound_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.dying_sound_id = value

    @property
    def wwise_train_sound_id(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_DE_START.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.wwise_train_sound_id

    @wwise_train_sound_id.setter
    def wwise_train_sound_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.wwise_train_sound_id = value

    @property
    def wwise_damage_sound_id(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_DE_START.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.wwise_damage_sound_id

    @wwise_damage_sound_id.setter
    def wwise_damage_sound_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.wwise_damage_sound_id = value

    @property
    def wwise_selection_sound_id(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_DE_START.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.wwise_selection_sound_id

    @wwise_selection_sound_id.setter
    def wwise_selection_sound_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.wwise_selection_sound_id = value

    @property
    def wwise_dying_sound_id(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_DE_START.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.wwise_dying_sound_id

    @wwise_dying_sound_id.setter
    def wwise_dying_sound_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.wwise_dying_sound_id = value

    @property
    def old_attack_mode(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.old_attack_mode

    @old_attack_mode.setter
    def old_attack_mode(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.old_attack_mode = value

    @property
    def convert_terrain(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.convert_terrain

    @convert_terrain.setter
    def convert_terrain(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.convert_terrain = value


    @property
    def name_len_debug_1(self) -> int:
        """"""
        if self._dat.struct_ver == Version(Dat.AOE1DE.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_len_debug_1

    @name_len_debug_1.setter
    def name_len_debug_1(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_len_debug_1 = value


    @property
    def name_len_debug_2(self) -> int:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_DE_START.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_len_debug_2

    @name_len_debug_2.setter
    def name_len_debug_2(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_len_debug_2 = value


    @property
    def name_1(self) -> str:
        """"""
        if self._dat.struct_ver == Version(Dat.AOE1DE.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_1

    @name_1.setter
    def name_1(self, value: str):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_1 = value


    @property
    def name_2(self) -> str:
        """"""
        if self._dat.struct_ver >= Version(Dat.AOE2_DE_START.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_2

    @name_2.setter
    def name_2(self, value: str):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_2 = value


    @property
    def name_3(self) -> str:
        """"""
        if self._dat.struct_ver <= Version(Dat.AOE1DE_ORIGINAL.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_3

    @name_3.setter
    def name_3(self, value: str):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_3 = value


    @property
    def name_4(self) -> str:
        """"""
        if Version(Dat.AOE2_AOK_1999.ver()) < self._dat.struct_ver <= Version(Dat.SWGB_EXPANSION.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_4

    @name_4.setter
    def name_4(self, value: str):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_4 = value

    @property
    def name_5(self) -> str:
        """"""
        if Version(Dat.SWGB.ver()) <= self._dat.struct_ver <= Version(Dat.SWGB_EXPANSION.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_5

    @name_5.setter
    def name_5(self, value: str):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.name_5 = value

    @property
    def unit_line_id(self) -> int:
        """"""
        if Version(Dat.SWGB.ver()) <= self._dat.struct_ver <= Version(Dat.SWGB_EXPANSION.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.unit_line_id

    @unit_line_id.setter
    def unit_line_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.unit_line_id = value

    @property
    def min_tech_level(self) -> int:
        """"""
        if Version(Dat.SWGB.ver()) <= self._dat.struct_ver <= Version(Dat.SWGB_EXPANSION.ver()):
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.min_tech_level

    @min_tech_level.setter
    def min_tech_level(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.min_tech_level = value

    @property
    def id1(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.id1

    @id1.setter
    def id1(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.id1 = value

    @property
    def id2(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.id2

    @id2.setter
    def id2(self, value: int):
        if Version(Dat.AOE2_AOK_1999.ver()) <= self._dat.struct_ver:
            self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.id2 = value


        #if self.unit_type >= 20:
    @property
    def speed(self) -> float:
        """"""
        if self.unit_type >= 20:
            return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_20[0].speed

    @speed.setter
    def speed(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_20[0].speed = value


        """if self.unit_type >= 25:
            pass
        if self.unit_type >= 30:
    @property
    def walking_graphic_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].move_graphics

    @walking_graphic_id.setter
    def walking_graphic_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].move_graphics = value

    @property
    def run_graphic_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].run_graphics

    @run_graphic_id.setter
    def run_graphic_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].run_graphics = value

    @property
    def turn_speed(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].turn_speed

    @turn_speed.setter
    def turn_speed(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].turn_speed = value

    @property
    def old_size_class(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].old_size_class

    @old_size_class.setter
    def old_size_class(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].old_size_class = value

    @property
    def trail_unit_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].trail_unit_id

    @trail_unit_id.setter
    def trail_unit_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].trail_unit_id = value

    @property
    def trail_options(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].trail_options

    @trail_options.setter
    def trail_options(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].trail_options = value

    @property
    def trail_spacing(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].trail_spacing

    @trail_spacing.setter
    def trail_spacing(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].trail_spacing = value

    @property
    def old_move_algorithm(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].old_move_algorithm

    @old_move_algorithm.setter
    def old_move_algorithm(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].old_move_algorithm = value

if self._dat.struct_ver >= Version(Dat.AOE2_AOK_1999.ver()):
    @property
    def turn_radius(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].turn_radius

    @turn_radius.setter
    def turn_radius(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].turn_radius = value

    @property
    def turn_radius_speed(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].turn_radius_speed

    @turn_radius_speed.setter
    def turn_radius_speed(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].turn_radius_speed = value

    @property
    def max_yaw_per_sec_moving(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].max_yaw_per_sec_moving

    @max_yaw_per_sec_moving.setter
    def max_yaw_per_sec_moving(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].max_yaw_per_sec_moving = value

    @property
    def stationary_yaw_revolution_time(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].stationary_yaw_revolution_time

    @stationary_yaw_revolution_time.setter
    def stationary_yaw_revolution_time(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].stationary_yaw_revolution_time = value

    @property
    def max_yaw_per_sec_stationary(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].max_yaw_per_sec_stationary

    @max_yaw_per_sec_stationary.setter
    def max_yaw_per_sec_stationary(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].max_yaw_per_sec_stationary = value

if self._dat.struct_ver >= Version(Dat.AOE2_DE_START.ver()):
    @property
    def min_collision_size_multiplier(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].min_collision_size_multiplier

    @min_collision_size_multiplier.setter
    def min_collision_size_multiplier(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_30[0].min_collision_size_multiplier = value

        if self.unit_type >= 40:
    @property
    def default_task_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].default_task_id

    @default_task_id.setter
    def default_task_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].default_task_id = value

    @property
    def search_radius(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].search_radius

    @search_radius.setter
    def search_radius(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].search_radius = value

    @property
    def work_rate(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].work_rate

    @work_rate.setter
    def work_rate(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].work_rate = value

if self._dat.struct_ver >= Version(Dat.AOE2_DE_START.ver()):
    @property
    def drop_sites_1(self) -> list[int]:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].drop_sites_1

    @drop_sites_1.setter
    def drop_sites_1(self, value: list[int]):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].drop_sites_1 = value

            if Version(Dat.AOE2_AOK_1999.ver()) < self._dat.struct_ver <= Version(Dat.SWGB_EXPANSION.ver()):
    @property
    def drop_sites_2(self) -> list[int]:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].drop_sites_2

    @drop_sites_2.setter
    def drop_sites_2(self, value: list[int]):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].drop_sites_2 = value

    @property
    def drop_sites(self) -> drop_sites:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].drop_sites

    @drop_sites.setter
    def drop_sites(self, value: drop_sites):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].drop_sites = value

    @property
    def task_group(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].task_group

    @task_group.setter
    def task_group(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].task_group = value

    @property
    def command_sound_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].command_sound_id

    @command_sound_id.setter
    def command_sound_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].command_sound_id = value

    @property
    def stop_sound_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].stop_sound_id

    @stop_sound_id.setter
    def stop_sound_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].stop_sound_id = value

if self._dat.struct_ver >= Version(Dat.AOE2_DE_START.ver()):
    @property
    def wwise_attack_sound_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].wwise_attack_sound_id

    @wwise_attack_sound_id.setter
    def wwise_attack_sound_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].wwise_attack_sound_id = value

    @property
    def wwise_move_sound_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].wwise_move_sound_id

    @wwise_move_sound_id.setter
    def wwise_move_sound_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].wwise_move_sound_id = value

    @property
    def run_pattern(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].run_pattern

    @run_pattern.setter
    def run_pattern(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].run_pattern = value

            if Version(Dat.AOE1_1997.ver()) < self._dat.struct_ver <= Version(Dat.AOE1DE.ver()):
    @property
    def unit_commands_1(self) -> list[UnitCommand]:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].unit_commands_1

    @unit_commands_1.setter
    def unit_commands_1(self, value: list[UnitCommand]):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].unit_commands_1 = value

if self._dat.struct_ver >= Version(Dat.AOE2_DE_START.ver()):
    @property
    def unit_commands_2(self) -> list[UnitCommand]:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].unit_commands_2

    @unit_commands_2.setter
    def unit_commands_2(self, value: list[UnitCommand]):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].unit_commands_2 = value

if self._dat.struct_ver >= Version(Dat.AOE2_DE_START.ver()):  # NB also missing other versions that use this
    @property
    def unit_commands(self) -> unit_commands:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].unit_commands

    @unit_commands.setter
    def unit_commands(self, value: unit_commands):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_40[0].unit_commands = value


        if self.unit_type == 60:
    @property
    def projectile_type(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_60[0].projectile_type

    @projectile_type.setter
    def projectile_type(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_60[0].projectile_type = value

    @property
    def smart_mode(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_60[0].smart_mode

    @smart_mode.setter
    def smart_mode(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_60[0].smart_mode = value

    @property
    def drop_animation_mode(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_60[0].drop_animation_mode

    @drop_animation_mode.setter
    def drop_animation_mode(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_60[0].drop_animation_mode = value

    @property
    def penetration_mode(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_60[0].penetration_mode

    @penetration_mode.setter
    def penetration_mode(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_60[0].penetration_mode = value

    @property
    def area_of_effect_special(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_60[0].area_of_effect_special

    @area_of_effect_special.setter
    def area_of_effect_special(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_60[0].area_of_effect_special = value

    @property
    def projectile_arc(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_60[0].projectile_arc

    @projectile_arc.setter
    def projectile_arc(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_60[0].projectile_arc = value


        if self.unit_type > 60:
            if Version(Dat.AOE1_1997.ver()) <= self._dat.struct_ver <= Version(Dat.AOE1DE.ver()):
    @property
    def default_armor_1(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].default_armor_1

    @default_armor_1.setter
    def default_armor_1(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].default_armor_1 = value

if self._dat.struct_ver == Version(Dat.AOE1DE.ver()):
    @property
    def default_armor_2(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].default_armor_2

    @default_armor_2.setter
    def default_armor_2(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].default_armor_2 = value

if self._dat.struct_ver == Version(Dat.AOE2_AOK_1999.ver()):
    @property
    def default_armor_3(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].default_armor_3

    @default_armor_3.setter
    def default_armor_3(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].default_armor_3 = value

            if Version(Dat.AOE2_CONQUERORS_2000.ver()) <= self._dat.struct_ver <= Version(Dat.AOE2_HD_DLC.ver()):
    @property
    def default_armor_4(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].default_armor_4

    @default_armor_4.setter
    def default_armor_4(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].default_armor_4 = value

            if Version(Dat.SWGB.ver()) <= self._dat.struct_ver <= Version(Dat.SWGB_EXPANSION.ver()):
    @property
    def default_armor_5(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].default_armor_5

    @default_armor_5.setter
    def default_armor_5(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].default_armor_5 = value

            if Version(Dat.AOE2_DE_START.ver()) <= self._dat.struct_ver:
    @property
    def default_armor_6(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].default_armor_6

    @default_armor_6.setter
    def default_armor_6(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].default_armor_6 = value


    @property
    def default_armor(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].default_armor


    @default_armor.setter
    def default_armor(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].default_armor = value

            if Version(Dat.AOE1_1997.ver()) <= self._dat.struct_ver:
    @property
    def attacks_1(self) -> list[int]:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].attacks_1

    @attacks_1.setter
    def attacks_1(self, value: list[int]):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].attacks_1 = value

    @property
    def armors_1(self) -> list[int]:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].armors_1

    @armors_1.setter
    def armors_1(self, value: list[int]):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].armors_1 = value

    @property
    def boundary_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].boundary_id

    @boundary_id.setter
    def boundary_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].boundary_id = value

            if Version(Dat.AOE2_DE_START.ver()) <= self._dat.struct_ver:
    @property
    def bonus_damage_resistance(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].bonus_damage_resistance

    @bonus_damage_resistance.setter
    def bonus_damage_resistance(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].bonus_damage_resistance = value

    @property
    def weapon_range_max(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].weapon_range_max

    @weapon_range_max.setter
    def weapon_range_max(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].weapon_range_max = value

    @property
    def blast_range(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].blast_range

    @blast_range.setter
    def blast_range(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].blast_range = value

    @property
    def attack_speed(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].attack_speed

    @attack_speed.setter
    def attack_speed(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].attack_speed = value

    @property
    def projectile_id0(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].projectile_id0

    @projectile_id0.setter
    def projectile_id0(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].projectile_id0 = value

    @property
    def accuracy(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].accuracy

    @accuracy.setter
    def accuracy(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].accuracy = value

    @property
    def break_off_combat(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].break_off_combat

    @break_off_combat.setter
    def break_off_combat(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].break_off_combat = value

    @property
    def frame_delay(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].frame_delay

    @frame_delay.setter
    def frame_delay(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].frame_delay = value

    @property
    def weapon_offset(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].weapon_offset

    @weapon_offset.setter
    def weapon_offset(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].weapon_offset = value

    @property
    def blast_level_offence(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].blast_level_offence

    @blast_level_offence.setter
    def blast_level_offence(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].blast_level_offence = value

    @property
    def weapon_range_min(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].weapon_range_min

    @weapon_range_min.setter
    def weapon_range_min(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].weapon_range_min = value

            if Version(Dat.AOE2_AOK_1999.ver()) <= self._dat.struct_ver:
    @property
    def accuracy_dispersion(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].accuracy_dispersion

    @accuracy_dispersion.setter
    def accuracy_dispersion(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].accuracy_dispersion = value

    @property
    def attack_graphic_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].attack_graphic_id

    @attack_graphic_id.setter
    def attack_graphic_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].attack_graphic_id = value

    @property
    def melee_armor_displayed(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].melee_armor_displayed

    @melee_armor_displayed.setter
    def melee_armor_displayed(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].melee_armor_displayed = value

    @property
    def attack_displayed(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].attack_displayed

    @attack_displayed.setter
    def attack_displayed(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].attack_displayed = value

    @property
    def range_displayed(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].range_displayed

    @range_displayed.setter
    def range_displayed(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].range_displayed = value

    @property
    def reload_time_displayed(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].reload_time_displayed

    @reload_time_displayed.setter
    def reload_time_displayed(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].reload_time_displayed = value

            if Version(Dat.AOE2_DE_LATEST.ver()) <= self._dat.struct_ver: # May need to update to when this was added
    @property
    def blast_damage(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].blast_damage

    @blast_damage.setter
    def blast_damage(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].attacking_type[0].blast_damage = value


        if self.unit_type >= 70:
    @property
    def resource_cost(self) -> list[ResourceCost]:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].resource_cost

    @resource_cost.setter
    def resource_cost(self, value: list[ResourceCost]):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].resource_cost = value

    @property
    def creation_time(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].creation_time

    @creation_time.setter
    def creation_time(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].creation_time = value

    @property
    def train_location_i(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].train_location_i

    @train_location_i.setter
    def train_location_i(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].train_location_i = value

    @property
    def creation_button_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].creation_button_id

    @creation_button_id.setter
    def creation_button_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].creation_button_id = value

            if Version(Dat.AOE2_DE_START.ver()) <= self._dat.struct_ver:
    @property
    def heal_timer(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].heal_timer

    @heal_timer.setter
    def heal_timer(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].heal_timer = value

            if Version(Dat.AOE2_AOK_1999.ver()) <= self._dat.struct_ver <= Version(Dat.SWGB_EXPANSION.ver()):
    @property
    def rear_attack_modifier(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].rear_attack_modifier

    @rear_attack_modifier.setter
    def rear_attack_modifier(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].rear_attack_modifier = value

            if Version(Dat.AOE2_AOK_1999.ver()) <= self._dat.struct_ver:
    @property
    def flank_attack_modifier(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].flank_attack_modifier

    @flank_attack_modifier.setter
    def flank_attack_modifier(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].flank_attack_modifier = value

    @property
    def creatable_type(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].creatable_type

    @creatable_type.setter
    def creatable_type(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].creatable_type = value

    @property
    def hero_mode(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].hero_mode

    @hero_mode.setter
    def hero_mode(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].hero_mode = value

    @property
    def garrison_graphic(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].garrison_graphic

    @garrison_graphic.setter
    def garrison_graphic(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].garrison_graphic = value

            if Version(Dat.AOE2_DE_START.ver()) <= self._dat.struct_ver:
    @property
    def spawn_graphic_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].spawn_graphic_id

    @spawn_graphic_id.setter
    def spawn_graphic_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].spawn_graphic_id = value

    @property
    def upgrade_graphic_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].upgrade_graphic_id

    @upgrade_graphic_id.setter
    def upgrade_graphic_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].upgrade_graphic_id = value

    @property
    def hero_glow_graphic_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].hero_glow_graphic_id

    @hero_glow_graphic_id.setter
    def hero_glow_graphic_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].hero_glow_graphic_id = value

    @property
    def max_charge(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].max_charge

    @max_charge.setter
    def max_charge(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].max_charge = value

    @property
    def charge_regen_rate(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].charge_regen_rate

    @charge_regen_rate.setter
    def charge_regen_rate(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].charge_regen_rate = value

    @property
    def charge_cost(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].charge_cost

    @charge_cost.setter
    def charge_cost(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].charge_cost = value

    @property
    def charge_type(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].charge_type

    @charge_type.setter
    def charge_type(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].charge_type = value

    @property
    def unknown_12_bytes(self) -> bytes:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].unknown_12_bytes

    @unknown_12_bytes.setter
    def unknown_12_bytes(self, value: bytes):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].unknown_12_bytes = value

            if Version(Dat.AOE2_AOK_1999.ver()) <= self._dat.struct_ver:
    @property
    def projectile_min_count(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].projectile_min_count

    @projectile_min_count.setter
    def projectile_min_count(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].projectile_min_count = value

    @property
    def projectile_max_count(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].projectile_max_count

    @projectile_max_count.setter
    def projectile_max_count(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].projectile_max_count = value

    @property
    def projectile_spawning_area_width(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].projectile_spawning_area_width

    @projectile_spawning_area_width.setter
    def projectile_spawning_area_width(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].projectile_spawning_area_width = value

    @property
    def projectile_spawning_area_length(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].projectile_spawning_area_length

    @projectile_spawning_area_length.setter
    def projectile_spawning_area_length(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].projectile_spawning_area_length = value

    @property
    def projectile_spawning_area_randomness(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].projectile_spawning_area_randomness

    @projectile_spawning_area_randomness.setter
    def projectile_spawning_area_randomness(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].projectile_spawning_area_randomness = value

    @property
    def projectile_id1(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].projectile_id1

    @projectile_id1.setter
    def projectile_id1(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].projectile_id1 = value

    @property
    def special_graphic_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].special_graphic_id

    @special_graphic_id.setter
    def special_graphic_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].special_graphic_id = value

    @property
    def special_activation(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].special_activation

    @special_activation.setter
    def special_activation(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].special_activation = value

    @property
    def pierce_armor_displayed(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].pierce_armor_displayed

    @pierce_armor_displayed.setter
    def pierce_armor_displayed(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_70[0].pierce_armor_displayed = value


        if self.unit_type >= 80:
    @property
    def construction_graphic_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].construction_graphic_id

    @construction_graphic_id.setter
    def construction_graphic_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].construction_graphic_id = value

            if Version(Dat.AOE2_CONQUERORS_2000.ver()) <= self._dat.struct_ver:
    @property
    def snow_graphic_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].snow_graphic_id

    @snow_graphic_id.setter
    def snow_graphic_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].snow_graphic_id = value

            if Version(Dat.AOE2_DE_START.ver()) <= self._dat.struct_ver:
    @property
    def destruction_graphic_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].destruction_graphic_id

    @destruction_graphic_id.setter
    def destruction_graphic_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].destruction_graphic_id = value

    @property
    def destruction_rubble_graphic_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].destruction_rubble_graphic_id

    @destruction_rubble_graphic_id.setter
    def destruction_rubble_graphic_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].destruction_rubble_graphic_id = value

    @property
    def research_graphic_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].research_graphic_id

    @research_graphic_id.setter
    def research_graphic_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].research_graphic_id = value

    @property
    def research_complete_graphic_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].research_complete_graphic_id

    @research_complete_graphic_id.setter
    def research_complete_graphic_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].research_complete_graphic_id = value

    @property
    def adjacent_mode(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].adjacent_mode

    @adjacent_mode.setter
    def adjacent_mode(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].adjacent_mode = value

    @property
    def graphics_angle(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].graphics_angle

    @graphics_angle.setter
    def graphics_angle(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].graphics_angle = value

    @property
    def disappears_when_built(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].disappears_when_built

    @disappears_when_built.setter
    def disappears_when_built(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].disappears_when_built = value

    @property
    def stack_unit_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].stack_unit_id

    @stack_unit_id.setter
    def stack_unit_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].stack_unit_id = value

    @property
    def foundation_terrain_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].foundation_terrain_id

    @foundation_terrain_id.setter
    def foundation_terrain_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].foundation_terrain_id = value

    @property
    def old_overlay_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].old_overlay_id

    @old_overlay_id.setter
    def old_overlay_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].old_overlay_id = value

    @property
    def research_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].research_id

    @research_id.setter
    def research_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].research_id = value

            if Version(Dat.AOE2_AOK_1999.ver()) <= self._dat.struct_ver:
    @property
    def can_burn(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].can_burn

    @can_burn.setter
    def can_burn(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].can_burn = value

    @property
    def building_annex(self) -> BuildingAnnex:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].building_annex

    @building_annex.setter
    def building_annex(self, value: BuildingAnnex):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].building_annex = value

    @property
    def head_unit_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].head_unit_id

    @head_unit_id.setter
    def head_unit_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].head_unit_id = value

    @property
    def transform_unit_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].transform_unit_id

    @transform_unit_id.setter
    def transform_unit_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].transform_unit_id = value

    @property
    def transform_sound_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].transform_sound_id

    @transform_sound_id.setter
    def transform_sound_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].transform_sound_id = value

    @property
    def construction_sound_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].construction_sound_id

    @construction_sound_id.setter
    def construction_sound_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].construction_sound_id = value

            if Version(Dat.AOE2_DE_START.ver()) <= self._dat.struct_ver:
    @property
    def wwise_construction_sound_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].wwise_construction_sound_id

    @wwise_construction_sound_id.setter
    def wwise_construction_sound_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].wwise_construction_sound_id = value

    @property
    def wwise_transform_sound_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].wwise_transform_sound_id

    @wwise_transform_sound_id.setter
    def wwise_transform_sound_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].wwise_transform_sound_id = value

            if Version(Dat.AOE2_AOK_1999.ver()) <= self._dat.struct_ver:
    @property
    def garrison_type(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].garrison_type

    @garrison_type.setter
    def garrison_type(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].garrison_type = value

    @property
    def garrison_heal_rate(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].garrison_heal_rate

    @garrison_heal_rate.setter
    def garrison_heal_rate(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].garrison_heal_rate = value

    @property
    def garrison_repair_rate(self) -> float:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].garrison_repair_rate

    @garrison_repair_rate.setter
    def garrison_repair_rate(self, value: float):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].garrison_repair_rate = value

    @property
    def salvage_unit_id(self) -> int:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].salvage_unit_id

    @salvage_unit_id.setter
    def salvage_unit_id(self, value: int):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].salvage_unit_id = value

    @property
    def salvage_attributes(self) -> LootingTable:
        """"""
        return self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].salvage_attributes

    @salvage_attributes.setter
    def salvage_attributes(self, value: LootingTable):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_80[0].salvage_attributes = value


        if self.unit_type == 90:
            pass"""

    def __repr__(self):
        return "<{klass} @{idr:x} {attrs}>".format(
            klass=self.__class__.__name__,
            idr=id(self) & 0xFFFFFF,
            attrs=" ".join("{}={!r}\n".format(k, v) for k, v in self.__dict__.items() if k != "dat"),
        ) + f"Graphics Data:\n {self.graphics}"

    """def change_hp(self, value):
        self._dat.civs[self._civ_id].unit_data[self._unit_id].type_10.hit_points = value
        self.hitpoints = value"""
