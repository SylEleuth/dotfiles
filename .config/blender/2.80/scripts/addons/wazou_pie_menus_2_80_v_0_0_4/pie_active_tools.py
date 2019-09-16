import bpy
from bpy.props import (EnumProperty)

######################
#    Manipulators    #
######################


class WAZOU_PIE_MENUS_OT_active_tools(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.active_tools"
    bl_label = "Wazou active tools"
    bl_options = {'REGISTER', 'UNDO'}

    active_tools: EnumProperty(
        items=(('transform', "Transform", ""),
               ('rotate', "Rotate", ""),
               ('scale', "Scale", ""),
               ('select', "Select", ""),
               ('select_circle', "select Circle", ""),
               ('select_lasso', "Select Lasso", ""),
               ('select_box', "select Box", ""),
               ('move', "Move", ""),
               ('cursor', "Cursor", ""),
               ('scale_cage', "Scale Cage", ""),
               ('gizmo_translate', "TRANSLATE", ""),
               ('gizmo_rotate', "ROTATE", ""),
               ('gizmo_scale', "SCALE", ""),
               ),
        default='transform'
    )

    def execute(self, context):

        # Active Tools Object mode
        if self.active_tools == 'move':
            bpy.ops.wm.tool_set_by_id(name="builtin.move")

        elif self.active_tools == 'rotate':
            bpy.ops.wm.tool_set_by_id(name="builtin.rotate")

        elif self.active_tools == 'scale':
            bpy.ops.wm.tool_set_by_id(name="builtin.scale")

        elif self.active_tools == 'select':
            bpy.ops.wm.tool_set_by_id(name="builtin.select")

        elif self.active_tools == 'select_circle':
            bpy.ops.wm.tool_set_by_id(name="builtin.select_circle")

        elif self.active_tools == 'select_lasso':
            bpy.ops.wm.tool_set_by_id(name="builtin.select_lasso")

        elif self.active_tools == 'select_box':
            bpy.ops.wm.tool_set_by_id(name="builtin.select_box")

        elif self.active_tools == 'cursor':
            bpy.ops.wm.tool_set_by_id(name="builtin.cursor")

        elif self.active_tools == 'scale_cage':
            bpy.ops.wm.tool_set_by_id(name="builtin.scale_cage")

        elif self.active_tools == 'gizmo_translate':
            bpy.context.scene.tool_settings.use_gizmo_mode = {'TRANSLATE'}

        elif self.active_tools == 'gizmo_rotate':
            bpy.context.scene.tool_settings.use_gizmo_mode = {'ROTATE'}

        elif self.active_tools == 'gizmo_scale':
            bpy.context.scene.tool_settings.use_gizmo_mode = {'SCALE'}

        return {'FINISHED'}

CLASSES =  [WAZOU_PIE_MENUS_OT_active_tools]

def register():
    for cls in CLASSES:
        try:
            bpy.utils.register_class(cls)
        except:
            print(f"{cls.__name__} already registred")


def unregister():
    for cls in CLASSES :
        if hasattr(bpy.types, cls.__name__):
            bpy.utils.unregister_class(cls)

