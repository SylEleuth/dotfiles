import bpy
from bpy.props import (EnumProperty)



######################
#      Snapping      #
######################

class WAZOU_PIE_MENUS_OT_snapping(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.snap"
    bl_label = "Wazou Pie Menus Snapping"
    bl_options = {'REGISTER', 'UNDO'}

    snap_elements : EnumProperty(
        items=(('vertex', "VERTEX", "VERTEX"),
               ('edge', "EDGE", "EDGE"),
               ('face', "FACE", "FACE"),
               ('increment', "INCREMENT", "INCREMENT"),
               ('volume', "VOLUME", "VOLUME"),
               ('active', "ACTIVE", "ACTIVE"),
               ('median', "MEDIAN", "MEDIAN"),
               ('center', "CENTER", "CENTER"),
               ('closest', "CLOSEST", "CLOSEST"),
               ),
        default='vertex'
    )

    def execute(self, context):
        bpy.context.scene.tool_settings.use_snap = True

        #Elements
        if self.snap_elements == 'vertex':
            bpy.context.scene.tool_settings.snap_elements = {'VERTEX'}
        elif self.snap_elements == 'edge':
            bpy.context.scene.tool_settings.snap_elements = {'EDGE'}
        elif self.snap_elements == 'face':
            bpy.context.scene.tool_settings.snap_elements = {'FACE'}
        elif self.snap_elements == 'increment':
            bpy.context.scene.tool_settings.snap_elements = {'INCREMENT'}
        elif self.snap_elements == 'volume':
            bpy.context.scene.tool_settings.snap_elements = {'VOLUME'}
        
        #Target
        elif self.snap_elements == 'active':
            bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
        elif self.snap_elements == 'median':
            bpy.context.scene.tool_settings.snap_target = 'MEDIAN'
        elif self.snap_elements == 'center':
            bpy.context.scene.tool_settings.snap_target = 'CENTER'
        elif self.snap_elements == 'closest':
            bpy.context.scene.tool_settings.snap_target = 'CLOSEST'

        return {'FINISHED'}

CLASSES =  [WAZOU_PIE_MENUS_OT_snapping]

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




