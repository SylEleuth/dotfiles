import bpy


# Limited Dissolve
class WAZOU_PIE_MENUS_OT_limited_dissolve(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.limited_dissolve"
    bl_label = "Delete Limited Dissolve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.dissolve_limited(angle_limit=3.14159, use_dissolve_boundaries=False)
        return {'FINISHED'}


CLASSES =  [WAZOU_PIE_MENUS_OT_limited_dissolve]

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