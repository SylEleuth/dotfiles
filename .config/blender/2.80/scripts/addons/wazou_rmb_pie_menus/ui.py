import bpy
import bmesh

# from bpy.types import Menu, Operator
from bpy.types import Menu, Operator, UIList

from bpy.props import PointerProperty, StringProperty, BoolProperty, \
    EnumProperty, IntProperty, FloatProperty, FloatVectorProperty, \
    CollectionProperty, BoolVectorProperty

from bpy.types import Curve, SurfaceCurve, TextCurve

from .operator import *
from .sculpt import *
from bpy.types import Operator, Macro

from mathutils import *
from .functions import *



########################################################################
# Pie Menus 
########################################################################

class WAZOU_RMB_PIE_MENUS_MT_Looptools_Menu(bpy.types.Menu):
    bl_label = "Looptools"
    bl_idname = "OBJECT_MT_looptools_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("wazou_rmb_pie_menus.looptools_circle", text="Circle", icon='MESH_CIRCLE')
        layout.operator("wazou_rmb_pie_menus.looptools_flatten", text="Flatten", icon='SNAP_FACE')
        layout.operator("wazou_rmb_pie_menus.looptools_space", text="Space", icon='UV_EDGESEL')
        layout.operator("wazou_rmb_pie_menus.looptools_relax", text="Relax", icon='GRID')
        layout.operator("wazou_rmb_pie_menus.looptools_bridge", text="Bridge/Loft", icon='SNAP_INCREMENT')
        layout.operator("wazou_rmb_pie_menus.looptools_gstretch", text="Gstretch", icon='PARTICLE_POINT')



# Sculpt Bottom
def Sculpt_Bottom(self, context):
    layout = self.layout
    pie = layout.menu_pie()

    brush = context.tool_settings.sculpt.brush
    capabilities = brush.sculpt_capabilities
    col = pie.column(align=True)
    col.scale_x = 0.8
    if capabilities.has_auto_smooth:
        row = col.row(align=True)

        row.prop(brush, "auto_smooth_factor", slider=True)
        row.prop(brush, "use_inverse_smooth_pressure", toggle=True, text="")

    # normal_weight
    if capabilities.has_normal_weight:
        row = col.row(align=True)
        row.prop(brush, "normal_weight", slider=True)

    # crease_pinch_factor
    if capabilities.has_pinch_factor:
        row = col.row(align=True)
        row.prop(brush, "crease_pinch_factor", slider=True, text="Pinch")

    # use_original_normal and sculpt_plane
    if capabilities.has_sculpt_plane:
        row = col.row(align=True)
        row.prop(brush, "use_original_normal", toggle=True, icon_only=True)
        row.prop(brush, "sculpt_plane", text="")

    # rake_factor
    if capabilities.has_rake_factor:
        col.separator()
        row = col.row(align=True)
        row.prop(brush, "rake_factor", slider=True)

    if brush.sculpt_tool == 'MASK':
        prop_invert_mask = col.operator('paint.mask_flood_fill', text="Invert Mask")
        prop_invert_mask.mode = 'INVERT'

        row = col.row(align=True)
        prop_clear = row.operator('paint.mask_flood_fill', text="Clear")
        prop_clear.mode = 'VALUE'
        prop_clear.value = 0

        prop_fill = row.operator('paint.mask_flood_fill', text="Fill")
        prop_fill.mode = 'VALUE'
        prop_fill.value = 1

        row = col.row(align=True)
        prop_hide_masked = row.operator('paint.hide_show', text="Hide")
        prop_hide_masked.action = 'HIDE'
        prop_hide_masked.area = 'MASKED'

        prop_show_masked = row.operator('paint.hide_show', text="Show")
        prop_show_masked.action = 'SHOW'
        prop_show_masked.area = 'ALL'

        row = col.row(align=True)
        row.operator("view3d.select_box", text="Box")
        row.operator("paint.mask_lasso_gesture", text="Lasso")



        # col.prop(brush, "mask_tool", text="")

    # plane_offset, use_offset_pressure, use_plane_trim, plane_trim
    if capabilities.has_plane_offset:
        row = col.row(align=True)
        row.prop(brush, "plane_offset", slider=True)
        row.prop(brush, "use_offset_pressure", text="")
        row = col.row()
        row.prop(brush, "use_plane_trim", text="Trim")
        row = col.row()
        row.active = brush.use_plane_trim
        row.prop(brush, "plane_trim", slider=True, text="Distance")

    # height
    if capabilities.has_height:
        row = col.row()
        row.prop(brush, "height", slider=True, text="Height")

    # use_frontface
    row = col.row()
    row.prop(brush, "use_frontface", text="Front Faces Only")

    # use_accumulate
    if capabilities.has_accumulate:
        col.prop(brush, "use_accumulate")

# Scupt Symmetrize
def Sculpt_Symmetry(self, context):
    layout = self.layout
    pie = layout.menu_pie()


    sculpt = context.tool_settings.sculpt
    box = pie.split().column()
    row = box.split(align=True)
    row.label(text="Symmetry:")
    row = box.row(align=True)
    row = box.split(align=True)
    row.prop(sculpt, "use_symmetry_x", text="X", toggle=True)
    row.prop(sculpt, "use_symmetry_y", text="Y", toggle=True)
    row.prop(sculpt, "use_symmetry_z", text="Z", toggle=True)

    if context.sculpt_object.use_dynamic_topology_sculpting:
        row = box.row(align=True)
        row.prop(sculpt, "symmetrize_direction")
        row = box.row(align=True)
        row.operator("sculpt.symmetrize")


def Sculpt_Curve_Stroke(self, context):
    layout = self.layout
    pie = layout.menu_pie()
    brush = context.tool_settings.sculpt.brush

    split = pie.split()
    col = split.column(align=True)
    row = col.row(align=True)
    row.label(text="Curve:")
    row = col.row(align=True)
    row.operator("brush.curve_preset", icon='SMOOTHCURVE', text="").shape = 'SMOOTH'
    row.operator("brush.curve_preset", icon='SPHERECURVE', text="").shape = 'ROUND'
    row.operator("brush.curve_preset", icon='ROOTCURVE', text="").shape = 'ROOT'
    row.operator("brush.curve_preset", icon='SHARPCURVE', text="").shape = 'SHARP'
    row.operator("brush.curve_preset", icon='LINCURVE', text="").shape = 'LINE'
    row.operator("brush.curve_preset", icon='NOCURVE', text="").shape = 'MAX'
    row.operator("wazou_rmb_pie_menus.curve_popup", icon='PREFERENCES', text="")

    row = col.row(align=True)
    row.label(text="Stroke Method:")
    row = col.row(align=True)
    row.prop(brush, "stroke_method", text="", icon='IPO_CONSTANT')


