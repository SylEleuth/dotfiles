import bpy
from bpy.props import (StringProperty,
                       BoolProperty,
                       FloatVectorProperty,
                       FloatProperty,
                       EnumProperty,
                       IntProperty,
                       PointerProperty)

######################
#       Views        #
######################


# Split Areas
class WAZOU_PIE_MENUS_OT_split_areas_vertical(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.split_areas_vertical"
    bl_label = "Wazou split Areas Vertical"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.screen.area_split(direction='VERTICAL')
        return {'FINISHED'}

class WAZOU_PIE_MENUS_OT_split_areas_horizontal(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.split_areas_horizontal"
    bl_label = "Wazou split Areas Horizontal"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        bpy.ops.screen.area_split(direction='HORIZONTAL')
        return {'FINISHED'}

# Join area
class WAZOU_PIE_MENUS_OT_join_areas(bpy.types.Operator):
    """Join 2 area, clic on the second area to join"""
    bl_idname = "wazou_pie_menus.join_areas"
    bl_label = "Wazou Join Area"
    bl_options = {'REGISTER', 'UNDO'}

    min_x : IntProperty()
    min_y : IntProperty()

    def modal(self, context, event):
        if event.type == 'LEFTMOUSE':
            self.max_x = event.mouse_x
            self.max_y = event.mouse_y
            bpy.ops.screen.area_join(min_x=self.min_x, min_y=self.min_y, max_x=self.max_x, max_y=self.max_y)
            bpy.ops.screen.screen_full_area()
            bpy.ops.screen.screen_full_area()
            return {'FINISHED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        self.min_x = event.mouse_x
        self.min_y = event.mouse_y
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}


# View Class menu
class WAZOU_PIE_MENUS_OT_view_menu(bpy.types.Operator):
    """Menu to change views"""
    bl_idname = "wazou_pie_menus.view_menu"
    bl_label = "Wazou View Menu"
    bl_options = {'REGISTER', 'UNDO'}
    ui_type_variable : bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.context.area.ui_type = self.ui_type_variable

        # bpy.context.area.type = self.variable
        return {'FINISHED'}

CLASSES =  [WAZOU_PIE_MENUS_OT_split_areas_vertical,
            WAZOU_PIE_MENUS_OT_split_areas_horizontal,
            WAZOU_PIE_MENUS_OT_join_areas,
            WAZOU_PIE_MENUS_OT_view_menu
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