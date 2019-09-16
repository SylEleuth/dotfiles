import bpy
from bpy.props import *
from bpy.types import PropertyGroup



class FRMScnProperties(PropertyGroup):
    force_frame_range: IntProperty(name = "Frames", description = "# of frames forward to bake the camera offset", default = 1, min = 1, max = 1000)
    
    adv_inc_modifiers: BoolProperty(name = 'Include Modifiers', description = 'Include modifiers of mesh', default = True)
    adv_inc_shape_keys: BoolProperty(name = 'Include Shape Keys', description = 'Include shape keys of mesh', default = True)
    
    adv_inc_bbone_settings: BoolProperty(name = 'Include BBone Settings', description = 'Include bbones of bones', default = True)
    
    mesh_adv_menu: BoolProperty(default = False)
    arm_adv_menu: BoolProperty(default = False)