def Sculpt_Top(self, context):
    layout = self.layout
    pie = layout.menu_pie()
    ups = context.tool_settings.unified_paint_settings
    brush = context.tool_settings.sculpt.brush

    col = pie.column(align=True)
    # col.scale_x = 0.6
    # settings = context.tool_settings.sculpt


    # col.template_ID_preview(settings, "brush", new="brush.add", rows=3, cols=8)
    col.prop(ups, "size", text="Radius", slider=False)
    col.prop(brush, "strength", slider=True)



def Sculpt_Brush_Preview(self, context):
    layout = self.layout
    pie = layout.menu_pie()
    col = pie.column(align=True)
    row = col.split(align=True)
    col.scale_x = 0.8
    row = col.row(align=True)
    row.separator()
    row = col.row(align=True)
    row.separator()
    row = col.row(align=True)
    row.separator()
    row = col.row(align=True)
    row.separator()
    row = col.row(align=True)
    row.separator()
    row = col.row(align=True)
    row.separator()
    row = col.row(align=True)
    row.separator()
    row = col.row(align=True)
    row.separator()
    row = col.row(align=True)
    row.separator()
    row = col.row(align=True)
    row.separator()

    # brush = context.tool_settings.sculpt.brush
    # col.template_ID_preview(brush, "texture", rows=3, cols=8)
    # col.operator("wazou_rmb_pie_menus.import_image_as_brush", text="Add Texture")


# Curve Popup
class WAZOU_RMB_PIE_MENUS_curve_popup(bpy.types.Operator):
    bl_idname = "wazou_rmb_pie_menus.curve_popup"
    bl_label = "Curve Popup"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def check(self, context):

        return True

    def execute(self, context):
        return {'FINISHED'}


    def draw(self, context):
        layout = self.layout
        # settings = self.paint_settings(context)
        # brush = settings.brush
        brush = context.tool_settings.sculpt.brush
        layout.template_curve_mapping(brush, "curve", brush=True)

    def invoke(self, context, event):
        dpi_value = bpy.context.preferences.view.ui_scale
        return context.window_manager.invoke_props_dialog(self, width=dpi_value * 400, height=100)

# # Wonder Mesh Popup
# class RMB_WonderMesh_Popup(bpy.types.Operator):
#     bl_idname = "object.rmb_wondermesh_popup"
#     bl_label = "Wonder Mesh Primitives Popup"
#     bl_options = {'REGISTER', 'UNDO'}
#
#     @classmethod
#     def poll(cls, context):
#         return context.active_object is not None
#
#     def check(self, context):
#
#         return True
#
#     def execute(self, context):
#         return {'FINISHED'}
#
#
#     def draw(self, context):
#
#         bpy.types.DATA_PT_Wlayout.draw(self, context)
#
#     def invoke(self, context, event):
#         if bpy.app.version == (2, 78, 0):
#             dpi_value = bpy.context.preferences.system.dpi
#             return context.window_manager.invoke_props_dialog(self, width=dpi_value * 400, height=100)
#
#         elif bpy.app.version >= (2, 79, 0):
#             dpi_value = bpy.context.preferences.view.ui_scale
#             return context.window_manager.invoke_props_dialog(self, width=dpi_value * 400, height=100)


