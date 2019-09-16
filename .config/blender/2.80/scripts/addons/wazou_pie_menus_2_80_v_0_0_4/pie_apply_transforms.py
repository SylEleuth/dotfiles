import bpy
from bpy.props import (EnumProperty)

###########################
#    Apply Transforms     #
###########################

class WAZOU_PIE_MENUS_OT_Apply_Clear_transforms(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.apply_clear_transforms"
    bl_label = "Wazou Apply/Clear Transforms"
    bl_options = {'REGISTER', 'UNDO'}

    apply_clear: EnumProperty(
        items=(('apply_location', "APPLY_LOCATION", ""),
               ('apply_rotation', "APPLY_ROTATION", ""),
               ('apply_scale', "APPLY_SCALE", ""),
               ('apply_rot_scale', "APPLY_ROT_SCALE", ""),
               ('apply_all', "APPLY_ALL", ""),
               ('clear_all', "CLEAR_ALL", ""),
               ),
        default='apply_location'
    )

    def execute(self, context):

        # Apply
        if self.apply_clear == 'apply_location':
            bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
        elif self.apply_clear == 'apply_rotation':
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        elif self.apply_clear == 'apply_scale':
            bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        elif self.apply_clear == 'apply_rot_scale':
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        elif self.apply_clear == 'apply_all':
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        # Clear
        elif self.apply_clear == 'clear_all':
            bpy.ops.object.location_clear()
            bpy.ops.object.rotation_clear()
            bpy.ops.object.scale_clear()

        return {'FINISHED'}


CLASSES =  [WAZOU_PIE_MENUS_OT_Apply_Clear_transforms]

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