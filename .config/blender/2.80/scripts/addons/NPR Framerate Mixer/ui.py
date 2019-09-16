import bpy
from bpy.props import *
from bpy.types import UIList, Panel, Operator
from .properties import *
from .operators import *


class CW_PT_tools_panel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_category = 'Framerate Mixer'
    bl_label = "FR Mixer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
          
    def draw(self, context):
        context = bpy.context
        aobj = context.active_object
        layout = self.layout
        scn = context.scene
        scn_prop = scn.frm_props
        
        
        box = layout.box()
        row = box.row()
        row.alignment = 'CENTER'
        row.operator("cw_tools.cw_detect_bake_camera_hold_offsets")
        row.alignment = 'CENTER'
        row = box.row()
        row.alignment = 'CENTER'
        row.prop(scn_prop, 'force_frame_range')
        row.operator("cw_tools.cw_force_bake_camera_hold_offsets")
        row.alignment = 'CENTER'
        
        
        
        return