#RMB          
class WAZOU_RMB_PIE_MENUS_MT_menu(Menu):
    bl_idname = "WAZOU_RMB_PIE_MENUS_MT_menu"
    bl_label = "Wazou RMB Pie Menu"

    # @classmethod
    # def poll(cls, context):
    #     return cls.paint_settings(context)
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        wm = bpy.context.window_manager
        obj = context.active_object
        toolsettings = context.tool_settings
        self.use_modals = get_addon_preferences().use_modals
        self.scale_y = get_addon_preferences().scale_y

        
        
        ################################################
        # No Objects                                   #
        ################################################
        if bpy.context.area.type == 'VIEW_3D' and not bpy.context.object:
            
            #4 - LEFT
            pie.operator("wm.read_homefile", text="New", icon='FILE_NEW')
            #6 - RIGHT
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.scale_y= self.scale_y
            row.operator("wm.recover_last_session", text="Recover Last Session", icon='RECOVER_LAST')
            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.operator("wm.recover_auto_save", text="Recover auto Save")
            #2 - BOTTOM
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.scale_x=1
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='MESH_CUBE').primitive = "cube"
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='MESH_PLANE').primitive = "plan"
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='MESH_GRID').primitive = "grid"
            row.operator("wazou_rmb_pie_menus.primitives", text = "", icon = 'MATSPHERE').primitive = "sphere"
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='MESH_CYLINDER').primitive = "cylinder"
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='MESH_CONE').primitive = "cone"
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='MESH_TORUS').primitive = "torus"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MESH_CIRCLE').primitive = "mesh_circle"
            # row.operator("wazou_rmb_pie_menus.add_empty_image", text="", icon='IMAGE_DATA')
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='CURVE_BEZCURVE').primitive = "bezier"
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='CURVE_BEZCIRCLE').primitive = "circle"
            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.scale_x=1
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='VERTEXSEL').primitive = "vertex"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='OUTLINER_OB_EMPTY').primitive = "empty_axe"
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='IPO_EASE_IN_OUT').primitive = "curve_line"
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='FILE_FONT').primitive = "text"
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='OUTLINER_OB_ARMATURE').primitive = "armature"
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='OUTLINER_OB_CAMERA').primitive = "camera"
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='LIGHT_AREA').primitive = "area"
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='LIGHT_SUN').primitive = "sun"
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='LIGHT_SPOT').primitive = "spot"
            row.operator("wazou_rmb_pie_menus.primitives",text="", icon ='LIGHT_POINT').primitive = "point"

            # # Wonder Mesh
            # if hasattr(bpy.types, "OBJECT_MT_W_Primitives_menu")  :
            #     row = col.row(align=True)
            #     row.label(text="Wonder Mesh Primitives :")
            #     row.separator()
            #     row = col.row(align=True)
            #     row.scale_y = self.scale_y
            #     row.scale_x = 1.74
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_PLANE').primitive = "plane"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_CUBE').primitive = "box"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_CIRCLE').primitive = "ring"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MATSPHERE').primitive = "sphere"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_CYLINDER').primitive = "tube"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_CONE').primitive = "cone"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_CAPSULE').primitive = "capsule"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_TORUS').primitive = "torus"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MOD_SCREW').primitive = "screw"


            
            #Import Export
            row = col.row()
            row.label(text="Import/Export :")
            row = col.row(align=True)
            row.scale_y=self.scale_y
            if hasattr(bpy.types, "IMPORT_SCENE_OT_obj"): 
                row.operator("wazou_rmb_pie_menus.import_exports", text="OBJ", icon='IMPORT').import_exports = "obj"
                
            if hasattr(bpy.types, "IMPORT_SCENE_OT_fbx"):   
                row.operator("wazou_rmb_pie_menus.import_exports", text="FBX", icon='IMPORT').import_exports = "fbx"
            
            if hasattr(bpy.types, "IMPORT_MESH_OT_stl"): 
                row.operator("wazou_rmb_pie_menus.import_exports", text="STL", icon='IMPORT').import_exports = "stl"
            
            row.operator("wazou_rmb_pie_menus.import_exports", text="ALEMBIC", icon='IMPORT').import_exports = "abc"

            #8 - TOP
            pie.operator("wm.save_mainfile", text="Save", icon='FILE_TICK')
            
            #7 - TOP - LEFT 
            pie.operator("wm.open_mainfile", text="Open file", icon='FILE_FOLDER')
            
            #9 - TOP - RIGHT
            pie.operator("wm.save_as_mainfile", text="Save As...")
           
            #1 - BOTTOM - LEFT
            pie.separator()
            
            #3 - BOTTOM - RIGHT
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.scale_x=1.5
            row.operator("wm.link", text="Link", icon='LINK_BLEND')
            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.scale_x=1.5
            row.operator("wm.append", text="Append", icon='APPEND_BLEND')
        
        ################################################
        # Object Mode                                  #
        ################################################    
        elif bpy.context.area.type == 'VIEW_3D' and bpy.context.object.mode == 'OBJECT':
            
            #4 - LEFT
            selection = context.selected_objects
            if len(context.selected_objects) == 1:
                pie.operator("wazou_rmb_pie_menus.extract_duplicate", text="Separate", icon='FULLSCREEN_ENTER')
            else:
                pie.operator("wazou_rmb_pie_menus.extract_duplicate", text="Join", icon='FULLSCREEN_EXIT')
                
            #6 - RIGHT
            pie.operator("wazou_rmb_pie_menus.subsurf_operator", text="Subsurf", icon='MOD_SUBSURF')
                
            #2 - BOTTOM
            split = pie.split()
            col = split.column(align=True)
            # row = col.row(align=True)

            if hasattr(bpy.types, "view3d.speedflow_ui_menu"):
                row = col.row(align=True)
                row.label(text="Speedflow")
                row = col.row(align=True)
                row.scale_y = self.scale_y
                row.scale_x = 1.705
                row.operator("speedflow.bevel", text="", icon='MOD_BEVEL')
                row.operator("speedflow.boolean", text="", icon='MOD_BOOLEAN')
                row.operator("speedflow.solidify", text="", icon='MOD_SOLIDIFY')
                row.operator("speedflow.symetrize", text="", icon='MOD_WIREFRAME')
                row.operator("speedflow.mirror", text="", icon='MOD_MIRROR')
                row.operator("speedflow.array", text="", icon='MOD_ARRAY')
                row.operator("speedflow.subsurf", text="", icon='MOD_SUBSURF')
                row.operator("speedflow.rotate", text="", icon='MOD_THICKNESS')
                row.operator("speedflow.tubify", text="", icon='MOD_CURVE')

            row = col.row(align=True)
            row.separator()
            # row = col.row(align=True)
            # row.menu("INFO_MT_add", text="Primitives:", icon='OBJECT_DATAMODE')
            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.scale_x=1
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MESH_CUBE').primitive = "cube"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MESH_PLANE').primitive = "plan"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MESH_GRID').primitive = "grid"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MATSPHERE').primitive = "sphere"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MESH_CYLINDER').primitive = "cylinder"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MESH_CONE').primitive = "cone"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MESH_TORUS').primitive = "torus"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MESH_CIRCLE').primitive = "mesh_circle"
            # row.operator("wazou_rmb_pie_menus.add_empty_image", text="", icon='IMAGE_DATA')
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='CURVE_BEZCURVE').primitive = "bezier"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='CURVE_BEZCIRCLE').primitive = "circle"
            row = col.row(align=True)
            row.scale_y = self.scale_y
            row.scale_x = 1
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='VERTEXSEL').primitive = "vertex"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='OUTLINER_OB_EMPTY').primitive = "empty_axe"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='IPO_EASE_IN_OUT').primitive = "curve_line"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='FILE_FONT').primitive = "text"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='OUTLINER_OB_ARMATURE').primitive = "armature"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='OUTLINER_OB_CAMERA').primitive = "camera"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='LIGHT_AREA').primitive = "area"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='LIGHT_SUN').primitive = "sun"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='LIGHT_SPOT').primitive = "spot"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='LIGHT_POINT').primitive = "point"


            # # Wonder Mesh
            # if hasattr(bpy.types, "OBJECT_MT_W_Primitives_menu") :
            #     if obj.type == "MESH" :
            #         WType = obj.data.WType
            #     row = col.row(align=True)
            #     row.label(text="Wonder Mesh Primitives :")
            #     row.separator()
            #     row = col.row(align=True)
            #     row.scale_y = self.scale_y
            #     row.scale_x = 1.7
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_PLANE').primitive = "plane"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_CUBE').primitive = "box"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_CIRCLE').primitive = "ring"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MATSPHERE').primitive = "sphere"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_CYLINDER').primitive = "tube"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_CONE').primitive = "cone"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_CAPSULE').primitive = "capsule"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_TORUS').primitive = "torus"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MOD_SCREW').primitive = "screw"
            #     if obj.type == "MESH":
            #         if WType != 'NONE':
            #             row = col.row(align=True)
            #             row.scale_y = self.scale_y
            #             row.scale_x = 1.3
            #             row.operator("object.rmb_wondermesh_popup", text="Edit Primitive", icon='SCRIPTWIN')
            #             row.operator("object.rmb_apply_wonder_mesh", text="Convert", icon='FILE_TICK')

            #Import Export
            row = col.row()
            row.label(text="Import/Export :")
            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.scale_x = 1
            if hasattr(bpy.types, "IMPORT_SCENE_OT_obj"): 
                row.operator("wazou_rmb_pie_menus.import_exports", text="OBJ", icon='IMPORT').import_exports = "obj"
                
            if hasattr(bpy.types, "IMPORT_SCENE_OT_fbx"):   
                row.operator("wazou_rmb_pie_menus.import_exports", text="FBX", icon='IMPORT').import_exports = "fbx"
            
            if hasattr(bpy.types, "IMPORT_MESH_OT_stl"): 
                row.operator("wazou_rmb_pie_menus.import_exports", text="STL", icon='IMPORT').import_exports = "stl"
            
            row.operator("wazou_rmb_pie_menus.import_exports", text="ALEMBIC", icon='IMPORT').import_exports = "abc"

            #8 - TOP
            pie.separator()
            # pie.operator("screen.redo_last", text="F6", icon='SCRIPTWIN')
           
            #7 - TOP - LEFT 
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)   
            if hasattr(bpy.types, "OBJECT_OT_automirror"): 
                row.scale_y=self.scale_y
                row.operator("wazou_rmb_pie_menus.auto_mirror", icon = 'MOD_MIRROR')

                # row = col.row(align=True)
            else:
                if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' ]) == 1:
                    row.label(text="Automirror", icon='ERROR')

            if hasattr(bpy.types, "OBJECT_OT_smart_cursor_modal_operator"):
                row.operator("object.smart_cursor_modal_operator", text="", icon='CURSOR')

            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.operator_menu_enum("object.modifier_add", "type")
            row.operator("wazou_rmb_pie_menus.apply_remove_modifiers", text="", icon='FILE_TICK')
            row = col.row(align=True)  
            row.scale_y=self.scale_y
            row.operator("wazou_rmb_pie_menus.cursor", text="Cursor", icon='CURSOR')
            row.operator("wazou_rmb_pie_menus.origin", text="Origin", icon='OUTLINER_OB_EMPTY')
            
            #9 - TOP - RIGHT
            pie.operator("wazou_rmb_pie_menus.parent_objects", text="Parent/Unparent", icon='MOD_SUBSURF')
            
            #1 - BOTTOM - LEFT
            row=pie.row()
            row.scale_y=self.scale_y
            row.operator("wazou_rmb_pie_menus.apply_transforms", text="Apply Transforms", icon='EMPTY_ARROWS')

            #3 - BOTTOM - RIGHT
            row=pie.row()
            row.scale_y=self.scale_y
            row.operator("wazou_rmb_pie_menus.align_selection",text="Align to Grid", icon = 'OUTLINER_DATA_EMPTY')

            
        
        ################################################
        # Edit Mode                                    #
        ################################################    
        elif bpy.context.object.mode == 'EDIT':    
            
            #4 - LEFT
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.scale_y=self.scale_y
            if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if bpy.context.object.mode == "EDIT"]) == 1:
                if not self.use_modals: 
                    row.operator("wazou_rmb_pie_menus.subdivide_smooth", text="Subdivide",icon='OUTLINER_OB_LATTICE')
                else:
                    row.operator("object.rmb_modal_subdivide", text="Subdivide",icon='OUTLINER_OB_LATTICE') 
    
                     
            row.operator("wazou_rmb_pie_menus.shrink_fatten", text='Shrink/Fatten')
            
            row = col.row(align=True)
            row.scale_y=self.scale_y
            if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if bpy.context.object.mode == "EDIT"]) == 1:
                row.operator("wazou_rmb_pie_menus.smooth_relax", text="Smooth/Relax", icon='GRID')
            row.operator("wazou_rmb_pie_menus.spin", text="Spin", icon='MOD_THICKNESS')
            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.operator("wazou_rmb_pie_menus.knurl", text="Knurl", icon='MESH_GRID')
            # selection = bpy.context.selected_objects
            if len(context.selected_objects) == 1:
                row.operator("wazou_rmb_pie_menus.extract_duplicate", text="Separate/Extract", icon='FULLSCREEN_ENTER')
            else:
                row.operator("wazou_rmb_pie_menus.extract_duplicate", text="Join", icon='FULLSCREEN_EXIT')

            #6 - RIGHT
            is_subsurf1 = False
            for mode in context.object.modifiers :
                if mode.type == 'SUBSURF' :
                    is_subsurf1 = True
            if is_subsurf1 == True :
                pie.operator("wazou_rmb_pie_menus.subsurf_operator", text="Subsurf", icon='MOD_SUBSURF')
            else :
                pie.operator("wazou_rmb_pie_menus.subsurf_operator", text="Subsurf", icon='MOD_SUBSURF')

            #2 - BOTTOM
            split = pie.split()
            col = split.column(align=True)
            
            if obj.type == 'MESH':
                row = col.row(align=True)
                row.separator()
                row = col.row(align=True)
                row.separator()
                row = col.row(align=True)
                row.separator()
                row = col.row(align=True)
                row.scale_y=self.scale_y
                row.operator("wazou_rmb_pie_menus.smart_merge", text="Merge", icon='AUTOMERGE_ON')
                row.operator("wazou_rmb_pie_menus.smart_connect", text="Connect", icon='UV_VERTEXSEL')

            elif obj.type == 'CURVE':
                row = col.row(align=True)
                row.separator()
                row = col.row(align=True)
                row.separator()
                row = col.row(align=True)
                row.scale_y=self.scale_y
                row.operator("curve.subdivide", text="Subdivide",icon='OUTLINER_OB_LATTICE')
                row.operator("curve.smooth", text="Smooth", icon='GRID')
                row = col.row(align=True)
                row.scale_y=self.scale_y
                row.operator("curve.switch_direction", text="Switch direction", icon='FILE_REFRESH')
                row.operator("transform.vertex_random", text="Randomize", icon='STICKY_UVS_DISABLE')
            
            elif obj.type == 'ARMATURE': 
                row = col.row(align=True)
                row.separator()
                row = col.row(align=True)
                row.separator()
                row = col.row(align=True)
                row.scale_y=self.scale_y
                row.operator("armature.subdivide", text="Subdivide")

            if hasattr(bpy.types, "pie.speedflow_pie_menu"):
                row.scale_y = self.scale_y
                row.separator()
                row.scale_y = self.scale_y
                row = col.row(align=True)
                row.label(text="Speedflow")
                row = col.row(align=True)
                row.scale_x = 1.705
                row.operator("speedflow.bevel", text="", icon='MOD_BEVEL')
                row.operator("speedflow.boolean", text="", icon='MOD_BOOLEAN')
                row.operator("speedflow.solidify", text="", icon='MOD_SOLIDIFY')
                row.operator("speedflow.symetrize", text="", icon='MOD_WIREFRAME')
                row.operator("speedflow.mirror", text="", icon='MOD_MIRROR')
                row.operator("speedflow.array", text="", icon='MOD_ARRAY')
                row.operator("speedflow.subsurf", text="", icon='MOD_SUBSURF')
                row.operator("speedflow.rotate", text="", icon='MOD_THICKNESS')
                row.operator("speedflow.tubify", text="", icon='MOD_CURVE')
                row.scale_y = self.scale_y
                row.separator()
            # row = col.row(align=True)
            # row.menu("INFO_MT_add", text="Primitives:", icon='OBJECT_DATAMODE')
            # row.label(text="Primitives :")
            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.scale_x=1
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MESH_CUBE').primitive = "cube"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MESH_PLANE').primitive = "plan"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MESH_GRID').primitive = "grid"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MATSPHERE').primitive = "sphere"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MESH_CYLINDER').primitive = "cylinder"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MESH_CONE').primitive = "cone"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MESH_TORUS').primitive = "torus"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='MESH_CIRCLE').primitive = "mesh_circle"
            # row.operator("wazou_rmb_pie_menus.add_empty_image", text="", icon='IMAGE_DATA')
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='CURVE_BEZCURVE').primitive = "bezier"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='CURVE_BEZCIRCLE').primitive = "circle"
            row = col.row(align=True)
            row.scale_y = self.scale_y
            row.scale_x = 1
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='VERTEXSEL').primitive = "vertex"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='OUTLINER_OB_EMPTY').primitive = "empty_axe"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='IPO_EASE_IN_OUT').primitive = "curve_line"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='FILE_FONT').primitive = "text"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='OUTLINER_OB_ARMATURE').primitive = "armature"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='OUTLINER_OB_CAMERA').primitive = "camera"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='LIGHT_AREA').primitive = "area"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='LIGHT_SUN').primitive = "sun"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='LIGHT_SPOT').primitive = "spot"
            row.operator("wazou_rmb_pie_menus.primitives", text="", icon='LIGHT_POINT').primitive = "point"

            # # Wonder Mesh
            # if hasattr(bpy.types, "OBJECT_MT_W_Primitives_menu"):
            #     if obj.type == "MESH" :
            #         WType = obj.data.WType
            #     row = col.row(align=True)
            #     row.label(text="Wonder Mesh Primitives :")
            #     row.separator()
            #     row = col.row(align=True)
            #     row.scale_y = self.scale_y
            #     row.scale_x = 1.74
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_PLANE').primitive = "plane"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_CUBE').primitive = "box"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_CIRCLE').primitive = "ring"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MATSPHERE').primitive = "sphere"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_CYLINDER').primitive = "tube"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_CONE').primitive = "cone"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_CAPSULE').primitive = "capsule"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MESH_TORUS').primitive = "torus"
            #     row.operator("object.rmb_wonder_mesh_primitives", text="", icon='MOD_SCREW').primitive = "screw"
            #     if obj.type == "MESH":
            #         if WType != 'NONE':
            #             # row.operator("object.rmb_wondermesh_popup", text="", icon='SCRIPTWIN')
            #             row.operator("object.rmb_apply_wonder_mesh", text="", icon='FILE_TICK')


            #8 - TOP
            pie.separator()
            # pie.operator("screen.redo_last", text="F6", icon='SCRIPTWIN')
            #7 - TOP - LEFT 
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)   
            if hasattr(bpy.types, "OBJECT_OT_automirror"): 
                row.scale_y=self.scale_y
