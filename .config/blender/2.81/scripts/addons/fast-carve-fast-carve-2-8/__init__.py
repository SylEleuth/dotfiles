bl_info = {
    "name": "Fast Carve",
    "description": "Hardsurface utility Blender addon for quick and easy boolean and bevel operations",
    "author": "Jayanam",
    "version": (0, 9, 6, 12),
    "blender": (2, 80, 0),
    "location": "View3D",
    "category": "Object"}

# Blender imports
import bpy

from bpy.props import *

from bpy.types import AddonPreferences

import rna_keymap_ui

from . fc_bevel_op          import FC_BevelOperator
from . fc_unbevel_op        import FC_UnBevelOperator
from . fc_panel             import FC_PT_Panel
from . fc_bevel_panel       import FC_PT_Bevel_Panel
from . fc_primitive_panel   import FC_PT_Primitive_Panel
from . fc_bool_op           import FC_BoolOperator_Diff
from . fc_bool_op           import FC_BoolOperator_Union
from . fc_bool_op           import FC_BoolOperator_Slice
from . fc_bool_op           import FC_BoolOperator_Intersect
from . fc_bool_op           import FC_TargetSelectOperator
from . fc_utils_op          import FC_MirrorOperator
from . fc_utils_op          import FC_SymmetrizeOperator
from . fc_utils_op          import FC_OriginActiveOperator
from . fc_utils_op          import FC_CenterActiveOperator
from . fc_utils_op          import FC_DissolveEdgesOperator
from . fc_utils_op          import FC_UnionSelectedOperator
from . fc_menus             import FC_MT_Bool_Menu
from . fc_apply_bool_op     import FC_ApplyBoolOperator
from . fc_primitive_mode_op import FC_Primitive_Mode_Operator
from . fc_array_mode_op     import FC_Array_Mode_Operator
from . fc_circle_array_mode_op     import FC_Circle_Array_Mode_Operator

from .types.enums import *

# Scene properties
bpy.types.Scene.carver_target = PointerProperty(type=bpy.types.Object)

bpy.types.Scene.apply_bool    = BoolProperty(
                                      name="Apply Immediately", 
                                      description="Apply bool operation immediately",
                                      default = True)

bpy.types.Scene.delete_on_apply   = BoolProperty(
                                      name="Delete after apply", 
                                      description="Delete the object after apply",
                                      default = True)

bpy.types.Scene.use_snapping   = BoolProperty(name="Snap to grid", 
                                        description="Use snapping to the grid",
                                        default = True)

bpy.types.Scene.snap_to_target   = BoolProperty(name="Snap to target", 
                                        description="Snap the primitive to the target",
                                        default = True)

bpy.types.Scene.draw_distance = FloatProperty(
                                      name="Draw Distance", 
                                      description="Distance of primitives to the origin",
                                      default = 2.0)

bpy.types.WindowManager.in_primitive_mode = BoolProperty(name="Primitive Mode",
                                        default = False)

bpy.types.Scene.extrude_mesh  = BoolProperty(name="Extrude mesh", 
                                      description="Extrude the mesh after creation",
                                      default = True)

bpy.types.Scene.fill_mesh  = BoolProperty(name="Fill mesh", 
                                      description="Fill the mesh after creation",
                                      default = True)

mode_items = [ ("Create",     "Create", "", 0),
               ("Difference", "Difference", "", 1),
               ("Union",      "Union", "", 2),
               ("Intersect",  "Intersect", "", 3),
               ("Slice",      "Slice", "", 4)
             ]

center_items = [ ("Mouse",     "Mouse", "", 0),
                 ("3D Cursor", "3D cursor", "", 1)
               ]

bpy.types.Scene.bool_mode = bpy.props.EnumProperty(items=mode_items, 
                                                   name="Mode",
                                                   default="Create")

bpy.types.Scene.center_type = bpy.props.EnumProperty(items=center_items, 
                                                   name="Center_TYpe",
                                                   default="Mouse")

primitive_types = [ ("Polyline",   "Polyline",  "", 0),
                    ("Circle",     "Circle",    "", 1),
                    ("Rectangle",  "Rectangle", "", 2)
                  ]

bpy.types.Scene.primitive_type = bpy.props.EnumProperty(items=primitive_types, 
                                                        name="Primitive",
                                                        default="Polyline")

bpy.types.Scene.start_center    = BoolProperty(
                                      name="From Center", 
                                      description="Start primtive from center",
                                      default = False)


# Addon preferences
class FC_AddonPreferences(AddonPreferences):
    bl_idname = __name__
    
    def draw(self, context):
    
        wm = bpy.context.window_manager 
        km_items = wm.keyconfigs.addon.keymaps['3D View'].keymap_items         
        km_item = km_items['object.fc_immediate_mode_op']

        row = self.layout.row()
        row.label(text=km_item.name)
        row.prop(km_item, 'type', text='', full_event=True)

        km_mnu_item = km_items['wm.call_menu_pie']
        row = self.layout.row()
        row.label(text=km_mnu_item.name)
        row.prop(km_mnu_item, 'type', text='', full_event=True) 

addon_keymaps = []

classes = (
    FC_PT_Panel,
    FC_PT_Bevel_Panel,
    FC_PT_Primitive_Panel,
    FC_BevelOperator,
    FC_UnBevelOperator,
    FC_BoolOperator_Diff,
    FC_BoolOperator_Union,
    FC_BoolOperator_Slice,
    FC_BoolOperator_Intersect,
    FC_TargetSelectOperator,
    FC_MirrorOperator,
    FC_SymmetrizeOperator,
    FC_OriginActiveOperator,
    FC_CenterActiveOperator,
    FC_DissolveEdgesOperator,
    FC_UnionSelectedOperator,
    FC_ApplyBoolOperator,
    FC_Primitive_Mode_Operator,
    FC_Array_Mode_Operator,
    FC_Circle_Array_Mode_Operator,
    FC_MT_Bool_Menu,
    FC_AddonPreferences
)
     
    
def register():
    for c in classes:
        bpy.utils.register_class(c)
   
    # add keymap entry
    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')

    kmi = km.keymap_items.new("object.fc_immediate_mode_op", 'P', 'PRESS', shift=True, ctrl=True)
    addon_keymaps.append((km, kmi))

    kmi = km.keymap_items.new("object.fc_array_mode_op", 'A', 'PRESS', shift=True, ctrl=True)
    addon_keymaps.append((km, kmi))

    kmi = km.keymap_items.new("object.fc_circle_array_mode_op", 'C', 'PRESS', shift=True, ctrl=True)
    addon_keymaps.append((km, kmi))

    kmi_mnu = km.keymap_items.new("wm.call_menu_pie", "COMMA", "PRESS", shift=True)
    kmi_mnu.properties.name = FC_MT_Bool_Menu.bl_idname

    addon_keymaps.append((km, kmi_mnu))
    
def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

    # remove keymap entry
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    addon_keymaps.clear()
