import bpy
from bpy.props import (StringProperty,
                       BoolProperty,
                       FloatVectorProperty,
                       FloatProperty,
                       EnumProperty,
                       IntProperty,
                       PointerProperty)

class WAZOU_PIE_MENUS_OT_pivot_align(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.pivot_align"
    bl_label = "Use Pivot Align"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if bpy.context.space_data.use_pivot_point_align == (False):
            bpy.context.space_data.use_pivot_point_align = True
        elif bpy.context.space_data.use_pivot_point_align == (True):
            bpy.context.space_data.use_pivot_point_align = False
        return {'FINISHED'}


# Pivot to selection
class WAZOU_PIE_MENUS_OT_pivot_to_selection(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.pivot_to_selection"
    bl_label = "Pivot To Selection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        saved_location = bpy.context.scene.cursor.location.copy()
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.scene.cursor.location = saved_location
        return {'FINISHED'}

# Pivot to Bottom
class WAZOU_PIE_MENUS_OT_pivot_to_bottom(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.pivot_to_bottom"
    bl_label = "Pivot To Bottom"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        mode = context.object.mode

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        o = bpy.context.active_object
        init = 0
        for x in o.data.vertices:
            if init == 0:
                a = x.co.z
                init = 1
            elif x.co.z < a:
                a = x.co.z

        for x in o.data.vertices:
            x.co.z -= a

        o.location.z += a
        bpy.ops.object.mode_set(mode=mode)
        return {'FINISHED'}

CLASSES =  [WAZOU_PIE_MENUS_OT_pivot_align,
            WAZOU_PIE_MENUS_OT_pivot_to_selection,
            WAZOU_PIE_MENUS_OT_pivot_to_bottom
            ]

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