#                if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' ]) == 1:
                row.operator("wazou_rmb_pie_menus.auto_mirror", icon = 'MOD_MIRROR')

#                else:
#                    row.operator("object.smart_cursor_modal_operator", text="Smart Cursor", icon='CURSOR')      
#                 row = col.row(align=True)
            else:
                if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' ]) == 1:
                    row.label(text="Automirror", icon='ERROR')
            if hasattr(bpy.types, "OBJECT_OT_smart_cursor_modal_operator"):
                row.operator("object.smart_cursor_modal_operator", text="", icon='CURSOR')

            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.operator_menu_enum("object.modifier_add", "type")
            row.operator("wazou_rmb_pie_menus.apply_remove_modifiers", text="", icon='FILE_TICK')
            row = col.row(align=True)  
            row.scale_y=self.scale_y
            row.operator("wazou_rmb_pie_menus.cursor", text="Cursor", icon='CURSOR')
            row.operator("wazou_rmb_pie_menus.origin", text="Origin", icon='OUTLINER_OB_EMPTY')
            row.operator("wazou_rmb_pie_menus.rmb_copy_custom_orientation", text="Orient", icon='OUTLINER_OB_EMPTY')

            #9 - TOP - RIGHT
            box = pie.split().column()
            row = box.split(factor=0.6)
            row.scale_y=self.scale_y
            if hasattr(bpy.types, "MESH_OT_offset_edges"):
                row.operator("wazou_rmb_pie_menus.offset_edges", text="Offset Edges", icon='UV_EDGESEL')
            else:
                row.label(text="Offset Edges", icon='ERROR')

            if hasattr(bpy.types, "MESH_OT_looptools_bridge"):
                row.menu(WAZOU_RMB_PIE_MENUS_MT_Looptools_Menu.bl_idname)
            else:
                row.label(text="Looptools", icon='ERROR')
                
            split = box.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.operator("wazou_rmb_pie_menus.bridge", text="Bridge", icon='SNAP_INCREMENT')
            # row.operator("wazou_rmb_pie_menus.edges_loopslide", text='Edge Loopslide')
            row.operator("mesh.fill_grid", text="Grid Fill", icon='UV_FACESEL')
            
            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.operator("wazou_rmb_pie_menus.inset_poke_faces", text="Inset/Poke", icon='FACESEL')
            row.operator("wazou_rmb_pie_menus.smart_loops", text="Loopcut", icon='UV_EDGESEL')
            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.operator("wazou_rmb_pie_menus.mark_clear_seam", text="Seam", icon='UV_EDGESEL')
            row.operator("wazou_rmb_pie_menus.unwrap", text="Unwrap", icon='MOD_UVPROJECT')
            
            
            #1 - BOTTOM - LEFT
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.operator("wazou_rmb_pie_menus.circle",text="Simplify", icon='MESH_CIRCLE')
            if hasattr(bpy.types, "MESH_OT_looptools_bridge"):
                row.operator("wazou_rmb_pie_menus.create_hole",text="circle", icon='CLIPUV_DEHLT')
            else:
                row.label(text="Looptools", icon='ERROR')
            row.operator("wazou_rmb_pie_menus.knife_tools", text="Knife", icon='SCULPTMODE_HLT')


            row = col.row(align=True)
            row.scale_y=self.scale_y
            if hasattr(bpy.types, "MESH_OT_vertex_align"):
                row.operator("wazou_rmb_pie_menus.align_space", text="Space/Align", icon='VIEW_ORTHO')
            else:
                row.label(text="Vertex Tools / Looptoos", icon='ERROR')

            if hasattr(bpy.types, "MO_OT_edge_equalize_active"):
                row.operator("wazou_rmb_pie_menus.equalize_edges_length", text="Equalize Edges", icon='UV_EDGESEL')
            else:
                row.label(text="Set equal edge lengths", icon='ERROR')


            #3 - BOTTOM - RIGHT
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.operator("wazou_rmb_pie_menus.align_selection",text="Align", icon = 'OUTLINER_DATA_EMPTY')
            
            row = col.row(align=True)
            row.scale_y=self.scale_y
            row.operator("mesh.remove_doubles", text="Doubles  ", icon='X')
            # row.operator("object.rmb_remove_double", text="Doubles  ",icon='X')
            row.operator("wazou_rmb_pie_menus.normals",text="Normals", icon = 'FACESEL')
            row = col.row(align=True)
            row.scale_y=self.scale_y
            if obj.type =='MESH':
                row.prop(toolsettings, "use_mesh_automerge", text="Automerge")
                mesh = obj.data
                row.prop(mesh, "use_mirror_x", text="Mirror X")

            # userpref = bpy.context.preferences
            # edit = userpref.edit
            # row = col.row(align=True)
            # row.prop(bpy.context.preferences.edit, "use_drag_immediately", text="Release Confirm")


                 
        ################################################
        # Sculpt                                       #
        ################################################    
        elif bpy.context.area.type == 'VIEW_3D' and bpy.context.object.mode == 'SCULPT':


            
            #------Dyntopo

            if context.sculpt_object.use_dynamic_topology_sculpting:
                #4 - LEFT
                pie.operator("sculpt.dynamic_topology_toggle", icon='X', text="Disable Dyntopo")
                #6 - RIGHT
                col = pie.column(align=True)
                row = col.row(align=True)
                row.operator("sculpt.optimize", text="Optimize   ")
                row.operator("sculpt.detail_flood_fill", text="Detail flood Fill")
                row = col.row(align=True)
                if bpy.context.scene.tool_settings.sculpt.use_smooth_shading == True:
                    row.operator("object.dtpsmoothshading", text="flat Shading", icon='MESH_ICOSPHERE')
                else:
                    row.operator("object.dtpsmoothshading", text="Smooth Shading", icon='SOLID')
                row.operator("object.smooth_sculpt", text="Smooth Mesh", icon='MOD_SMOOTH')

                # pie.separator()
                
                #2 - BOTTOM
                Sculpt_Bottom(self, context)

                #8 - TOP
                Sculpt_Top(self, context)
                
                #7 - TOP - LEFT
                toolsettings = context.tool_settings
                sculpt_relative = toolsettings.sculpt
                sculpt = context.tool_settings.sculpt
                if bpy.context.tool_settings.sculpt.detail_type_method == 'CONSTANT':
                    
                    col = pie.column(align=True)
                    row= col.row(align=True)
                    row.prop(sculpt, "constant_detail_resolution")
                    row.operator("sculpt.sample_detail_size", text="", icon='EYEDROPPER')
                    col.prop(sculpt, "detail_refine_method", text="")
                    col.prop(sculpt, "detail_type_method", text="")
                    
                elif bpy.context.tool_settings.sculpt.detail_type_method == 'RELATIVE':
                    col = pie.column(align=True)     
                    col.prop(sculpt_relative, "detail_size")
                    col.prop(sculpt, "detail_refine_method", text="")
                    col.prop(sculpt, "detail_type_method", text="")
                else:
                    col = pie.column(align=True) 
                    col.prop(sculpt, "detail_percent")   
                    col.prop(sculpt, "detail_refine_method", text="")
                    col.prop(sculpt, "detail_type_method", text="") 

                #9 - TOP - RIGHT
                # Sculpt_Brush_Preview(self, context)
                Sculpt_Curve_Stroke(self, context)

                
                #1 - BOTTOM - LEFT
                Sculpt_Symmetry(self, context)

                #3 - BOTTOM - RIGHT
                Sculpt_Brush_Preview(self, context)



            #------Normal Sculpt
                 
            else:
                #4 - LEFT
                pie.operator("enable.dyntopo", text="Enable Dyntopo", icon='LINE_DATA')
                #6 - RIGHT
                pie.operator("wazou_rmb_pie_menus.subsurf_operator", text="Subsurf", icon='MOD_SUBSURF')

                #2 - BOTTOM
                Sculpt_Bottom(self, context)

              
                #8 - TOP
                Sculpt_Top(self, context)
                
                #7 - TOP - LEFT
                pie.separator()
             
                #9 - TOP - RIGHT
                # Sculpt_Brush_Preview(self, context)
                Sculpt_Curve_Stroke(self, context)

                #1 - BOTTOM - LEFT
                Sculpt_Symmetry(self, context)


                #3 - BOTTOM - RIGHT
                Sculpt_Brush_Preview(self, context)


        ################################################
        # Particles                                    #
        ################################################
        elif bpy.context.area.type == 'VIEW_3D' and bpy.context.object.mode == 'PARTICLE_EDIT':
            # 4 - LEFT
            pie.operator("wazou_rmb_pie_menus.selection_particles_brushes", text="Smooth", icon='BRUSH_DATA').variable = 'SMOOTH'
            # 6 - RIGHT
            pie.operator("wazou_rmb_pie_menus.selection_particles_brushes", text="Length", icon='BRUSH_DATA').variable = 'LENGTH'
            # 2 - BOTTOM
            pie.operator("wazou_rmb_pie_menus.selection_particles_brushes", text="Puff", icon='BRUSH_DATA').variable = 'PUFF'
            # 8 - TOP
            pie.operator("wazou_rmb_pie_menus.selection_particles_brushes", text="Comb", icon='BRUSH_DATA').variable = 'COMB'
            # 7 - TOP - LEFT
            pie.operator("wazou_rmb_pie_menus.selection_particles_brushes", text="Add", icon='BRUSH_DATA').variable = 'ADD'
            # 9 - TOP - RIGHT
            pie.operator("wazou_rmb_pie_menus.selection_particles_brushes", text="Cut", icon='BRUSH_DATA').variable = 'CUT'
            # 1 - BOTTOM - LEFT
            pie.operator("wazou_rmb_pie_menus.selection_particles_brushes", text="None", icon='BRUSH_DATA').variable = 'NONE'
            # 3 - BOTTOM - RIGHT
            pie.operator("wazou_rmb_pie_menus.selection_particles_brushes", text="Weight", icon='BRUSH_DATA').variable = 'WEIGHT'

        bpy.context.area.tag_redraw()


