import bpy
from bpy.props import (EnumProperty)


class WAZOU_PROPORTIONAL_OT_pie(bpy.types.Operator):
    bl_idname = "wazou_proportional.object"
    bl_label = "Wazou Proportional"
    bl_options = {'REGISTER', 'UNDO'}

    proportional : EnumProperty(
        items=(('smooth', "SMOOTH", "SMOOTH"),
               ('sphere', "SPHERE", "SPHERE"),
               ('root', "ROOT", "ROOT"),
               ('sharp', "SHARP", "SHARP"),
               ('linear', "LINEAR", "LINEAR"),
               ('constant', "CONSTANT", "CONSTANT"),
               ('random', "RANDOM", "RANDOM"),
               ('connected', "CONNECTED", "CONNECTED"),
               ('projected', "PROJECTED", "PROJECTED"),
               ('enabled', "ENABLED", "ENABLED"),),
        default='smooth'
    )

    def execute(self, context):
        if context.object.mode == 'EDIT':
            bpy.context.scene.tool_settings.proportional_edit = 'ENABLED'
        elif context.object.mode == 'OBJECT':
            bpy.context.scene.tool_settings.use_proportional_edit_objects = True

        # if context.object.mode == "EDIT":
        if self.proportional == 'smooth':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'SMOOTH'
        elif self.proportional == 'sphere':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'SPHERE'
        elif self.proportional == 'root':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'ROOT'
        elif self.proportional == 'sharp':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'SHARP'
        elif self.proportional == 'linear':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'LINEAR'
        elif self.proportional == 'constant':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'CONSTANT'
        elif self.proportional == 'random':
            bpy.context.scene.tool_settings.proportional_edit_falloff = 'RANDOM'
        elif self.proportional == 'connected':
            bpy.context.scene.tool_settings.proportional_edit = 'CONNECTED'
        elif self.proportional == 'projected':
            bpy.context.scene.tool_settings.proportional_edit = 'PROJECTED'


        return {'FINISHED'}

class WAZOU_PROPORTIONAL_OT_Enable_disable(bpy.types.Operator):
    bl_idname = "wazou_proportional.enable_disable"
    bl_label = "Wazou Proportional Enable/Disable"
    bl_description = 'Enable or Disable Proportionnal Edition'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if bpy.context.scene.tool_settings.proportional_edit != ('DISABLED'):
            bpy.context.scene.tool_settings.proportional_edit = 'DISABLED'
        elif bpy.context.scene.tool_settings.proportional_edit != ('ENABLED'):
            bpy.context.scene.tool_settings.proportional_edit = 'ENABLED'

        return {'FINISHED'}