# #Pie Sculpt Mirror
# class PieSculptMirror(Menu):
#     bl_idname = "pie.sculptmirror"
#     bl_label = "Pie Sculpt Mirror"
#
#     def draw(self, context):
#         layout = self.layout
#         pie = layout.menu_pie()
#         sculpt = context.tool_settings.sculpt
#         #4 - LEFT
#         pie.operator("sculpt.symmetrizemoinsx", text="-X to +X", icon='TRIA_RIGHT')
#         #6 - RIGHT
#         pie.operator("sculpt.symmetrizeplusx", text="+X to -X", icon='TRIA_LEFT')
#         #2 - BOTTOM
#         if bpy.context.scene.tool_settings.sculpt.use_symmetry_y == (True):
#             pie.operator("sculpt.sculptusesymmetryy", text="Unlock Y", icon='LOCKED')
#         else:
#             pie.operator("sculpt.sculptusesymmetryy", text="Lock Y", icon='UNLOCKED')
#         #8 - TOP
#         pie.operator("object.symetrylocky", text="Symmetrize Y", icon='MOD_MIRROR')
#         #7 - TOP - LEFT
#         pie.operator("object.symetrylockx", text="Symmetrize X", icon='MOD_MIRROR')
#         #9 - TOP - RIGHT
#         pie.operator("object.symetrylockz", text="Symmetrize Z", icon='MOD_MIRROR')
#         #1 - BOTTOM - LEFT
#         if bpy.context.scene.tool_settings.sculpt.use_symmetry_x == (True):
#             pie.operator("sculpt.sculptusesymmetryx", text="Unlock X", icon='LOCKED')
#         else:
#             pie.operator("sculpt.sculptusesymmetryx", text="Lock X", icon='UNLOCKED')
#         #3 - BOTTOM - RIGHT
#         if bpy.context.scene.tool_settings.sculpt.use_symmetry_z == (True):
#             pie.operator("sculpt.sculptusesymmetryz", text="Unlock Z", icon='LOCKED')
#         else:
#             pie.operator("sculpt.sculptusesymmetryz", text="Lock Z", icon='UNLOCKED')

################################################
# Particles                                    #
################################################
class WAZOU_RMB_PIE_MENUS_MT_particles_brushes(Menu):
    bl_idname = "WAZOU_RMB_PIE_MENUS_MT_particles_brushes"
    bl_label = "RMB Pie Menu"

    @classmethod
    def poll(cls, context):
        if bpy.context.area.type == 'VIEW_3D' and bpy.context.object.mode == 'PARTICLE_EDIT':
            return True

    def draw(self, context):
        layout = self.layout

        # if bpy.context.area.type == 'VIEW_3D' and bpy.context.object.mode == 'PARTICLE_EDIT':
        pie = layout.menu_pie()
        # 4 - LEFT
        pie.operator("wazou_rmb_pie_menus.selection_particles_brushes", text="Smooth", icon='BRUSH_DATA').variable = 'SMOOTH'
        # 6 - RIGHT
        pie.operator("wazou_rmb_pie_menus.selection_particles_brushes", text="Length", icon='BRUSH_DATA').variable = 'LENGTH'
        # 2 - BOTTOM
        pie.operator("wazou_rmb_pie_menus.selection_particles_brushes", text="Puff", icon='BRUSH_DATA').variable = 'PUFF'
        # 8 - TOP
        pie.operator("wazou_rmb_pie_menus.selection_particles_brushes", text="Comb", icon='BRUSH_DATA').variable = 'COMB'
        # 7 - TOP - LEFT
        pie.operator("wazou_rmb_pie_menus.selection_particles_brushes", text="Add", icon='BRUSH_DATA').variable = 'ADD'
        # 9 - TOP - RIGHT
        pie.operator("wazou_rmb_pie_menus.selection_particles_brushes", text="Cut", icon='BRUSH_DATA').variable = 'CUT'
        # 1 - BOTTOM - LEFT
        pie.operator("wazou_rmb_pie_menus.selection_particles_brushes", text="None", icon='BRUSH_DATA').variable = 'NONE'
        # 3 - BOTTOM - RIGHT
        pie.operator("wazou_rmb_pie_menus.selection_particles_brushes", text="Weight", icon='BRUSH_DATA').variable = 'WEIGHT'


#Pie Particle Brushes
class WAZOU_RMB_PIE_MENUS_MT_particle_brushes(Menu):
    bl_idname = "WAZOU_RMB_PIE_MENUS_MT_particle_brushes"
    bl_label = "Pie Particle Parameters"

    @classmethod
    def poll(cls, context):
        if bpy.context.area.type == 'VIEW_3D' and bpy.context.object.mode == 'PARTICLE_EDIT':
            return True

    def draw(self, context):
        layout = self.layout

        # if bpy.context.area.type == 'VIEW_3D' and bpy.context.object.mode == 'PARTICLE_EDIT':
        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("wazou_rmb_pie_menus.selection_particles_mode", text="Path", icon='PARTICLE_PATH').variable = 'PATH'
        #6 - RIGHT
        pie.operator("wazou_rmb_pie_menus.selection_particles_mode", text="Point", icon='PARTICLE_POINT').variable = 'POINT'
        #2 - BOTTOM
        pie.operator("wazou_rmb_pie_menus.selection_particles_mode", text="Tip", icon='PARTICLE_TIP').variable = 'TIP'
        #8 - TOP
        pie.operator("wm.call_menu_pie", text="Brushes", icon='BRUSH_DATA').name = "pie.pie_particles_brushes"
        # pie.menu("pie.pie_particles_brushes", text="Brushes", icon='BRUSH_DATA')
        #7 - TOP - LEFT
        pie.operator("wm.call_menu_pie", text="Options", icon='SCRIPTWIN').name="pie.particleoptions"
        #9 - TOP - RIGHT
        if bpy.context.scene.tool_settings.particle_edit.show_particles == (True):
            pie.operator("wazou_rmb_pie_menus.particle_children", text="Chidren OFF", icon='HAIR')
        else:
            pie.operator("wazou_rmb_pie_menus.particle_children", text="Chidren ON", icon='HAIR')
        #1 - BOTTOM - LEFT
        if bpy.context.scene.tool_settings.particle_edit.use_default_interpolate == (True):
            pie.operator("wazou_rmb_pie_menus.particle_interpolate", text="Interpolate OFF", icon='HAIR')
        else:
            pie.operator("wazou_rmb_pie_menus.particle_interpolate", text="Interpolate ON", icon='HAIR')
        #3 - BOTTOM - RIGHT
        if bpy.context.space_data.use_occlude_geometry == (True):
            pie.operator("wm.context_toggle", text="Occlude Geo ON", icon="ORTHO").data_path = "space_data.use_occlude_geometry"
        else:
            pie.operator("wm.context_toggle", text="Occlude Geo OFF", icon="ORTHO").data_path = "space_data.use_occlude_geometry"


#Pie Particle Options
class WAZOU_RMB_PIE_MENUS_MT_particle_options(Menu):
    bl_idname = "WAZOU_RMB_PIE_MENUS_MT_particle_options"
    bl_label = "Pie Particle Options"

    @classmethod
    def poll(cls, context):
        if bpy.context.area.type == 'VIEW_3D' and bpy.context.object.mode == 'PARTICLE_EDIT':
            return True

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        #4 - LEFT
        pie.operator("object.particlepathsteps", text="Path Steps = 6", icon='PARTICLE_POINT').variable = 6
        #6 - RIGHT
        pie.operator("object.particlepathsteps", text="Path Steps = 2", icon='PARTICLE_POINT').variable = 2
        #2 - BOTTOM
        pie.operator("object.particlepathsteps", text="Path Steps = 4", icon='PARTICLE_POINT').variable = 4
        #8 - TOP
        if bpy.context.scene.tool_settings.particle_edit.use_preserve_length == (True):
            pie.operator("wazou_rmb_pie_menus.particle_length", text="Keep Lengths OFF", icon='RNDCURVE')
        else :
            pie.operator("wazou_rmb_pie_menus.particle_length", text="Keep Lengths ON", icon='RNDCURVE')
        #7 - TOP - LEFT
        if bpy.context.object.data.use_mirror_x == (True):
            pie.operator("wazou_rmb_pie_menus.particle_x_mirror", text="X Mirror OFF", icon='MOD_MIRROR')
        else :
            pie.operator("wazou_rmb_pie_menus.particle_x_mirror", text="X Mirror ON", icon='MOD_MIRROR')
        #9 - TOP - RIGHT
        if bpy.context.scene.tool_settings.particle_edit.use_preserve_root == (True):
            pie.operator("wazou_rmb_pie_menus.particle_root", text="Keep Root OFF", icon='LAYER_ACTIVE')
        else :
            pie.operator("wazou_rmb_pie_menus.particle_root", text="Keep Root ON", icon='LAYER_ACTIVE')
        #1 - BOTTOM - LEFT
        pie.operator("object.particlepathsteps", text="Path Steps = 5", icon='PARTICLE_POINT').variable = 5
        #3 - BOTTOM - RIGHT
        pie.operator("object.particlepathsteps", text="Path Steps = 3", icon='PARTICLE_POINT').variable = 3

CLASSES =  [WAZOU_RMB_PIE_MENUS_MT_Looptools_Menu,
            WAZOU_RMB_PIE_MENUS_curve_popup,
            WAZOU_RMB_PIE_MENUS_MT_menu,
            WAZOU_RMB_PIE_MENUS_MT_particles_brushes,
            WAZOU_RMB_PIE_MENUS_MT_particle_brushes,
            WAZOU_RMB_PIE_MENUS_MT_particle_options,]

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