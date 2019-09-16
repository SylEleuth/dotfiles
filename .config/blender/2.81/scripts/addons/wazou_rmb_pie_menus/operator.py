import bpy
import os
import bmesh
from bpy.types import Menu, Operator
from bpy.props import PointerProperty, StringProperty, BoolProperty, \
    EnumProperty, IntProperty, FloatProperty, FloatVectorProperty, \
    CollectionProperty, BoolVectorProperty
from bpy.types import Curve, SurfaceCurve, TextCurve
from bpy.types import Operator, Macro
import bgl
from mathutils import *
import math
from .functions import *



# class WAZOU_RMB_PIE_MENUS_OT_import_image_as_brush(bpy.types.Operator):
#     bl_idname = "wazou_rmb_pie_menus.import_image_as_brush"
#     bl_label = "Import Image as Brush"
#     bl_options = {"REGISTER"}
#
#     filepath : bpy.props.StringProperty(subtype="FILE_PATH")
#
#     filter_glob : StringProperty(
#         default=".exr;*.jpg;*.jpeg;*.png;*.tif",
#         options={'HIDDEN'},
#     )
#
#     def execute(self, context):
#         print(self.filepath)
#         new_image = bpy.data.images.load(self.filepath, check_existing=True)
#         tex = bpy.data.textures.new(new_image.name, 'IMAGE')
#         tex.image = new_image
#
#         context.tool_settings.sculpt.brush.texture = tex
#         context.tool_settings.sculpt.brush.texture.image = new_image
#
#
#
#         return {"FINISHED"}
#
#     def invoke(self, context, event):
#
#         context.window_manager.fileselect_add(self)
#         return {'RUNNING_MODAL'}


# --------------------------------------------------------------------------
# Particles
# --------------------------------------------------------------------------

# Particle Path Steps
class WAZOU_RMB_PIE_MENUS_OT_particle_path_steps(bpy.types.Operator):
    bl_idname = "wazou_rmb_pie_menus.particle_path_steps"
    bl_label = "Particle Path Steps"
    bl_options = {'REGISTER', 'UNDO'}
    variable : bpy.props.IntProperty()

    def execute(self, context):
        context.scene.tool_settings.particle_edit.draw_step = self.variable
        return {'FINISHED'}

    # Particle Childrens


class WAZOU_RMB_PIE_MENUS_OT_particle_childrens(bpy.types.Operator):
    bl_idname = "wazou_rmb_pie_menus.particle_children"
    bl_label = "Particle Childrens"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.scene.tool_settings.particle_edit.show_particles == True:
            context.scene.tool_settings.particle_edit.show_particles = False
            context.area.type = 'VIEW_3D'
        elif context.scene.tool_settings.particle_edit.show_particles == False:
            context.scene.tool_settings.particle_edit.show_particles = True
            context.area.type = 'VIEW_3D'
        return {'FINISHED'}

    # Particle Length


class WAZOU_RMB_PIE_MENUS_OT_particle_length(bpy.types.Operator):
    bl_idname = "wazou_rmb_pie_menus.particle_length"
    bl_label = "Particle Length"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.scene.tool_settings.particle_edit.use_preserve_length == True:
            context.scene.tool_settings.particle_edit.use_preserve_length = False
            context.area.type = 'VIEW_3D'
        elif context.scene.tool_settings.particle_edit.use_preserve_length == False:
            context.scene.tool_settings.particle_edit.use_preserve_length = True
            context.area.type = 'VIEW_3D'
        return {'FINISHED'}

    # Particle X Mirror


class WAZOU_RMB_PIE_MENUS_OT_particle_x_mirror(bpy.types.Operator):
    bl_idname = "wazou_rmb_pie_menus.particle_x_mirror"
    bl_label = "Particle X Mirror"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.object.data.use_mirror_x == True:
            context.object.data.use_mirror_x = False
            context.area.type = 'VIEW_3D'
        elif context.object.data.use_mirror_x == False:
            context.object.data.use_mirror_x = True
            context.area.type = 'VIEW_3D'
        return {'FINISHED'}

    # Particle Root


class WAZOU_RMB_PIE_MENUS_OT_particle_root(bpy.types.Operator):
    bl_idname = "wazou_rmb_pie_menus.particle_root"
    bl_label = "Particle Root"
    bl_options : {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.scene.tool_settings.particle_edit.use_preserve_root == True:
            context.scene.tool_settings.particle_edit.use_preserve_root = False
            context.area.type = 'VIEW_3D'
        elif context.scene.tool_settings.particle_edit.use_preserve_root == False:
            context.scene.tool_settings.particle_edit.use_preserve_root = True
            context.area.type = 'VIEW_3D'
        return {'FINISHED'}

    # Selection Particles Mode


class WAZOU_RMB_PIE_MENUS_OT_selection_particles_mode(bpy.types.Operator):
    bl_idname = "wazou_rmb_pie_menus.selection_particles_mode"
    bl_label = "Selection Particles Mode"
    bl_options = {'REGISTER', 'UNDO'}
    variable : bpy.props.StringProperty()

    def execute(self, context):
        context.scene.tool_settings.particle_edit.select_mode = self.variable
        return {'FINISHED'}

    # Selection Particles Brushes


class WAZOU_RMB_PIE_MENUS_OT_selection_particles_brushes(bpy.types.Operator):
    bl_idname = "wazou_rmb_pie_menus.selection_particles_brushes"
    bl_label = "Selection Particles Brushes"
    bl_options = {'REGISTER', 'UNDO'}
    variable : bpy.props.StringProperty()

    def execute(self, context):
        context.scene.tool_settings.particle_edit.tool = self.variable
        context.area.type = 'VIEW_3D'
        return {'FINISHED'}

    # Particles Interpolate


class WAZOU_RMB_PIE_MENUS_OT_particles_interpolate(bpy.types.Operator):
    bl_idname = "wazou_rmb_pie_menus.particle_interpolate"
    bl_label = "Particles Interpolate"
    bl_options = {'REGISTER', 'UNDO'}
    variable : bpy.props.IntProperty()

    def execute(self, context):
        if context.scene.tool_settings.particle_edit.use_default_interpolate == True:
            context.scene.tool_settings.particle_edit.use_default_interpolate = False
            context.area.type = 'VIEW_3D'
        elif context.scene.tool_settings.particle_edit.use_default_interpolate == False:
            context.scene.tool_settings.particle_edit.use_default_interpolate = True
            context.area.type = 'VIEW_3D'
        return {'FINISHED'}

#RMB Copy custom Orientation
class WAZOU_RMB_PIE_MENUS_OT_copy_custom_orientation(bpy.types.Operator):
    """    COPY CUSTOM ORIENTATION

    CLICK - Copy Orientation, Pivot on selection
    SHIFT - Copy Orientation, Pivot at center
    CTRL  - Clear Rotation
    ALT    - Clear Location
    """
    bl_idname = 'wazou_rmb_pie_menus.rmb_copy_custom_orientation'
    bl_label = ""
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):

        obj = context.active_object
        if obj.mode == 'EDIT':
            me = obj.data
            bm = bmesh.from_edit_mesh(me)
            if [v for v in bm.verts if v.select] or [e for e in bm.edges if e.select] or [f for f in bm.faces if f.select]:
                return True

        return False

    def invoke(self, context, event):
        saved_location_0 = context.scene.cursor.location.copy()
        act_obj = context.active_object
        copy_modifiers = False

        for obj in context.selected_objects:
            if obj.modifiers:
                copy_modifiers = True


        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.view3d.viewnumpad(type='TOP',align_active=True)
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='VIEW')

        plane_obj = context.active_object

        act_obj.select_set(state=True)

        if copy_modifiers:
            context.view_layer.objects.active =  act_obj
            bpy.ops.object.make_links_data(type='MODIFIERS')
            context.view_layer.objects.active =  plane_obj

        bpy.ops.object.join()
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.delete(type='FACE')
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.view3d.view_persportho()
        bpy.ops.view3d.viewnumpad(type='FRONT', align_active=False)



        if event.ctrl:
            bpy.ops.object.rotation_clear(clear_delta=False)
            bpy.ops.transform.rotate(value=3.14159, axis=(1, 0, 0), constraint_axis=(True, False, False),
                                     constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED',
                                     proportional_edit_falloff='SMOOTH', proportional_size=1)

            saved_location = context.scene.cursor.location.copy()
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            context.scene.cursor.location = saved_location
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

            if event.shift:
                bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')

            if event.alt:
                bpy.ops.object.location_clear(clear_delta=False)

        elif event.shift:
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')

        elif event.alt:
            bpy.ops.object.location_clear(clear_delta=False)

        context.scene.cursor.location = saved_location_0
        return {'FINISHED'}

#RMB Looptools Circle
class WAZOU_RMB_PIE_MENUS_OT_looptools_circle(bpy.types.Operator):
    """    LOOPTOOLS CIRCLE

    CLICK - Circle Regular
    SHIFT - Circle not Regular
    CTRL  - Inside
    """
    bl_idname = 'wazou_rmb_pie_menus.looptools_circle'
    bl_label = "Looptools Circle"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return True


    def invoke(self, context, event):


        if event.shift:
            bpy.ops.mesh.looptools_circle(True, custom_radius=False, fit='best', flatten=True, influence=100, lock_x=False,

                                      lock_y=False, lock_z=False, radius=1, regular=False)
        elif event.ctrl:
            bpy.ops.mesh.looptools_circle(True, custom_radius=False, fit='inside', flatten=True, influence=100, lock_x=False,
                                          lock_y=False, lock_z=False, radius=1, regular=True)

        else:
            bpy.ops.mesh.looptools_circle(True, custom_radius=False, fit='best', flatten=True, influence=100, lock_x=False,
                                          lock_y=False, lock_z=False, radius=1, regular=True)

        return {'FINISHED'}

# RMB Looptools Flatten
class WAZOU_RMB_PIE_MENUS_OT_looptools_flatten(bpy.types.Operator):
    """    LOOPTOOLS FLATTEN

    CLICK - Best Fit
    SHIFT - View
    CTRL  - Normal
    """
    bl_idname = 'wazou_rmb_pie_menus.looptools_flatten'
    bl_label = "Looptools Flatten"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return True

    def invoke(self, context, event):

        if event.shift:
            bpy.ops.mesh.looptools_flatten(True, influence=100, lock_x=False, lock_y=False, lock_z=False, plane='view', restriction='none')

        elif event.ctrl:
            bpy.ops.mesh.looptools_flatten(True, influence=100, lock_x=False, lock_y=False, lock_z=False, plane='normal', restriction='none')

        else:
            bpy.ops.mesh.looptools_flatten(True, influence=100, lock_x=False, lock_y=False, lock_z=False, plane='best_fit', restriction='none')

        return {'FINISHED'}

# RMB Looptools Relax
class WAZOU_RMB_PIE_MENUS_OT_looptools_relax(bpy.types.Operator):
    """    LOOPTOOLS RELAX

    CLICK - LapRelax
    SHIFT - Looptools Relax
    CTRL  - LapRelax x5
    ALT    - Looptools Relax x5
    """
    bl_idname = 'wazou_rmb_pie_menus.looptools_relax'
    bl_label = "Looptools Relax"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return True

    def invoke(self, context, event):

        if event.shift:
            bpy.ops.mesh.looptools_relax(True, input='selected', interpolation='linear', iterations='1', regular=True)

        elif event.ctrl:
            bpy.ops.object.rmb_lap_relax()
            bpy.ops.object.rmb_lap_relax()
            bpy.ops.object.rmb_lap_relax()
            bpy.ops.object.rmb_lap_relax()
            bpy.ops.object.rmb_lap_relax()

        elif event.alt:
            bpy.ops.mesh.looptools_relax(True, input='selected', interpolation='linear', iterations='5', regular=True)

        else:
            bpy.ops.object.rmb_lap_relax()

        return {'FINISHED'}

# RMB Looptools Bridge
class WAZOU_RMB_PIE_MENUS_OT_looptools_bridge(bpy.types.Operator):
    """    LOOPTOOLS BRIDGE/LOFT

    CLICK - 1 Segment Linear
    SHIFT - 2 Segments Cubic
    CTRL  - Parallel (All)
    ALT    - Cubic x5
    """
    bl_idname = 'wazou_rmb_pie_menus.looptools_bridge'
    bl_label = "Looptools Bridge"
    bl_options = {'REGISTER'}


    def invoke(self, context, event):

        if event.shift:
            bpy.ops.mesh.looptools_bridge(True, cubic_strength=0, interpolation='cubic', loft=False, loft_loop=False,
                                          min_width=0, mode='shortest', remove_faces=True, reverse=False, segments=2,
                                          twist=0)

        elif event.ctrl:
            bpy.ops.mesh.looptools_bridge(True, cubic_strength=0, interpolation='cubic', loft=False, loft_loop=False,
                                          min_width=0, mode='shortest', remove_faces=True, reverse=False, segments=4,
                                          twist=0)

        else:
            bpy.ops.mesh.looptools_bridge(True, cubic_strength=0, interpolation='linear', loft=False, loft_loop=False,
                                          min_width=0, mode='shortest', remove_faces=True, reverse=False, segments=1,
                                          twist=0)

        return {'FINISHED'}

# RMB Looptools Space
class WAZOU_RMB_PIE_MENUS_OT_looptools_space(bpy.types.Operator):
    """    LOOPTOOLS SPACE

    CLICK - Cubic
    SHIFT - Linear
    CTRL  - Parrallel (All)
    """
    bl_idname = 'wazou_rmb_pie_menus.looptools_bridge.looptools_space'
    bl_label = "Looptools Space"
    bl_options = {'REGISTER'}


    def invoke(self, context, event):

        if event.shift:
            bpy.ops.mesh.looptools_space(True, influence=100, input='selected', interpolation='linear', lock_x=False, lock_y=False, lock_z=False)


        elif event.ctrl:
            bpy.ops.mesh.looptools_space(True, influence=100, input='selected', interpolation='linear', lock_x=False, lock_y=False, lock_z=False)


        else:
            bpy.ops.mesh.looptools_space(True, influence=100, input='selected', interpolation='cubic', lock_x=False, lock_y=False, lock_z=False)

        return {'FINISHED'}

# RMB Looptools Gstretch
class WAZOU_RMB_PIE_MENUS_OT_looptools_gstretch(bpy.types.Operator):
    """    LOOPTOOLS GSTRETCH

    CLICK - Spread Evenly
    SHIFT - Spread
    CTRL  - Project
    """
    bl_idname = 'wazou_rmb_pie_menus.looptools_gstretch'
    bl_label = "Looptools Gstretch"
    bl_options = {'REGISTER'}


    def invoke(self, context, event):

        if event.shift:
            bpy.ops.mesh.looptools_gstretch(True, conversion='none', conversion_distance=0.1, conversion_max=32,
                                            conversion_min=8, conversion_vertices=32, delete_strokes=False,
                                            influence=100, lock_x=False, lock_y=False, lock_z=False, method='irregular')

        elif event.ctrl:
            bpy.ops.mesh.looptools_gstretch(True, conversion='none', conversion_distance=0.1, conversion_max=32,
                                            conversion_min=8, conversion_vertices=32, delete_strokes=False,
                                            influence=100, lock_x=False, lock_y=False, lock_z=False, method='project')


        else:
            bpy.ops.mesh.looptools_gstretch(True, conversion='none', conversion_distance=0.1, conversion_max=32,
                                            conversion_min=8, conversion_vertices=32, delete_strokes=False,
                                            influence=100, lock_x=False, lock_y=False, lock_z=False, method='regular')

        # bpy.ops.remove.gp()

        return {'FINISHED'}



#Equalize Edges
class WAZOU_RMB_PIE_MENUS_OT_equalize_edges_length(bpy.types.Operator):
    """    EQUALIZE EDGES

    CLICK - To Active Edge
    SHIFT - To Longest
    CTRL  - To Shortest
    ALT    - To Average
    """
    bl_idname = 'wazou_rmb_pie_menus.equalize_edges_length'
    bl_label = ""
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        if tuple(context.tool_settings.mesh_select_mode) == (False, True, False):
            return True

    def invoke(self, context, event):

        if event.shift:
            bpy.ops.mo.edge_equalize_long('INVOKE_DEFAULT', True)

        elif event.ctrl:
            bpy.ops.mo.edge_equalize_short('INVOKE_DEFAULT',True)

        elif event.alt:
            bpy.ops.mo.edge_equalize_average('INVOKE_DEFAULT',True)

        else:
            bpy.ops.mo.edge_equalize_active('INVOKE_DEFAULT',True)
        return {'FINISHED'}


class WAZOU_RMB_PIE_MENUS_OT_align_space(bpy.types.Operator):
    """    SPACE / ALIGN

    CLICK - Space
    SHIFT - Align
    CTRL  - Align & Distribute
    """
    bl_idname = 'wazou_rmb_pie_menus.align_space'
    bl_label = ""
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if
                context.object.mode == "EDIT"]) == 1:
            return True

    # def execute(self, context):
    def invoke(self, context, event):

        if event.shift:
            if hasattr(bpy.types, "MESH_OT_vertex_align"):
                bpy.ops.mesh.vertex_align()

        elif event.ctrl:
            if hasattr(bpy.types, "MESH_OT_vertex_align"):
                bpy.ops.mesh.vertex_inline()

        else:
            if hasattr(bpy.types, "MESH_OT_looptools_bridge"):
                bpy.ops.mesh.looptools_space(influence=100, input='selected', interpolation='cubic', lock_x=False,
                                             lock_y=False,
                                             lock_z=False)



        return {'FINISHED'}

# # Auto Mirror Popup
class WAZOU_RMB_PIE_MENUS_OT_auto_mirror_popup(bpy.types.Operator):
    bl_idname = "object.rmb_auto_mirror_popup"
    bl_label = "Auto Mirror Popup"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def check(self, context):

        return True

    def execute(self, context):
        return {'FINISHED'}

    def draw(self, context):
        bpy.types.BisectMirror.draw(self, context)

    def invoke(self, context, event):
        dpi_value = context.user_preferences.view.ui_scale
        return context.window_manager.invoke_props_dialog(self, width=dpi_value * 400, height=100)

#Automirror
class WAZOU_RMB_PIE_MENUS_OT_auto_mirror(bpy.types.Operator):
    """    AUTO MIRROR

    CLICK - Add
    SHIFT - Apply Mirror
    CTRL  - Remove Mirror
    ALT    - Show/Hide
    CTRL+SHIFT - Auto Mirror Popup
    """
    bl_idname = "wazou_rmb_pie_menus.auto_mirror"
    bl_label = "Auto Mirror"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH']):
            return True

    def invoke(self, context, event):
        obj = context.active_object
        for obj in context.selected_objects:
            context.view_layer.objects.active = obj

            if event.shift and event.ctrl:
                bpy.ops.object.rmb_auto_mirror_popup('INVOKE_DEFAULT')


            elif event.shift:
                for mod in [m for m in obj.modifiers if m.type == 'MIRROR']:
                    if context.object.mode == "EDIT":
                        bpy.ops.object.mode_set(mode = 'OBJECT')
                        bpy.ops.object.modifier_apply( modifier = mod.name )
                        bpy.ops.object.mode_set(mode = 'EDIT')
                    else:
                        bpy.ops.object.modifier_apply( modifier = mod.name )

            elif event.ctrl:
                for mod in [m for m in obj.modifiers if m.type == 'MIRROR']:
                    bpy.ops.object.modifier_remove( modifier = mod.name )


            elif event.alt:
                for mod in [m for m in obj.modifiers if m.type == 'MIRROR']:
                    obj.modifiers[mod.name].show_viewport = not obj.modifiers[mod.name].show_viewport

            else:
                if not obj.type == 'MIRROR':
                    if context.object.mode == "EDIT":
                        bpy.ops.object.mode_set(mode = 'OBJECT')
                        bpy.ops.object.automirror()
                        bpy.ops.object.mode_set(mode = 'EDIT')

                    elif context.object.mode == "OBJECT":
                        bpy.ops.object.automirror()
                        bpy.ops.object.mode_set(mode = 'OBJECT')

                    else:
                        bpy.ops.object.automirror()


        return {"FINISHED"}


#Looptools
# class WAZOU_RMB_PIE_MENUS_MT_edit_mesh_looptools(bpy.types.Menu):
#     """    LOOPTOOLS    """
#     bl_idname = "loop.tools"
#     bl_label = "LoopTools"
#
#     def draw(self, context):
#         layout = self.layout
#         layout.operator("mesh.looptools_bridge", text="Bridge").loft = False
#         layout.operator("mesh.looptools_circle")
#         layout.operator("mesh.looptools_curve")
#         layout.operator("mesh.looptools_flatten")
#         layout.operator("mesh.looptools_gstretch")
#         layout.operator("mesh.looptools_bridge", text="Loft").loft = True
#         layout.operator("mesh.looptools_relax")
#         layout.operator("mesh.looptools_space")

#Create Hole
class WAZOU_RMB_PIE_MENUS_OT_create_hole(bpy.types.Operator):
    """    CREATE CIRCLES

    CLICK - Add Circle
    SHIFT - Add Circle with Loop
    CTRL  - Add Circle on Individual Faces
    ALT    - Subdivide Circle

    You can combine CTRL+SHIFT+ALT
    """
    bl_idname = "wazou_rmb_pie_menus.create_hole"
    bl_label = "Create Hole on a Selection"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if context.object.mode == "EDIT"]) == 1:
            return True

    def invoke(self, context, event):
        WM = context.window_manager
        obj = context.active_object
        mesh = obj.data
        bm = bmesh.from_edit_mesh(mesh)
        sel_vert=[v.index for v in bm.verts if v.select]
        faces_list=[]

        #If faces
        if tuple (context.tool_settings.mesh_select_mode) == (False, False, True) :
            #Individual
            if event.ctrl :
                bpy.ops.mesh.inset(thickness=0.02, use_individual=True)
            else:
                bpy.ops.mesh.inset(thickness=0.02)

            #Subdivide
            if event.alt :
                bpy.ops.mesh.subdivide(smoothness=0)
                bpy.ops.mesh.dissolve_mode()

                bpy.ops.mesh.poke()
            bpy.ops.mesh.looptools_circle()

            #Add Loop
            if event.shift :
                bpy.ops.mesh.inset(thickness=0.02)
                bpy.ops.mesh.select_more()

            context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
            bpy.ops.transform.resize('INVOKE_DEFAULT')

        elif tuple (context.tool_settings.mesh_select_mode) == (True, False, False) :

            if event.alt :
                for v in sel_vert:
                    bpy.ops.mesh.select_all(action='DESELECT')
                    bm.verts.ensure_lookup_table()
                    bm.verts[v].select = True

                    bpy.ops.mesh.bevel(offset=0.1, vertex_only=True)
                    bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
                    bpy.ops.mesh.subdivide(smoothness=0)
                    bpy.ops.mesh.dissolve_mode()
                    bpy.ops.mesh.looptools_circle()
                    bpy.ops.mesh.poke()
                    # bpy.ops.mesh.subdivide()

                    if event.shift :
                        bpy.ops.mesh.inset(thickness=0.02)
                        bpy.ops.mesh.select_more()

                    for f in bm.faces:
                        if f.select:
                            faces_list.append(f)

                for f in faces_list:
                    f.select = True

            elif event.shift :
                bpy.ops.mesh.bevel(offset=0.1, vertex_only=True)
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
                bpy.ops.mesh.inset(thickness=0.02)
                bpy.ops.mesh.select_more()

            else:
                bpy.ops.mesh.bevel(offset=0.1, vertex_only=True)
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')

            context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'

            bpy.ops.transform.resize('INVOKE_DEFAULT')
        else:
            pass

        del(sel_vert[:])
        del(faces_list[:])
        return {'FINISHED'}



#Apply_Transforms
class WAZOU_RMB_PIE_MENUS_OT_apply_transforms(bpy.types.Operator):
    """    APPLY TRANSFORMS

    CLICK - Apply Transforms
    SHIFT - Apply Transforms and Keep Origin
    CTRL  - APPLY Scale for Bevel Modifier
    """
    bl_idname = "wazou_rmb_pie_menus.apply_transforms"
    bl_label = "Rmb Apply Transforms"
    bl_options = {"REGISTER","UNDO"}

    def invoke(self, context, event):
        saved_location_0 = context.scene.cursor.location.copy()

        if event.shift:

            selection = context.selected_objects


            for obj in selection:
                bpy.ops.object.select_all(action='DESELECT')
                context.view_layer.objects.active = obj
                obj.select_set(state=True)
                bpy.ops.view3d.snap_cursor_to_active()
                saved_location = context.scene.cursor.location.copy()
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                context.scene.cursor.location = saved_location
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

            for obj in selection:
                obj.select_set(state=True)
                context.view_layer.objects.active =obj

            del(selection[:])

        elif event.ctrl:
            ob = context.object
            var1 = min(ob.scale, key=lambda x:abs(1-x))

            for mod in ob.modifiers:
                if mod.type == 'BEVEL':
                    mod.width *= var1
            bpy.ops.object.transform_apply(scale=True)

        else:
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        context.scene.cursor.location = saved_location_0
        return {"FINISHED"}

#Make Object An Empty
# class WAZOU_RMB_PIE_MENUS_OT_make_object_empty(bpy.types.Operator):
#     """    MAKE EMPTY
#
#     Create an object as empty for Boolean Inserts
#     """
#     bl_idname = "wazou_rmb_pie_menus.rmb_make_empty"
#     bl_label = "Make Object An Empty"
#     bl_options = {'REGISTER', 'UNDO'}
#
#     @classmethod
#     def poll(cls, context):
#         obj = context.active_object
#         if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if context.object.mode == "OBJECT"]) >= 1:
#             return True
#
#     def execute(self, context):
#         if context.object.hide_render == False:
#             context.object.hide_render = True
#             context.object.draw_type = 'WIRE'
#             context.object.cycles_visibility.camera = False
#             context.object.cycles_visibility.diffuse = False
#             context.object.cycles_visibility.glossy = False
#             context.object.cycles_visibility.scatter = False
#             context.object.cycles_visibility.transmission = False
#             context.object.cycles_visibility.shadow = False
#         elif context.object.hide_render == True:
#             context.object.hide_render = False
#             context.object.draw_type = 'SOLID'
#             context.object.cycles_visibility.camera = True
#             context.object.cycles_visibility.diffuse = True
#             context.object.cycles_visibility.glossy = True
#             context.object.cycles_visibility.scatter = True
#             context.object.cycles_visibility.transmission = True
#             context.object.cycles_visibility.shadow = True
#         return {'FINISHED'}

#Mark Seam
class WAZOU_RMB_PIE_MENUS_OT_mark_clear_seam(bpy.types.Operator):
    """    MARK/CLEAR SEAMS

    CLICK - Add Seam
    CTRL  - Clean Seam
    """
    bl_idname = "wazou_rmb_pie_menus.mark_clear_seam"
    bl_label = "Mark/clear Seam, Ctrl to Clear Seam"
    bl_options = {'REGISTER','UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if context.object.mode == "EDIT"]) == 1:
            return True

    def invoke(self, context, event):

        if event.ctrl:
            bpy.ops.mesh.mark_seam(clear=True)
        else:
            bpy.ops.mesh.mark_seam()
        return {'FINISHED'}

#Unwrap
class WAZOU_RMB_PIE_MENUS_OT_unwrap(bpy.types.Operator):
    """    UNWRAP

    CLICK - Unwrap
    SHIFT - Smart Project
    CTRL  - Follow Active quad
    """
    bl_idname = "wazou_rmb_pie_menus.unwrap"
    bl_label = "Unwrap"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if context.object.mode == "EDIT"]) == 1:
            return True

    def invoke(self, context, event):
        obj = context.edit_object
        me = obj.data
#        bm = bmesh.from_edit_mesh(me)
        bm = bmesh.from_edit_mesh(context.object.data)
        sel_vert=[e for e in bm.verts if e.select]

        if event.shift :
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.uv.smart_project()

        if event.ctrl:
            if len(sel_vert)>1:

                pass
            else:
                bpy.ops.uv.follow_active_quads()

        if event.alt:
            bpy.ops.uv.reset()

        else:
            if tuple (context.tool_settings.mesh_select_mode) == (False, True, False) :
                for e in bm.edges:
                    if e.select :
                        bpy.ops.mesh.mark_seam(clear=False)
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
                bpy.ops.mesh.select_all(action='SELECT')

            bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.02)

        del(sel_vert[:])
        return {"FINISHED"}

#Simplify Circle
class WAZOU_RMB_PIE_MENUS_OT_simplify_circle(bpy.types.Operator):
    """    SIMPLIFY CIRCLE"""

    bl_idname = "wazou_rmb_pie_menus.circle"
    bl_label = "Simplify Circle"
    bl_options = {"REGISTER", 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if context.object.mode == "EDIT"]) == 1:
            return True

    def execute(self, context):
        bpy.ops.mesh.select_nth()
        bpy.ops.mesh.edge_collapse()
        return {"FINISHED"}

#Extract_Duplicate
class WAZOU_RMB_PIE_MENUS_OT_extract_duplicate(bpy.types.Operator):
    """    EXTRACT/DUPLICATE

    CLICK - Duplicate Selection to new Object
    SHIFT - Extract Selection
    CTRL  - Join with Remove Double if 2 Objects are Selected

    EDIT MODE
    SHIFT - Extract
    CTRL  - Duplicate and stay in Edit Mode
    CTRL+SHIFT - Extract and stay in Edit Mode
    """
    bl_idname = "wazou_rmb_pie_menus.extract_duplicate"
    bl_label = "Extract Duplicate"
    bl_options = {"REGISTER","UNDO"}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH']) >= 1:
            return True

    def invoke(self, context, event):
        obj = context.active_object

        if context.object.mode == 'OBJECT':
            if len(context.selected_objects) == 1:
                bpy.ops.mesh.separate(type='LOOSE')
                obj.select_set(state=True)
            else:
                bpy.ops.Object.join()
                if event.shift:
                    bpy.ops.object.mode_set(mode = 'EDIT')
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.remove_doubles()
                    bpy.ops.object.mode_set(mode = 'OBJECT')

        elif context.object.mode == 'EDIT':
            if event.shift:
                bpy.ops.mesh.separate(type='SELECTED')
                bpy.ops.object.mode_set(mode = 'OBJECT')
                obj.select_set(state=False)
                context.view_layer.objects.active =  context.selected_objects[0]

            else:
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.duplicate_move()
                bpy.ops.object.mode_set(mode = 'EDIT')

                if tuple (context.tool_settings.mesh_select_mode) == (False, False, True) :
                    bpy.ops.mesh.select_all(action='INVERT')
                    bpy.ops.mesh.delete(type='FACE')
                else:
                    bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                    bpy.ops.mesh.select_all(action='INVERT')
                    bpy.ops.mesh.delete(type='VERT')

                bpy.ops.object.mode_set(mode = 'OBJECT')

            if event.ctrl:
                bpy.ops.object.mode_set(mode = 'EDIT')

        return {"FINISHED"}

#Poke_face
class WAZOU_RMB_PIE_MENUS_OT_inset_poke_faces(bpy.types.Operator):
    """    INSERT/POKE

    CLICK - Insert
    SHIFT - Poke
    CTRL  - Insert with Poke
    """
    bl_idname = "wazou_rmb_pie_menus.inset_poke_faces"
    bl_label = "Inset/Poke Faces"
    bl_options = {"REGISTER","UNDO"}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if context.object.mode == "EDIT"]) == 1:
            return True

    def invoke(self, context, event):
        bm = bmesh.from_edit_mesh(context.object.data)
        sel_faces=[e for e in bm.faces if e.select]

        if event.shift:
            if len(sel_faces)>0:
                bpy.ops.mesh.poke()
            else:
                bpy.ops.mesh.edge_face_add()
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
                bpy.ops.mesh.poke()


        elif event.ctrl:
            if len(sel_faces)>0:
                bpy.ops.mesh.poke()
                bpy.ops.mesh.inset('INVOKE_DEFAULT')
            else:
                bpy.ops.mesh.edge_face_add()
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
                bpy.ops.mesh.poke()
                bpy.ops.mesh.inset('INVOKE_DEFAULT')
        else:
            if len(sel_faces)==0:
                bpy.ops.mesh.edge_face_add()
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            bpy.ops.mesh.inset('INVOKE_DEFAULT')

        del(sel_faces[:])
        return {"FINISHED"}

#Subsurf

def WAZOU_RMB_PIE_MENUS_Add_Subsurf(context):
    obj = context.active_object
    new_subsurf = obj.modifiers.new("Subsurf", "SUBSURF")
    new_subsurf.show_only_control_edges = True
    new_subsurf.levels = 2
    new_subsurf.show_on_cage = True
    return new_subsurf

class WAZOU_RMB_PIE_MENUS_OT_subsurf_operator(bpy.types.Operator):
    """    SUBSURF

    CLICK - Add Subsurf
    SHIFT - Apply Subsurf Modifier
    CTRL  - Remove Subsurf Modifier
    ALT    - Hide Subsurf Modifier

    If No Subsurf + Shift - Add and Apply Subsurf Modifier
    """
    bl_idname = "wazou_rmb_pie_menus.subsurf_operator"
    bl_label = "Subsurf Operator"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type in ['MESH','TEXT','CURVE'] ]) >= 1:
            return True

    def invoke(self, context, event):
        obj = context.active_object
        selection = context.selected_objects
        edit_mode = False

        for obj in selection:
            context.view_layer.objects.active =obj
            if obj.modifiers:
                subsurf = [mod for mod in obj.modifiers if mod.type == 'SUBSURF']
                if subsurf :
                    #Apply
                    if event.shift:
                        if context.object.mode == "EDIT":
                            edit_mode = True
                            bpy.ops.object.mode_set(mode = 'OBJECT')

                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=subsurf[0].name)

                        if edit_mode == True:
                            bpy.ops.object.mode_set(mode = 'EDIT')
                        # self.report({'INFO'}, "Subsurf Modifier Applied")

                    #Remove
                    elif event.ctrl:
                        obj.modifiers.remove(subsurf[0])
                        # self.report({'INFO'}, "Subsurf Modifier Removed")
                    #Hide
                    elif event.alt:
                        obj.modifiers[subsurf[0].name].show_viewport = not obj.modifiers[subsurf[0].name].show_viewport

                    else:
                        obj.modifiers.remove(subsurf[0])
                        # self.report({'INFO'}, "Subsurf Modifier Removed")

                else:
                    if event.shift:
                        subsurf= WAZOU_RMB_PIE_MENUS_Add_Subsurf(context)
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=subsurf.name)

                    elif not event.ctrl and not event.alt:
                        WAZOU_RMB_PIE_MENUS_Add_Subsurf(context)

            else:
                if event.shift:
                    subsurf= WAZOU_RMB_PIE_MENUS_Add_Subsurf(context)
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=subsurf.name)

                elif not event.ctrl and not event.alt:
                    WAZOU_RMB_PIE_MENUS_Add_Subsurf(context)


        return {"FINISHED"}


#Apply_Remove_Modifiers
class WAZOU_RMB_PIE_MENUS_OT_apply_remove_modifiers(bpy.types.Operator):
    """ APPLY/REMOVE MODIFIERS

    CLICK - Apply Modifiers
    CTRL  - Remove Modifiers
    ALT   - Hide Modifiers
    """
    bl_idname = "wazou_rmb_pie_menus.apply_remove_modifiers"
    bl_label = "Apply Remove Modifiers"
    bl_options = {"REGISTER",'UNDO'}

    def invoke(self, context, event):
        obj = context.active_object
        selection = context.selected_objects
        edit_mode = False
        #Remove
        if event.ctrl:
            for obj in selection:
                obj.select_set(state=True)
                if obj.modifiers:
                    context.view_layer.objects.active = obj
                    for mod in obj.modifiers :
                        bpy.ops.object.modifier_remove(modifier=mod.name)
        #Hide
        elif event.alt:
            for obj in selection:
                obj.select_set(state=True)
                if obj.modifiers:
                    context.view_layer.objects.active = obj
                    for mod in obj.modifiers :
                        obj.modifiers[mod.name].show_viewport = not obj.modifiers[mod.name].show_viewport

        #Apply
        else:
            if context.object.mode == "EDIT":
                edit_mode = True
                bpy.ops.object.mode_set(mode = 'OBJECT')

            for obj in selection:
                obj.select_set(state=True)
                if obj.modifiers:
                    context.view_layer.objects.active=obj
                    for mod in obj.modifiers :
                        if mod.show_viewport == False :
                            bpy.ops.object.modifier_remove(modifier=mod.name)
                        else:
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)

            if edit_mode == True:
                bpy.ops.object.mode_set(mode = 'EDIT')

        return {"FINISHED"}


# Knurl
class WAZOU_RMB_PIE_MENUS_OT_knurl(bpy.types.Operator):
    """    KNURL

    CLICK - Straight with Poke
    SHIFT - Rotated with Poke
    CTRL  - Rotated Faces
    ALT    - Quad Knurl
    """
    bl_idname = 'wazou_rmb_pie_menus.knurl'
    bl_label = "Smart Knurl"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if
                context.object.mode == "EDIT"]) == 1:
            return True

    def invoke(self, context, event):

        if event.shift:
            bpy.ops.mesh.poke(True, offset=0)
            bpy.ops.mesh.tris_convert_to_quads(True, face_threshold=0.698132, shape_threshold=0.698132)
            bpy.ops.mesh.poke(True, offset=0.1)

        elif event.ctrl:
            bpy.ops.mesh.poke(True, offset=0)
            bpy.ops.mesh.tris_convert_to_quads(True, face_threshold=0.698132, shape_threshold=0.698132)

        elif event.alt:
            bpy.ops.mesh.poke(True, offset=0)
            bpy.ops.mesh.tris_convert_to_quads(True, face_threshold=0.698132, shape_threshold=0.698132)
            bpy.ops.mesh.inset(True, use_boundary=True, thickness=0.0269157, depth=0.0958026, use_individual=True)

        else:
            bpy.ops.mesh.poke(True, offset=0.1)

        return {'FINISHED'}

# #Parent Unparent
# def find_parent(ob, lst):
#
#     lst.append(ob)
#     if ob.parent:
#         find_parent(ob.parent, lst)
#
# # select_hierarchy
# def find_child(ob, lst):
#     for x in ob.children:
#         lst.append(x)
#         find_child(x, lst)
#
# def Last_Parent():
#     lst = []  # list for all objects
#     find_parent(bpy.context.object, lst)  # find parent
#     if len(lst) > 0:
#
#         last_parent = lst[0]
#         for p in lst:
#             # parent of everything has no parent itself
#             if not p.parent: last_parent = p
#             bpy.ops.object.select_all(action='DESELECT')
#             bpy.context.view_layer.objects.active = last_parent
#             last_parent.select_set(state=True)

# #Select Last Parent
# class WAZOU_RMB_PIE_MENUS_OT_select_last_parent(bpy.types.Operator):
#     """    SELECT HIERARCHY
#
#     CLICK - Select Last Parent
#     SHIFT - Select Hierarchy
#     """
#     bl_idname = 'wazou_rmb_pie_menus.select_last_parent'
#     bl_label = ""
#     bl_options = {'REGISTER'}
#
#     @classmethod
#     def poll(cls, context):
#         return True
#
#     def invoke(self, context, event):
#
#         # def execute(self, context):
#         obj = context.active_object
#         parent_list = []
#
#         for obj in context.selected_objects:
#             bpy.ops.object.select_all(action='DESELECT')
#             context.view_layer.objects.active = obj
#             Last_Parent()
#
#             for obj in context.selected_objects:
#                 parent_list.append(obj)
#
#         for obj in parent_list:
#             context.view_layer.objects.active = obj
#             obj.select_set(state=True)
#
#         if event.shift:
#             for obj in context.selected_objects:
#                 context.view_layer.objects.active = obj
#                 bpy.ops.nw.select_hierarchy()
#
#         print("Parent List:", parent_list)
#         return {'FINISHED'}

# class WAZOU_RMB_PIE_MENUS_OT_select_hierarchy(bpy.types.Operator):
#     bl_idname = "object.select_hierarchy"
#     bl_label = "select hierarchy"
#     bl_options = {"UNDO"}
#
#     def execute(self, context):
#         lst = []  # list for all objects
#         find_parent(context.object, lst)  # find parent
#
#         if len(lst) > 0:
#
#             last_parent = lst[0]
#             for p in lst:
#                 # parent of everything has no parent itself
#                 if not p.parent: last_parent = p
#
#             # find children for each parent
#             for c in lst: find_child(c, lst)
#
#             # select all
#             for x in lst: x.select_set(state=True)
#
#             # make parent active
#             context.view_layer.objects.active = last_parent
#
#         # print(lst)
#         context.space_data.pivot_point = 'ACTIVE_ELEMENT'
#         return {'FINISHED'}




#Parent Objects
class WAZOU_RMB_PIE_MENUS_OT_parent_objects(bpy.types.Operator):
    """    PARENT/UNPARENT

    CLICK - Parent Selection to Active Object
    SHIFT - Parent with Parent orientation
    CTRL  - Clear and Keep Transforms
    CTRL+CLICK - Clear
    ALT    - Select Hierarchy
    ALT+SHIFT - Select Only Parents
    """
    bl_idname = "wazou_rmb_pie_menus.parent_objects"
    bl_label = "Parent Objects"
    bl_options = {"REGISTER","UNDO"}

    def invoke(self, context, event):
        obj = context.active_object

        #Unparent
        if event.ctrl:
            #If parent selected
            if not obj.parent:
                C = context
                for obj in C.object.children:
                    obj.select_set(state=True)

                    if event.shift:
                        bpy.ops.object.parent_clear(type='CLEAR')
                    else:
                        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
                    bpy.ops.object.select_all(action='TOGGLE')


            #If child selected
            else:
                for obj in context.selected_objects:
                    obj.select_set(state=True)
                    context.view_layer.objects.active=obj

                    if event.shift:
                        bpy.ops.object.parent_clear(type='CLEAR')
                    else:
                        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')


        elif event.alt:
            parent_list = []

            for obj in context.selected_objects:
                bpy.ops.object.select_all(action='DESELECT')
                context.view_layer.objects.active = obj
                Last_Parent()

                for obj in context.selected_objects:
                    parent_list.append(obj)

            for obj in parent_list:
                context.view_layer.objects.active = obj
                obj.select_set(state=True)

            if not event.shift:
                for obj in context.selected_objects:
                    context.view_layer.objects.active = obj
                    # bpy.ops.nw.select_hierarchy()
                    # bpy.ops.object.select_hierarchy()
                    bpy.ops.object.select_grouped(extend=True, type='CHILDREN_RECURSIVE')

            print("Parent List:", parent_list)
            # bpy.ops.object.select_hierarchy()

        else:
            # Parent
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
        return {"FINISHED"}



# # Empty Images
# class WAZOU_RMB_PIE_MENUS_OT_add_empty_image(bpy.types.Operator):
#     """    EMPTY IMAGE
#
#     CLICK - Add Empty Image
#     SHIFT - Add Image As Plane
#     """
#     bl_idname = "wazou_rmb_pie_menus.add_empty_image"
#     bl_label = "Empty Image"
#     bl_options = {"REGISTER"}
#
#     filepath : bpy.props.StringProperty(subtype="FILE_PATH")
#
#     filter_glob = StringProperty(
#         default=".exr;*.jpg;*.jpeg;*.png;*.tif",
#         options={'HIDDEN'},
#     )
#
#     def execute(self, context):
#
#         # Creation
#         if context.object is not None:
#             if context.object.mode == "EDIT":
#                 bpy.ops.object.mode_set(mode='OBJECT')
#             bpy.ops.object.select_all(action='DESELECT')
#
#         empty = bpy.data.objects.new("Empty_Image", None)
#         scene = context.scene
#         scene.objects.link(empty)
#         scene.update()
#
#         # Rotation
#         context.view_layer.objects.active = empty
#         empty.select_set(state=True)
#         bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0))
#
#         # Edition
#         empty.empty_draw_type = 'IMAGE'
#         empty.empty_image_offset[0] = -0.5
#         empty.empty_image_offset[1] = -0.5
#         empty.color[3] = 0.5
#         empty.show_transparent = True
#
#         # Link Image
#         img_name = bpy.data.images.load(filepath=self.filepath, check_existing=True)
#         empty.data = img_name
#
#         return {"FINISHED"}
#
#     def invoke(self, context, event):
#
#         if not event.shift:
#             context.window_manager.fileselect_add(self)
#             return {'RUNNING_MODAL'}
#
#         else:
#             if hasattr(bpy.types, "IMPORT_IMAGE_OT_to_plane"):
#                 bpy.ops.import_image.to_plane('INVOKE_DEFAULT')
#
#             # else:
#                 # self.report({'INFO'}, "Activate Image as Plane Addon")
#
#             return {"FINISHED"}


#Primitives
class WAZOU_RMB_PIE_MENUS_OT_primitives(bpy.types.Operator):
    """    ADD PRIMITIVES

    CLICK - Add
    SHIFT - Add on Selection
    CTRL  - Add on Mouse
    ALT    - Add in Edit Mode
    CTRL+SHIFT : Add Mirror Modifier

    You can combine ATL + SHIFT or ALT + CTRL
    """

    bl_idname = "wazou_rmb_pie_menus.primitives"
    bl_label = "Custom Add Primitives"
    bl_options = {"REGISTER"}

    primitive : EnumProperty(
        items = (('cube', "Cube", ""),
                 ('mesh_circle', "Circle", ""),
                 ('sphere', "Sphere", ""),
                 ('plan', "Plan", ""),
                 ('grid', "Grid", ""),
                 ('cylinder', "Cylinder", ""),
                 ('cone', "Cone", ""),
                 ('torus', "Torus", ""),
                 ('empty_axe', "Empty_Axe", ""),
                 ('bezier', "Bezier", ""),
                 ('vertex', "Vertex", ""),
                 ('text', "Text", ""),
                 ('area', "Area", ""),
                 ('sun', "Sun", ""),
                 ('point', "Point", ""),
                 ('spot', "Spot", ""),
                 ('camera', "Camera", ""),
                 ('circle', "Circle", ""),
                 ('armature', "Armature", ""),
                 ('curve_line', "Curve Line", "")),
                 default = 'cube'
                 )

    def invoke(self, context, event):
        obj = False
        obj = context.active_object

        if context.selected_objects and context.object is not None :
            mirror_object = context.active_object
        else:
            mirror_object = [obj for obj in context.selected_objects if context.object]

        saved_location = context.scene.cursor.location.copy()

        if event.shift:
            bpy.ops.view3d.snap_cursor_to_selected()

        if event.ctrl:
            bpy.ops.view3d.cursor3d('INVOKE_DEFAULT')


        #Cube
        if self.primitive == 'cube':
            if event.alt:
                if context.object is not None and context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.mesh.primitive_cube_add(enter_editmode=True, align='WOLRD')
            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.mesh.primitive_cube_add(True, enter_editmode=False, align='WORLD')

                #Add Mirror
                if event.ctrl and event.shift:
                    act_obj = context.active_object
                    newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
                    newMod.show_on_cage = True
                    newMod.show_in_editmode = True
                    if not mirror_object:
                        bpy.ops.object.empty_add(type='PLAIN_AXES')
                        bpy.ops.object.location_clear(clear_delta=False)
                        empty_for_mirror = context.active_object
                        bpy.ops.object.select_all(action='DESELECT')
                        context.view_layer.objects.active = act_obj
                        act_obj.select_set(state=True)
                        newMod.mirror_object = empty_for_mirror
                    else:
                        newMod.mirror_object = mirror_object

        # Circle
        elif self.primitive == 'mesh_circle':
            if event.alt:
                if context.object is not None and context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.mesh.primitive_circle_add(vertices=16, radius=1, enter_editmode=True, align='WORLD')


            else:
                if context.object is not None:
                    bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.mesh.primitive_circle_add(True, vertices=16, radius=1, enter_editmode=False, align='WORLD')

                # Add Mirror
                if event.ctrl and event.shift:
                    act_obj = context.active_object
                    newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
                    newMod.show_on_cage = True
                    newMod.show_in_editmode = True
                    if not mirror_object:
                        bpy.ops.object.empty_add(type='PLAIN_AXES')
                        bpy.ops.object.location_clear(clear_delta=False)
                        empty_for_mirror = context.active_object
                        bpy.ops.object.select_all(action='DESELECT')
                        context.view_layer.objects.active = act_obj
                        act_obj.select_set(state=True)
                        newMod.mirror_object = empty_for_mirror
                    else:
                        newMod.mirror_object = mirror_object

        #Plan
        elif self.primitive == 'plan':
            if event.alt:
                if context.object is not None and context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.mesh.primitive_plane_add(enter_editmode=True, align='WORLD')


            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.mesh.primitive_plane_add(True, enter_editmode=False, align='WORLD')
                #Add Mirror
                if event.ctrl and event.shift:
                    act_obj = context.active_object
                    newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
                    newMod.show_on_cage = True
                    newMod.show_in_editmode = True
                    if not mirror_object:
                        bpy.ops.object.empty_add(type='PLAIN_AXES')
                        bpy.ops.object.location_clear(clear_delta=False)
                        empty_for_mirror = context.active_object
                        bpy.ops.object.select_all(action='DESELECT')
                        context.view_layer.objects.active = act_obj
                        act_obj.select_set(state=True)
                        newMod.mirror_object = empty_for_mirror
                    else:
                        newMod.mirror_object = mirror_object

        #Grid
        elif self.primitive == 'grid':
            if event.alt:
                if context.object is not None and context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=10, y_subdivisions=10, size=2, enter_editmode=True, align='WORLD')

            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')

                bpy.ops.mesh.primitive_grid_add(True, x_subdivisions=10, y_subdivisions=10, size=2, enter_editmode=False,
                                                    align='WORLD')
                #Add Mirror
                if event.ctrl and event.shift:
                    act_obj = context.active_object
                    newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
                    newMod.show_on_cage = True
                    newMod.show_in_editmode = True
                    if not mirror_object:
                        bpy.ops.object.empty_add(type='PLAIN_AXES')
                        bpy.ops.object.location_clear(clear_delta=False)
                        empty_for_mirror = context.active_object
                        bpy.ops.object.select_all(action='DESELECT')
                        context.view_layer.objects.active = act_obj
                        act_obj.select_set(state=True)
                        newMod.mirror_object = empty_for_mirror
                    else:
                        newMod.mirror_object = mirror_object

        #Sphere
        elif self.primitive == 'sphere':
            if event.alt:
                if context.object is not None and context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, radius=1, enter_editmode=True, align='WORLD')

            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.mesh.primitive_uv_sphere_add(True, segments=24, ring_count=12, radius=1, enter_editmode=False, align='WORLD')
                #Add Mirror
                if event.ctrl and event.shift:
                    act_obj = context.active_object
                    newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
                    newMod.show_on_cage = True
                    newMod.show_in_editmode = True
                    if not mirror_object:
                        bpy.ops.object.empty_add(type='PLAIN_AXES')
                        bpy.ops.object.location_clear(clear_delta=False)
                        empty_for_mirror = context.active_object
                        bpy.ops.object.select_all(action='DESELECT')
                        context.view_layer.objects.active = act_obj
                        act_obj.select_set(state=True)
                        newMod.mirror_object = empty_for_mirror
                    else:
                        newMod.mirror_object = mirror_object

        #Cylinder
        elif self.primitive == 'cylinder':
            if event.alt:
                if context.object is not None and context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=1, depth=2, enter_editmode=True, align='WORLD')

            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.mesh.primitive_cylinder_add(True, vertices=16, radius=1, depth=2, enter_editmode=False, align='WORLD')
                #Add Mirror
                if event.ctrl and event.shift:
                    act_obj = context.active_object
                    newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
                    newMod.show_on_cage = True
                    newMod.show_in_editmode = True
                    if not mirror_object:
                        bpy.ops.object.empty_add(type='PLAIN_AXES')
                        bpy.ops.object.location_clear(clear_delta=False)
                        empty_for_mirror = context.active_object
                        bpy.ops.object.select_all(action='DESELECT')
                        context.view_layer.objects.active = act_obj
                        act_obj.select_set(state=True)
                        newMod.mirror_object = empty_for_mirror
                    else:
                        newMod.mirror_object = mirror_object

        #cone
        elif self.primitive == 'cone':
            if event.alt:
                if context.object is not None and context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.mesh.primitive_cone_add(vertices=16, radius1=1, radius2=0, depth=2, enter_editmode=True, align='WORLD')

            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.mesh.primitive_cone_add(True, vertices=16, radius1=1, radius2=0, depth=2, enter_editmode=False, align='WORLD')
                #Add Mirror
                if event.ctrl and event.shift:
                    act_obj = context.active_object
                    newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
                    newMod.show_on_cage = True
                    newMod.show_in_editmode = True
                    if not mirror_object:
                        bpy.ops.object.empty_add(type='PLAIN_AXES')
                        bpy.ops.object.location_clear(clear_delta=False)
                        empty_for_mirror = context.active_object
                        bpy.ops.object.select_all(action='DESELECT')
                        context.view_layer.objects.active = act_obj
                        act_obj.select_set(state=True)
                        newMod.mirror_object = empty_for_mirror
                    else:
                        newMod.mirror_object = mirror_object

        #Empty Axe
        elif self.primitive == 'empty_axe':
            if context.object is not None :
                bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.empty_add(type='PLAIN_AXES', radius=1, align='WORLD')


        #Bezier
        elif self.primitive == 'bezier':
            if event.alt:
                if context.object is not None and context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.curve.primitive_bezier_curve_add(radius=1, enter_editmode=True, align='WORLD')

            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.curve.primitive_bezier_curve_add(True, radius=1, enter_editmode=False, align='WORLD')
                #Add Mirror
                if event.ctrl and event.shift:
                    act_obj = context.active_object
                    newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
                    newMod.show_on_cage = True
                    newMod.show_in_editmode = True
                    if not mirror_object:
                        bpy.ops.object.empty_add(type='PLAIN_AXES')
                        bpy.ops.object.location_clear(clear_delta=False)
                        empty_for_mirror = context.active_object
                        bpy.ops.object.select_all(action='DESELECT')
                        context.view_layer.objects.active = act_obj
                        act_obj.select_set(state=True)
                        newMod.mirror_object = empty_for_mirror
                    else:
                        newMod.mirror_object = mirror_object

        #Circle
        elif self.primitive == 'circle':
            if event.alt:
                if context.object is not None and context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.curve.primitive_bezier_circle_add(radius=1, enter_editmode=True, align='WORLD')

            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.curve.primitive_bezier_circle_add(True, radius=1, enter_editmode=False, align='WORLD')
                #Add Mirror
                if event.ctrl and event.shift:
                    act_obj = context.active_object
                    newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
                    newMod.show_on_cage = True
                    newMod.show_in_editmode = True
                    if not mirror_object:
                        bpy.ops.object.empty_add(type='PLAIN_AXES')
                        bpy.ops.object.location_clear(clear_delta=False)
                        empty_for_mirror = context.active_object
                        bpy.ops.object.select_all(action='DESELECT')
                        context.view_layer.objects.active = act_obj
                        act_obj.select_set(state=True)
                        newMod.mirror_object = empty_for_mirror
                    else:
                        newMod.mirror_object = mirror_object

        #Armature
        elif self.primitive == 'armature':
            if event.alt:
                if context.object is not None and context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.object.armature_add(radius=1, enter_editmode=True, align='WORLD')


            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.armature_add(True, radius=1, enter_editmode=False, align='WORLD')
        #Text
        elif self.primitive == 'text':
            if event.alt:
                if context.object is not None and context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.object.text_add(radius=1, enter_editmode=True, align='WORLD')
            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.text_add(True, radius=1, enter_editmode=False, align='WORLD')
                #Add Mirror
                if event.ctrl and event.shift:
                    act_obj = context.active_object
                    newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
                    newMod.show_on_cage = True
                    newMod.show_in_editmode = True
                    if not mirror_object:
                        bpy.ops.object.empty_add(type='PLAIN_AXES')
                        bpy.ops.object.location_clear(clear_delta=False)
                        empty_for_mirror = context.active_object
                        bpy.ops.object.select_all(action='DESELECT')
                        context.view_layer.objects.active = act_obj
                        act_obj.select_set(state=True)
                        newMod.mirror_object = empty_for_mirror
                    else:
                        newMod.mirror_object = mirror_object

        #Torus
        elif self.primitive == 'torus':
            if event.alt:
                if context.object is not None and context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.mesh.primitive_torus_add(align='WORLD', major_segments=32, minor_segments=12, mode='MAJOR_MINOR',
                                                 major_radius=1, minor_radius=0.25, abso_major_rad=1.25,
                                                 abso_minor_rad=0.75)

                bpy.ops.object.mode_set(mode = 'EDIT')
            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.mesh.primitive_torus_add(True, align='WORLD', major_segments=32, minor_segments=12,
                                                 mode='MAJOR_MINOR',
                                                 major_radius=1, minor_radius=0.25, abso_major_rad=1.25,
                                                 abso_minor_rad=0.75)
                #Add Mirror
                if event.ctrl and event.shift:
                    act_obj = context.active_object
                    newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
                    newMod.show_on_cage = True
                    newMod.show_in_editmode = True
                    if not mirror_object:
                        bpy.ops.object.empty_add(type='PLAIN_AXES')
                        bpy.ops.object.location_clear(clear_delta=False)
                        empty_for_mirror = context.active_object
                        bpy.ops.object.select_all(action='DESELECT')
                        context.view_layer.objects.active = act_obj
                        act_obj.select_set(state=True)
                        newMod.mirror_object = empty_for_mirror
                    else:
                        newMod.mirror_object = mirror_object

        #Vertex
        elif self.primitive == 'vertex':
            if context.object is not None :
                bpy.ops.object.mode_set(mode = 'OBJECT')

            bpy.ops.view3d.cursor3d('INVOKE_DEFAULT')
            bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

            #Add Mirror
            if event.ctrl and event.shift:
                act_obj = context.active_object
                newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
                newMod.show_on_cage = True
                newMod.show_in_editmode = True
                if not mirror_object:
                    bpy.ops.object.empty_add(type='PLAIN_AXES')
                    bpy.ops.object.location_clear(clear_delta=False)
                    empty_for_mirror = context.active_object
                    bpy.ops.object.select_all(action='DESELECT')
                    context.view_layer.objects.active = act_obj
                    act_obj.select_set(state=True)
                    newMod.mirror_object = empty_for_mirror
                else:
                    newMod.mirror_object = mirror_object

            elif event.shift:
                context.scene.tool_settings.use_snap = True
                context.scene.tool_settings.snap_element = 'INCREMENT'
                context.scene.tool_settings.use_snap_grid_absolute = True

            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            bpy.ops.mesh.merge(type='CENTER')
            shading = context.space_data.shading
            if shading.show_xray:
                shading.show_xray = False
            else:
                pass
            # if context.space_data.use_occlude_geometry == True :
            #     context.space_data.use_occlude_geometry = False
            # else :
            #     pass


            bpy.ops.transform.translate('INVOKE_DEFAULT')

        #Curve Line
        elif self.primitive == 'curve_line':
            if context.object is not None and obj.type == 'MESH':
                bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.curve.primitive_bezier_curve_add(enter_editmode=False, align='VIEW')

            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.curve.select_all(action='SELECT')

            bpy.ops.curve.delete(type='VERT')
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.mode_set(mode = 'EDIT')

            context.space_data.overlay.show_curve_normals = False

            #Add Mirror
            bpy.ops.object.mode_set(mode = 'OBJECT')
            if event.ctrl and event.shift:
                act_obj = context.active_object
                newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
                newMod.show_on_cage = True
                newMod.show_in_editmode = True
                if not mirror_object:
                    bpy.ops.object.empty_add(type='PLAIN_AXES')
                    bpy.ops.object.location_clear(clear_delta=False)
                    empty_for_mirror = context.active_object
                    bpy.ops.object.select_all(action='DESELECT')
                    context.view_layer.objects.active = act_obj
                    act_obj.select_set(state=True)
                    newMod.mirror_object = empty_for_mirror
                else:
                    newMod.mirror_object = mirror_object

            bpy.ops.object.mode_set(mode = 'EDIT')

            bpy.ops.curve.draw('INVOKE_DEFAULT')

        #Area
        elif self.primitive == 'area':
            if context.object is not None :
                bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.light_add(type='AREA', radius=1)


        #Sun
        elif self.primitive == 'sun':
            if context.object is not None :
                bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.light_add(type='SUN')


        #Spot
        elif self.primitive == 'spot':
            if context.object is not None :
                bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.light_add(type='SPOT')

        #Point
        elif self.primitive == 'point':
            if context.object is not None :
                bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.light_add(type='POINT')


        #Camera
        elif self.primitive == 'camera':
            obj = context.active_object

            if event.shift:
                if len([obj for obj in context.selected_objects if context.object is not None]) >= 1:
#                if getattr(context, 'selected_objects')
                    act_obj = True
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                    bpy.ops.object.select_all(action='DESELECT')

                else:
                    act_obj = False

                #Add cam and go inside
                bpy.ops.object.camera_add()
                cam = context.active_object.name
                context.scene.camera = bpy.data.objects[cam]
                bpy.ops.view3d.camera_to_view()
                context.space_data.lock_camera = True
                context.scene.render.use_border = True
                context.object.data.lens = 55

                if act_obj == True :
                    bpy.ops.object.select_all(action='DESELECT')
                    context.view_layer.objects.active = obj
                    obj.select_set(state=True)

                else:
                    bpy.ops.object.select_all(action='DESELECT')


            elif event.alt :
                if len([obj for obj in context.selected_objects if context.object is not None]) >= 1:
#                if getattr(context, 'selected_objects')
                    act_obj = True
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                    bpy.ops.object.select_all(action='DESELECT')

                else:
                    act_obj = False

                #Create Empty Dof
                bpy.ops.object.empty_add(type='PLAIN_AXES', radius=3)

                empty = context.active_object

                #Add cam and go inside
                bpy.ops.object.camera_add()
                cam = context.active_object.name
                context.scene.camera = bpy.data.objects[cam]
                bpy.ops.view3d.camera_to_view()
                context.space_data.lock_camera = True
                context.scene.render.use_border = True

                #Name empty Dof and use it for camera
                empty.name = "Dof_" + cam
                context.object.data.dof.use_dof = True
                context.object.data.dof.focus_object = empty

                if act_obj == True :
                    bpy.ops.object.select_all(action='DESELECT')
                    context.view_layer.objects.active = obj
                    obj.select_set(state=True)
                else:
                    bpy.ops.object.select_all(action='DESELECT')
                    context.view_layer.objects.active = empty
                    empty.select_set(state=True)


            else:
                bpy.ops.object.camera_add()

        if event.ctrl:
            bpy.ops.transform.translate('INVOKE_DEFAULT')

        context.scene.cursor.location = saved_location
        return {"FINISHED"}

# # Wonder Mesh Primitives
# class RMB_Wonder_Mesh_Primitives(bpy.types.Operator):
#     """    WM PRIMITIVES
#
#     CLICK - Add
#     SHIFT - Add on Selection
#     CTRL  - Add on Mouse
#     ALT    - Show Wire
#     CTRL+SHIFT - Add Mirror
#     """
#
#     bl_idname = "object.rmb_wonder_mesh_primitives"
#     bl_label = "Wonder Mesh Primitives"
#     bl_options = {"REGISTER"}
#
#     primitive = EnumProperty(
#         items=(('plane', "Plane", ""),
#                ('box', "box", ""),
#                ('ring', "Ring", ""),
#                ('tube', "Tube", ""),
#                ('sphere', "Sphere", ""),
#                ('capsule', "Capsule", ""),
#                ('cone', "Cone", ""),
#                ('torus', "Torus", ""),
#                ('screw', "Screw", "")),
#         default='box'
#     )
#
#     def invoke(self, context, event):
#         obj = False
#         obj = context.active_object
#
#         if context.selected_objects and context.object is not None:
#             mirror_object = context.active_object
#         else:
#             mirror_object = [obj for obj in context.selected_objects if context.object]
#
#         saved_location = context.scene.cursor.location.copy()
#
#         if event.shift:
#             bpy.ops.view3d.snap_cursor_to_selected()
#
#         if event.ctrl:
#             bpy.ops.view3d.cursor3d('INVOKE_DEFAULT')
#
#         # Box
#         if self.primitive == 'box':
#             if context.object is not None:
#                 bpy.ops.object.mode_set(mode='OBJECT')
#             bpy.ops.mesh.make_wbox(True)
#
#             if event.alt:
#                 context.object.show_wire = True
#                 context.object.show_all_edges = True
#
#             # Add Mirror
#             if event.ctrl and event.shift:
#                 act_obj = context.active_object
#                 newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
#                 newMod.show_on_cage = True
#                 newMod.show_in_editmode = True
#                 if not mirror_object:
#                     bpy.ops.object.empty_add(type='PLAIN_AXES')
#                     bpy.ops.object.location_clear(clear_delta=False)
#                     empty_for_mirror = context.active_object
#                     bpy.ops.object.select_all(action='DESELECT')
#                     context.view_layer.objects.active = act_obj
#                     act_obj.select_set(state=True)
#                     newMod.mirror_object = empty_for_mirror
#                 else:
#                     newMod.mirror_object = mirror_object
#
#         # Plane
#         elif self.primitive == 'plane':
#             if context.object is not None:
#                 bpy.ops.object.mode_set(mode='OBJECT')
#             bpy.ops.mesh.make_wplane(True)
#
#             if event.alt:
#                 context.object.show_wire = True
#                 context.object.show_all_edges = True
#
#             # Add Mirror
#             if event.ctrl and event.shift:
#                 act_obj = context.active_object
#                 newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
#                 newMod.show_on_cage = True
#                 newMod.show_in_editmode = True
#                 if not mirror_object:
#                     bpy.ops.object.empty_add(type='PLAIN_AXES')
#                     bpy.ops.object.location_clear(clear_delta=False)
#                     empty_for_mirror = context.active_object
#                     bpy.ops.object.select_all(action='DESELECT')
#                     context.view_layer.objects.active = act_obj
#                     act_obj.select_set(state=True)
#                     newMod.mirror_object = empty_for_mirror
#                 else:
#                     newMod.mirror_object = mirror_object
#
#         # Ring
#         elif self.primitive == 'ring':
#             if context.object is not None:
#                 bpy.ops.object.mode_set(mode='OBJECT')
#             bpy.ops.mesh.make_wring(True)
#             # context.object.data.WRing.seg[0] = 16
#             context.object.data.WRing.seg_perimeter = 16
#
#             if event.alt:
#                 context.object.show_wire = True
#                 context.object.show_all_edges = True
#
#             # Add Mirror
#             if event.ctrl and event.shift:
#                 act_obj = context.active_object
#                 newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
#                 newMod.show_on_cage = True
#                 newMod.show_in_editmode = True
#                 if not mirror_object:
#                     bpy.ops.object.empty_add(type='PLAIN_AXES')
#                     bpy.ops.object.location_clear(clear_delta=False)
#                     empty_for_mirror = context.active_object
#                     bpy.ops.object.select_all(action='DESELECT')
#                     context.view_layer.objects.active = act_obj
#                     act_obj.select_set(state=True)
#                     newMod.mirror_object = empty_for_mirror
#                 else:
#                     newMod.mirror_object = mirror_object
#
#         # Tube
#         elif self.primitive == 'tube':
#             if context.object is not None:
#                 bpy.ops.object.mode_set(mode='OBJECT')
#             bpy.ops.mesh.make_wtube(True)
#
#             context.object.data.WTube.seg_perimeter = 16
#
#             # context.object.data.WTube.seg[0] = 16
#             context.object.data.WTube.smooth = False
#
#             if event.alt:
#                 context.object.show_wire = True
#                 context.object.show_all_edges = True
#
#             # Add Mirror
#             if event.ctrl and event.shift:
#                 act_obj = context.active_object
#                 newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
#                 newMod.show_on_cage = True
#                 newMod.show_in_editmode = True
#                 if not mirror_object:
#                     bpy.ops.object.empty_add(type='PLAIN_AXES')
#                     bpy.ops.object.location_clear(clear_delta=False)
#                     empty_for_mirror = context.active_object
#                     bpy.ops.object.select_all(action='DESELECT')
#                     context.view_layer.objects.active = act_obj
#                     act_obj.select_set(state=True)
#                     newMod.mirror_object = empty_for_mirror
#                 else:
#                     newMod.mirror_object = mirror_object
#
#         # Sphere
#         elif self.primitive == 'sphere':
#             if context.object is not None:
#                 bpy.ops.object.mode_set(mode='OBJECT')
#             bpy.ops.mesh.make_wsphere(True)
#
#             if event.alt:
#                 context.object.show_wire = True
#                 context.object.show_all_edges = True
#
#             # Add Mirror
#             if event.ctrl and event.shift:
#                 act_obj = context.active_object
#                 newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
#                 newMod.show_on_cage = True
#                 newMod.show_in_editmode = True
#                 if not mirror_object:
#                     bpy.ops.object.empty_add(type='PLAIN_AXES')
#                     bpy.ops.object.location_clear(clear_delta=False)
#                     empty_for_mirror = bpy.context.active_object
#                     bpy.ops.object.select_all(action='DESELECT')
#                     context.view_layer.objects.active = act_obj
#                     act_obj.select_set(state=True)
#                     newMod.mirror_object = empty_for_mirror
#                 else:
#                     newMod.mirror_object = mirror_object
#
#         # Screw
#         elif self.primitive == 'screw':
#             if context.object is not None:
#                 bpy.ops.object.mode_set(mode='OBJECT')
#             bpy.ops.mesh.make_wscrew(True)
#
#             if event.alt:
#                 context.object.show_wire = True
#                 context.object.show_all_edges = True
#
#             # Add Mirror
#             if event.ctrl and event.shift:
#                 act_obj = context.active_object
#                 newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
#                 newMod.show_on_cage = True
#                 newMod.show_in_editmode = True
#                 if not mirror_object:
#                     bpy.ops.object.empty_add(type='PLAIN_AXES')
#                     bpy.ops.object.location_clear(clear_delta=False)
#                     empty_for_mirror = context.active_object
#                     bpy.ops.object.select_all(action='DESELECT')
#                     context.view_layer.objects.active = act_obj
#                     act_obj.select_set(state=True)
#                     newMod.mirror_object = empty_for_mirror
#                 else:
#                     newMod.mirror_object = mirror_object
#         # Capsule
#         elif self.primitive == 'capsule':
#             if context.object is not None:
#                 bpy.ops.object.mode_set(mode='OBJECT')
#             bpy.ops.mesh.make_wcapsule(True)
#
#             if event.alt:
#                 context.object.show_wire = True
#                 context.object.show_all_edges = True
#
#             # Add Mirror
#             if event.ctrl and event.shift:
#                 act_obj = context.active_object
#                 newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
#                 newMod.show_on_cage = True
#                 newMod.show_in_editmode = True
#                 if not mirror_object:
#                     bpy.ops.object.empty_add(type='PLAIN_AXES')
#                     bpy.ops.object.location_clear(clear_delta=False)
#                     empty_for_mirror = context.active_object
#                     bpy.ops.object.select_all(action='DESELECT')
#                     context.view_layer.objects.active = act_obj
#                     act_obj.select_set(state=True)
#                     newMod.mirror_object = empty_for_mirror
#                 else:
#                     newMod.mirror_object = mirror_object
#
#         # Torus
#         elif self.primitive == 'torus':
#             if context.object is not None:
#                 bpy.ops.object.mode_set(mode='OBJECT')
#             bpy.ops.mesh.make_wtorus(True)
#
#             if event.alt:
#                 context.object.show_wire = True
#                 context.object.show_all_edges = True
#
#             # Add Mirror
#             if event.ctrl and event.shift:
#                 act_obj = context.active_object
#                 newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
#                 newMod.show_on_cage = True
#                 newMod.show_in_editmode = True
#                 if not mirror_object:
#                     bpy.ops.object.empty_add(type='PLAIN_AXES')
#                     bpy.ops.object.location_clear(clear_delta=False)
#                     empty_for_mirror = context.active_object
#                     bpy.ops.object.select_all(action='DESELECT')
#                     context.view_layer.objects.active = act_obj
#                     act_obj.select_set(state=True)
#                     newMod.mirror_object = empty_for_mirror
#                 else:
#                     newMod.mirror_object = mirror_object
#
#         # Cone
#         elif self.primitive == 'cone':
#             if context.object is not None:
#                 bpy.ops.object.mode_set(mode='OBJECT')
#             bpy.ops.mesh.make_wcone(True)
#
#             if event.alt:
#                 context.object.show_wire = True
#                 context.object.show_all_edges = True
#
#             # Add Mirror
#             if event.ctrl and event.shift:
#                 act_obj = context.active_object
#                 newMod = act_obj.modifiers.new("Mirror", 'MIRROR')
#                 newMod.show_on_cage = True
#                 newMod.show_in_editmode = True
#                 if not mirror_object:
#                     bpy.ops.object.empty_add(type='PLAIN_AXES')
#                     bpy.ops.object.location_clear(clear_delta=False)
#                     empty_for_mirror = context.active_object
#                     bpy.ops.object.select_all(action='DESELECT')
#                     context.view_layer.objects.active = act_obj
#                     act_obj.select_set(state=True)
#                     newMod.mirror_object = empty_for_mirror
#                 else:
#                     newMod.mirror_object = mirror_object
#
#         if event.ctrl:
#             bpy.ops.transform.translate('INVOKE_DEFAULT')
#
#         context.scene.cursor.location = saved_location
#         return {"FINISHED"}
#
# class RMB_Apply_Wonder_Mesh(bpy.types.Operator):
#     bl_idname = 'object.rmb_apply_wonder_mesh'
#     bl_label = "Apply wonder Mesh Primitives"
#     bl_options = {'REGISTER'}
#
#     @classmethod
#     def poll(cls, context):
#         return True
#
#     def execute(self, context):
#         bpy.ops.mesh.convert_w_mesh()
#         # self.report({'INFO'}, "Wonder Mesh Applied")
#         return {'FINISHED'}


#Knife tool
class WAZOU_RMB_PIE_MENUS_OT_knife_tools(bpy.types.Operator):
    """    KNIFE TOOL

    CLICK - Knife Tool
    SHIFT - Knife Cut Throught the Mesh
    """
    bl_idname = "wazou_rmb_pie_menus.knife_tools"
    bl_label = "knife Tools"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if context.object.mode == "EDIT"]) == 1:
            return True

    def invoke(self, context, event):
        obj = context.active_object

        if event.shift:
            bpy.ops.mesh.knife_tool('INVOKE_DEFAULT', True, use_occlude_geometry=False, only_selected=False)
            if event.ctrl:
                bpy.ops.mesh.knife_tool('INVOKE_DEFAULT', True, use_occlude_geometry=True, only_selected=True)
        else:
            bpy.ops.mesh.knife_tool('INVOKE_DEFAULT', True, use_occlude_geometry=True, only_selected=False)
        return {"FINISHED"}

#Imports/Exports
class WAZOU_RMB_PIE_MENUS_OT_import_exports(bpy.types.Operator):
    """    IMPORT/EXPORT

    CLICK - Import
    SHIFT - Export
    """
    bl_idname = "wazou_rmb_pie_menus.import_exports"
    bl_label = "Rmb Import Exports"
    bl_options = {"REGISTER"}


    import_exports : EnumProperty(
        items = (('obj', "OBJ", ""),
                 ('fbx', "FBX", ""),
                 ('stl', "STL", ""),
                 ('abc', "ABC", "")),
                 default = 'abc'
                 )

    def invoke(self, context, event):
        obj = context.active_object
        wm = context.window_manager
#
#        RMBimport = {'obj': bpy.ops.import_scene.obj('INVOKE_DEFAULT'),
#                     'fbx': bpy.ops.import_scene.fbx('INVOKE_DEFAULT'),
#                     'stl': bpy.ops.import_mesh.stl('INVOKE_DEFAULT'),
#                     'abc':bpy.ops.wm.alembic_import('INVOKE_DEFAULT'),
#                     }
#
#        RMBexport = {'obj': bpy.ops.export_scene.obj('INVOKE_DEFAULT'),
#                     'fbx': bpy.ops.export_scene.fbx('INVOKE_DEFAULT'),
#                     'stl': bpy.ops.export_mesh.stl('INVOKE_DEFAULT'),
#                     'abc':bpy.ops.wm.alembic_export('INVOKE_DEFAULT'),
#                     }
#
#        if event.shift:
#            RMBexport[self.import_exports]
#
#        else:
#            RMBimport[self.import_exports]

        #OBJ
        if self.import_exports == 'obj':
            if event.shift:
                bpy.ops.export_scene.obj('INVOKE_DEFAULT')
            else:
                bpy.ops.import_scene.obj('INVOKE_DEFAULT')

        #FBX
        elif self.import_exports == 'fbx':
            if event.shift:
                bpy.ops.export_scene.fbx('INVOKE_DEFAULT')
            else:
                bpy.ops.import_scene.fbx('INVOKE_DEFAULT')

        #STL
        elif self.import_exports == 'stl':
            if event.shift:
                bpy.ops.export_mesh.stl('INVOKE_DEFAULT')
            else:
                bpy.ops.import_mesh.stl('INVOKE_DEFAULT')

        #ABC
        elif self.import_exports == 'abc':
            if event.shift:
                bpy.ops.wm.alembic_export('INVOKE_DEFAULT')
            else:
                bpy.ops.wm.alembic_import('INVOKE_DEFAULT')

        return {"FINISHED"}

#Offset_Edges
class WAZOU_RMB_PIE_MENUS_OT_offset_edges(bpy.types.Operator):
    """    OFFSET EDGES

    CLICK - Extrude
    SHIFT - Move
    CTRL  - Offset
    ALT    - Profile
    """
    bl_idname = "wazou_rmb_pie_menus.offset_edges"
    bl_label = "Offset Edges"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if context.object.mode == "EDIT"]) == 1:
            return True

    def invoke(self, context, event):
        obj = context.active_object
        if event.shift:
            bpy.ops.mesh.offset_edges('INVOKE_DEFAULT',True,caches_valid=False, geometry_mode='move')

        elif event.ctrl:
            bpy.ops.mesh.offset_edges('INVOKE_DEFAULT',True,caches_valid=False, geometry_mode='offset')

        elif event.alt:
            if len([obj for obj in context.selected_objects if context.object is not None if obj.type in ['MESH','CURVE'] if context.object.mode == "EDIT"]) == 2:
                bpy.ops.mesh.offset_edges_profile('INVOKE_DEFAULT',True)
            # else:
                # self.report({'INFO'},"Select a Curve and an edge")

        else:
            bpy.ops.mesh.offset_edges('INVOKE_DEFAULT',True,caches_valid=False, geometry_mode='extrude')

        return {"FINISHED"}

#Shrink Fatten
class WAZOU_RMB_PIE_MENUS_OT_shrink_fatten(bpy.types.Operator):
    """    SHRINK/FATTEN

    CLICK - Even Offset ON
    SHIFT - Even Offset OFF
    """
    bl_idname = "wazou_rmb_pie_menus.shrink_fatten"
    bl_label = "Rmb Shrink Fatten"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if context.object.mode == "EDIT"]) == 1:
            return True

    def invoke(self, context, event):
        if event.shift:
            bpy.ops.transform.shrink_fatten('INVOKE_DEFAULT',True, use_even_offset=False, mirror=False,
                                            use_proportional_edit=False, proportional_edit_falloff='SMOOTH',
                                            proportional_size=1, use_proportional_connected=False,
                                            use_proportional_projected=False)

        else:
            bpy.ops.transform.shrink_fatten('INVOKE_DEFAULT', True, use_even_offset=True, mirror=False,
                                            use_proportional_edit=False, proportional_edit_falloff='SMOOTH',
                                            proportional_size=1, use_proportional_connected=False,
                                            use_proportional_projected=False)

        return {"FINISHED"}

# #Edges_Loop_Slide
# class WAZOU_RMB_PIE_MENUS_OT_edges_loop_slide(bpy.types.Operator):
#     """    EDGES LOOP SLIDE
#
#     CLICK - Use Even ON
#     SHIFT - Use Even OFF
#     """
#     bl_idname = "wazou_rmb_pie_menus.edges_loopslide"
#     bl_label = "Edges Loop slide"
#     bl_options = {"REGISTER"}
#
#     @classmethod
#     def poll(cls, context):
#         obj = context.active_object
#         if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if context.object.mode == "EDIT"]) == 1:
#             return True
#
#     def invoke(self, context, event):
#         if event.shift:
#             bpy.ops.mesh.offset_edge_loops_slide('INVOKE_DEFAULT',True, MESH_OT_offset_edge_loops={"use_cap_endpoint":False}, TRANSFORM_OT_edge_slide={ "use_even":False})
#
#         else:
#             bpy.ops.mesh.offset_edge_loops_slide('INVOKE_DEFAULT',True, MESH_OT_offset_edge_loops={"use_cap_endpoint":False}, TRANSFORM_OT_edge_slide={ "use_even":True})
#
#         return {"FINISHED"}


#Spin
class WAZOU_RMB_PIE_MENUS_OT_spin(bpy.types.Operator):
    """    SPIN

    CLICK - Spin at  90°
    SHIFT - Spin at -90°
    """
    bl_idname = "wazou_rmb_pie_menus.spin"
    bl_label = "Spin"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if context.object.mode == "EDIT"]) == 1:
            return True

    def invoke(self, context, event):

        if event.shift:
            bpy.ops.mesh.spin('INVOKE_DEFAULT',True, steps=10, angle=-1.5708)
        else:
            bpy.ops.mesh.spin('INVOKE_DEFAULT',True, steps=10, angle=1.5708)

        bpy.ops.view3d.snap_cursor_to_selected()
        return {"FINISHED"}

#Merge
class WAZOU_RMB_PIE_MENUS_OT_smart_merge(bpy.types.Operator):
    """    MERGE

    CLICK - Merge at CENTER
    SHIFT - Merge at FIRST
    CTRL  - Merge at LAST
    ALT    - Merge at CURSOR
    CTRL+SHIFT - COLLAPSE
    CTRL+OSKEY - Smart MERGE
    """
    bl_idname = "wazou_rmb_pie_menus.smart_merge"
    bl_label = "RMB Smart Merge"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if context.object.mode == "EDIT"]) == 1:
            return True

    def invoke(self, context, event):
        obj = context.active_object

        #Collapse
        if event.ctrl and event.shift:
            bpy.ops.mesh.merge(type='COLLAPSE', uvs=True)


        #Collapse
        elif event.ctrl and event.oskey:
            if not tuple (context.tool_settings.mesh_select_mode) == (True, False, False) :
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            bpy.ops.object.smart_merge_tool_raycast('INVOKE_DEFAULT')

        #At First
        elif event.shift:

            if tuple (context.tool_settings.mesh_select_mode) != (True, False, False) :
                bpy.ops.mesh.merge(type='CENTER', uvs=True)
            else:
                bpy.ops.mesh.merge(type='FIRST', uvs=True)

        #At Last
        elif event.ctrl:
            if tuple (context.tool_settings.mesh_select_mode) != (True, False, False) :
                bpy.ops.mesh.merge(type='CENTER', uvs=True)

            else:
                bpy.ops.mesh.merge(type='LAST', uvs=True)

        #At cursor
        elif event.alt:
            bpy.ops.mesh.merge(type='CURSOR', uvs=True)

        #Center
        else:
            bpy.ops.mesh.merge(type='CENTER', uvs=True)

        return {"FINISHED"}

#=======================================
#  Code by Andreas Strømberg
#=======================================
# def draw_callback_px(self, context):
#     # 50% alpha, 2 pixel width line
#     bgl.glEnable(bgl.GL_BLEND)
#     bgl.glColor4f(1.0, 1.0, 1.0, 1.0)
#     bgl.glLineWidth(4)
#
#     bgl.glBegin(bgl.GL_LINES)
#     if self.started:
#         bgl.glVertex2i(self.start_vertex[0], self.start_vertex[1])
#         bgl.glVertex2i(self.end_vertex[0], self.end_vertex[1])
#
#     bgl.glEnd()
#
#     # restore opengl defaults
#     bgl.glLineWidth(1)
#     bgl.glDisable(bgl.GL_BLEND)
#     bgl.glColor4f(0.0, 0.0, 0.0, 1.0)


def main(context, event, started):
    """Run this function on left mouse, execute the ray cast"""
    coord = event.mouse_region_x, event.mouse_region_y

    if started:
        result = bpy.ops.view3d.select(extend=True, location=coord)
    else:
        result = bpy.ops.view3d.select(extend=False, location=coord)

    if result == {'PASS_THROUGH'}:
        bpy.ops.mesh.select_all(action='DESELECT')


class WAZOU_RMB_PIE_MENUS_OT_smart_merge_tool_raycast(bpy.types.Operator):
    """Modal object selection with a ray cast"""
    bl_idname = "object.smart_merge_tool_raycast"
    bl_label = "Merge Tool Operator"
    bl_options = {'REGISTER'}

    def __init__(self):
        self.started = None
        self.start_vertex = None
        self.end_vertex = None
#        self._handle = None

    def modal(self, context, event):
        context.area.tag_redraw()

        if event.type in {'MIDDLEMOUSE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE', 'ALT'}:
            # allow navigation
            return {'PASS_THROUGH'}

        elif event.type == 'MOUSEMOVE':
            if self.started:
                self.end_vertex = (event.mouse_region_x, event.mouse_region_y)

        elif event.type == 'LEFTMOUSE':
            main(context, event, self.started)
            if not self.started:
                if context.object.data.total_vert_sel == 1:
                    self.start_vertex = (event.mouse_region_x, event.mouse_region_y)
                    self.end_vertex = (event.mouse_region_x, event.mouse_region_y)
                    self.started = True

            elif context.object.data.total_vert_sel == 2:
                if event.ctrl:
                    bpy.ops.mesh.vert_connect_path()
                else:
                    my_type = 'CENTER' if event.shift else 'LAST'
                    bpy.ops.mesh.merge(type=my_type)

                self.started = False

            return {'RUNNING_MODAL'}

        elif event.type == 'SPACE':
            self.started = False

        elif event.type in {'RIGHTMOUSE', 'ESC', 'SPACE'}:
            #Remove Informations
            context.area.header_text_set()
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.space_data.type == 'VIEW_3D':
            args = (self, context)

            self.start_vertex = (0, 0)
            self.end_vertex = (0, 0)

            # context.window_manager.modal_handler_add(self)
            # self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px, args, 'WINDOW', 'POST_PIXEL')

            self.started = False
            #Informations
            context.area.header_text_set("Click: Continuos Merge, Drag+Click: Merge, Shift: At Center, Space: Restart Auto Merge, RMB/ESC: Exit")
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "Active space must be a View3d")
            return {'CANCELLED'}

#Connect
class WAZOU_RMB_PIE_MENUS_OT_smart_connect(bpy.types.Operator):
    """    CONNECT

    CLICK - Connect
    SHIFT - Smart Connect
    """
    bl_idname = "wazou_rmb_pie_menus.smart_connect"
    bl_label = "RMB Smart Connect"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if context.object.mode == "EDIT"]) == 1:
            return True

    def invoke(self, context, event):
        obj = context.active_object

        #Connect Raycast
        if event.shift:
            if not tuple (context.tool_settings.mesh_select_mode) == (True, False, False) :
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')

            bpy.ops.object.smart_connect_tool_raycast('INVOKE_DEFAULT')

        #Normal connect
        else:
            if not tuple (context.tool_settings.mesh_select_mode) == (True, False, False) :
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                bpy.ops.mesh.select_all(action='DESELECT')

            if context.object.data.total_vert_sel > 1:
                bpy.ops.mesh.vert_connect_path()
            else:
                bpy.ops.object.smart_connect_tool_raycast('INVOKE_DEFAULT')


        return {"FINISHED"}

#Connect modal
class WAZOU_RMB_PIE_MENUS_OT_smart_connect_tool_raycast(bpy.types.Operator):
    """Modal object selection with a ray cast"""
    bl_idname = "object.smart_connect_tool_raycast"
    bl_label = "Smart Connect Tool Operator"
    bl_options = {'REGISTER'}

    def __init__(self):
        self.started = None
        self.start_vertex = None
        self.end_vertex = None
        self._handle = None

    def modal(self, context, event):
        context.area.tag_redraw()

        if event.type in {'MIDDLEMOUSE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE'}:
            return {'PASS_THROUGH'}

        elif event.type == 'MOUSEMOVE':
            if self.started:
                self.end_vertex = (event.mouse_region_x, event.mouse_region_y)

        elif event.type == 'LEFTMOUSE':
            main(context, event, self.started)
            if not self.started:
                if context.object.data.total_vert_sel == 1:
                    self.start_vertex = (event.mouse_region_x, event.mouse_region_y)
                    self.end_vertex = (event.mouse_region_x, event.mouse_region_y)
                    self.started = True
            elif context.object.data.total_vert_sel == 2:

                if event.ctrl:
                    bpy.ops.mesh.merge(type='CENTER', uvs=True)
                else:
                    bpy.ops.mesh.vert_connect_path()
                if event.shift:
                    bpy.ops.mesh.merge(type='LAST', uvs=True)

                bpy.ops.ed.undo_push(message="Add an undo step *function may be moved*")
                self.started = False

            return {'RUNNING_MODAL'}

        elif event.type == 'SPACE':
            self.started = False


        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            context.area.header_text_set()
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.space_data.type == 'VIEW_3D':
            args = (self, context)

            self.start_vertex = (0, 0)
            self.end_vertex = (0, 0)

            # context.window_manager.modal_handler_add(self)
            # self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px, args, 'WINDOW', 'POST_PIXEL')
            context.area.header_text_set("Click: Continuos Connect, Drag+Click: Connect, Shift+Click: merge at Last, Ctrl+Click: Merge at Center, Space: Restart Auto Connect, RMB/ESC: Exit")
            self.started = False
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "Active space must be a View3d")
            return {'CANCELLED'}

#Looptools
class WAZOU_RMB_PIE_MENUS_OT_smart_loops_modal(bpy.types.Operator):
    bl_idname = "object.smart_loops_modal"
    bl_label = "RMB Smart Loops Modal"
    bl_options = {'REGISTER'}

    active : bpy.props.BoolProperty(name="active", default=False)

    @classmethod
    def poll(cls, context):

        return bpy.ops.mesh.loopcut_slide.poll()

    def modal(self, context, event):
        if event.type == 'MIDDLEMOUSE':
            return {'PASS_THROUGH'}

        if event.type in {'RIGHTMOUSE', 'ESC', 'SPACE'}:
            context.area.header_text_set()
            return {'CANCELLED'}

        elif event.type == 'LEFTMOUSE' and event.value == 'RELEASE':
            self.active = False

        if not self.active:
            self.active = True
            bpy.ops.mesh.loopcut_slide('INVOKE_DEFAULT', True)
            context.area.header_text_set("Press ESC/RMB To Exit")

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

#subdivide smooth
class WAZOU_RMB_PIE_MENUS_OT_subdivide_smooth(bpy.types.Operator):
    """    SUBDIVIDE

    CLICK - Subdivide
    SHIFT - Subdivide Smooth
    CTRL  - Subdivide Smooth 5 Cuts
    ALT    - Subdivide Smooth 10 Cuts
    """
    bl_idname = "wazou_rmb_pie_menus.subdivide_smooth"
    bl_label = "Subdivide Smooth"
    bl_options = {"REGISTER"}

    def invoke(self, context, event):

        if event.shift:
            bpy.ops.mesh.subdivide(True, smoothness=1)

        elif event.ctrl:
            bpy.ops.mesh.subdivide(True, number_cuts=5, smoothness=1)

        elif event.alt:
            bpy.ops.mesh.subdivide(True, number_cuts=10, smoothness=1)

        else:
            bpy.ops.mesh.subdivide(True, smoothness=0)

        return {"FINISHED"}


#Looptools
class WAZOU_RMB_PIE_MENUS_OT_smart_loops(bpy.types.Operator):
    """    SMART LOOPS

    CLICK - Add Loops
    SHIFT - Continuous Loops
    """
    bl_idname = "wazou_rmb_pie_menus.smart_loops"
    bl_label = "Rmb Smart Loops"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if context.object.mode == "EDIT"]) == 1:
            return True

    def invoke(self, context, event):
        obj = context.active_object

        #smart loops
        if event.shift:
            if not tuple (context.tool_settings.mesh_select_mode) == (False, True, False) :
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')

            bpy.ops.object.smart_loops_modal('INVOKE_DEFAULT', True)

        #Normal loops
        else:
            bpy.ops.mesh.loopcut_slide('INVOKE_DEFAULT',True)

        return {"FINISHED"}

#align
selection = list()
class WAZOU_RMB_PIE_MENUS_OT_align_selection(bpy.types.Operator):
    """    ALIGN TO GRID

    CLICK - Align to X
    SHIFT - Align to Y
    CTRL  - Align to Z
    ALT    - Align to Center in Object Mode
    """
    bl_idname = "wazou_rmb_pie_menus.align_selection"
    bl_label = "Rmb Align Selection"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if obj.type == 'MESH' :
            return True

    def invoke(self, context, event):
        obj = context.active_object
        act_obj = context.active_object.name
        saved_location = context.scene.cursor.location.copy()

#        align_axis = 'X' if event.shift = 'Y' elif event.ctrl = 'Z' else
#        bpy.ops.mesh.merge(type=my_type)


        for obj in context.selected_objects:
            selection.append(obj)

        #Y
        if event.shift:
            if context.object.mode == "EDIT":
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.view3d.snap_cursor_to_active()
                saved_location_object = context.scene.cursor.location.copy()
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

                bpy.ops.object.transform_apply(location=True, rotation=True, scale=False)


                context.scene.cursor.location[0] = 0
                context.scene.cursor.location[1] = 0
                context.scene.cursor.location[2] = 0

                for vert in context.object.data.vertices:
                    if vert.select:
                        vert.co[1] = 0

                context.scene.cursor.location = saved_location_object
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                context.scene.cursor.location = saved_location
                bpy.ops.object.mode_set(mode = 'EDIT')
            else:
                for obj in context.selected_objects:
                    context.view_layer.objects.active = obj
                    obj.select_set(state=True)
                    context.object.location[1] = 0
                for obj in selection:
                    obj.select_set(state=True)
                    context.view_layer.objects.active = bpy.data.objects[act_obj]

        #Z
        elif event.ctrl:
            if context.object.mode == "EDIT":
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.view3d.snap_cursor_to_active()
                saved_location_object = context.scene.cursor.location.copy()
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

                bpy.ops.object.transform_apply(location=True, rotation=True, scale=False)

                context.scene.cursor.location[0] = 0
                context.scene.cursor.location[1] = 0
                context.scene.cursor.location[2] = 0

                for vert in context.object.data.vertices:
                    if vert.select:
                        vert.co[2] = 0

                context.scene.cursor.location = saved_location_object
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                context.scene.cursor.location = saved_location
                bpy.ops.object.mode_set(mode = 'EDIT')
            else:
                for obj in context.selected_objects:
                    context.view_layer.objects.active = obj
                    obj.select_set(state=True)
                    context.object.location[2] = 0
                for obj in selection:
                    obj.select_set(state=True)
                    context.view_layer.objects.active = bpy.data.objects[act_obj]

        #Z
        elif event.alt:
            for obj in context.selected_objects:
                context.view_layer.objects.active = obj
                obj.select_set(state=True)
                context.object.location[0] = 0
                context.object.location[1] = 0
                context.object.location[2] = 0
            for obj in selection:
                obj.select_set(state=True)
                context.view_layer.objects.active = bpy.data.objects[act_obj]

        #X
        else:
            if context.object.mode == "EDIT":
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.view3d.snap_cursor_to_active()
                saved_location_object = context.scene.cursor.location.copy()
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

                bpy.ops.object.transform_apply(location=True, rotation=True, scale=False)

                context.scene.cursor.location[0] = 0
                context.scene.cursor.location[1] = 0
                context.scene.cursor.location[2] = 0

                for vert in context.object.data.vertices:
                    if vert.select:
                        vert.co[0] = 0

                context.scene.cursor.location = saved_location_object
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                context.scene.cursor.location = saved_location
                bpy.ops.object.mode_set(mode = 'EDIT')
            else:
                for obj in context.selected_objects:
                    context.view_layer.objects.active = obj
                    obj.select_set(state=True)
                    context.object.location[0] = 0

                for obj in selection:
                    obj.select_set(state=True)
                    context.view_layer.objects.active = bpy.data.objects[act_obj]

        del(selection[:])
        return {"FINISHED"}



#Normals
class WAZOU_RMB_PIE_MENUS_OT_normals(bpy.types.Operator):
    """    NORMALS

    CLICK - Flip Normals
    SHIFT - Recalculate Outside
    CTRL  - Recalculate Inside
    ALT    - Show Normals
    """
    bl_idname = "wazou_rmb_pie_menus.normals"
    bl_label = "Rmb Normals"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if context.object.mode == "EDIT"]) == 1:
            return True

    def invoke(self, context, event):

        if event.shift:
            bpy.ops.mesh.normals_make_consistent(inside=True)

        if event.ctrl:
            bpy.ops.mesh.normals_make_consistent(inside=False)

        if event.alt:
            if context.space_data.overlay.show_curve_normals  == False :
                context.space_data.overlay.show_curve_normals = True
            else:
                context.space_data.overlay.show_curve_normals = False

        else:
            bpy.ops.mesh.flip_normals()

        return {"FINISHED"}

#Smooth/Relax
class WAZOU_RMB_PIE_MENUS_OT_smooth_relax(bpy.types.Operator):
    """    SMOOTH/RELAX

    CLICK - Smooth
    SHIFT - Relax

    """
    bl_idname = "wazou_rmb_pie_menus.smooth_relax"
    bl_label = "Rmb Smooth Relax"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if len([obj for obj in context.selected_objects if context.object is not None if obj.type == 'MESH' if context.object.mode == "EDIT"]) == 1:
            return True

    def invoke(self, context, event):
        self.use_modals = get_addon_preferences().use_modals

        if event.shift:
            bpy.ops.object.rmb_lap_relax()

        else:
            if not self.use_modals:
#            if (2, 77, 5) < bpy.app.version:
                bpy.ops.mesh.vertices_smooth('INVOKE_DEFAULT', True)
            else:
                bpy.ops.object.rmb_modal_smooth('INVOKE_DEFAULT', True)

        return {"FINISHED"}

class WAZOU_RMB_PIE_MENUS_OT_laprelax(bpy.types.Operator):
    bl_idname = "object.rmb_lap_relax"
    bl_label = "Rmb Smooth Lap Relax"
    bl_description = ""
    bl_options = {"REGISTER"}

    Repeat : bpy.props.IntProperty(
        name = "Repeat",
        description = "Repeat how many times",
        default = 5,
        min = 1,
        max = 100)

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj and obj.type == 'MESH' and context.mode == 'EDIT_MESH')

    def do_laprelax(self):

        context = bpy.context
        region = bpy.context.region
        area = bpy.context.area
        selobj = bpy.context.active_object
        mesh = selobj.data
        bm = bmesh.from_edit_mesh(mesh)
        bmprev = bm.copy()
        vertices = [v for v in bmprev.verts if v.select]

        for v in bmprev.verts:
            if v.select:
                tot = Vector((0, 0, 0))
                cnt = 0
                for e in v.link_edges:
                    for f in e.link_faces:
                        if not(f.select):
                            cnt = 1
                    if len(e.link_faces) == 1:
                        cnt = 1
                        break
                if cnt:
                    # dont affect border edges: they cause shrinkage
                    continue

                # find Laplacian mean
                for e in v.link_edges:
                    tot += e.other_vert(v).co
                tot /= len(v.link_edges)

                # cancel movement in direction of vertex normal
                delta = (tot - v.co)
                if delta.length != 0:
                    ang = delta.angle(v.normal)
                    deltanor = math.cos(ang) * delta.length
                    nor = v.normal
                    nor.length = abs(deltanor)
                    bm.verts.ensure_lookup_table()
                    bm.verts[v.index].co = tot + nor


        mesh.update()
        bm.free()
        bmprev.free()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

#    def invoke(self, context, event):
    def execute(self, context):

        # smooth #Repeat times
        for i in range(self.Repeat):
            self.do_laprelax()

        return {'FINISHED'}
#Cursor
class WAZOU_RMB_PIE_MENUS_OT_cursor(bpy.types.Operator):
    """    CURSOR
    
    CLICK - Cursor to Selected
    SHIFT - Selection to Cursor
    CTRL  - Cursor to CENTER
    ALT    - Cursor to ACTIVE
    CTRL+SHIFT - Cursor to Selection > Object Mode
    CTRL+ALT    - Selection to Cursor Offset
    """
    bl_idname = "wazou_rmb_pie_menus.cursor"
    bl_label = "Rmb Cursor"
    bl_options = {"REGISTER"}

    def invoke(self, context, event):
        
        if event.ctrl and event.shift:
            bpy.ops.view3d.snap_cursor_to_selected()
            bpy.ops.object.mode_set(mode = 'OBJECT')
       
        elif event.ctrl and event.alt:
            bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)

        elif event.shift:
            bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
        
        elif event.ctrl:
            bpy.ops.view3d.snap_cursor_to_center()
        
        elif event.alt:
            bpy.ops.view3d.snap_cursor_to_active()
        
        else:
            bpy.ops.view3d.snap_cursor_to_selected()

        return {"FINISHED"}

#Origin
selection = list() 
class WAZOU_RMB_PIE_MENUS_OT_origin(bpy.types.Operator):
    """    ORIGIN
    
    CLICK - Origin to Selection
    SHIFT - Origin to Cursor
    CTRL  - Geometry to Origin
    ALT    - Origin to Geometry
    CTRL+SHIFT - Origin to Center Of Mass
    CTRL+ALT    - Origin to Bottom
    """
    bl_idname = "wazou_rmb_pie_menus.origin"
    bl_label = "Rmb Origin"
    bl_options = {"REGISTER"}

    def invoke(self, context, event):
        wm = context.window_manager
#        wm.act_obj = context.active_object.name
        act_obj = context.active_object
        
        if event.ctrl and event.shift:
            #Origin To Center Of Mass
            for obj in context.selected_objects :
                bpy.ops.object.mode_set(mode = 'OBJECT')
                context.view_layer.objects.active=obj
                obj.select_set(state=True)
                bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
#                context.view_layer.objects.active = bpy.data.objects[wm.act_obj]
                context.view_layer.objects.active = act_obj
    
        elif event.ctrl and event.alt:
            #Origin To Bottom 
            for obj in context.selected_objects :
                selection.append(obj)
                context.view_layer.objects.active=obj
                obj.select_set(state=True)
            
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
                o=context.active_object
                init=0
                for x in o.data.vertices:
                     if init==0:
                         a=x.co.z
                         init=1
                     elif x.co.z<a:
                         a=x.co.z
                         
                for x in o.data.vertices:
                     x.co.z-=a

                o.location.z+=a 
                bpy.ops.object.select_all(action='DESELECT')

            for obj in selection :
                obj.select_set(state=True)
#                context.view_layer.objects.active = bpy.data.objects[wm.act_obj]
                context.view_layer.objects.active = act_obj
                
        elif event.shift:
            #To Cursor
            if context.object.mode == "EDIT":
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                bpy.ops.object.mode_set(mode = 'EDIT')
            else:
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR') 
                
        elif event.ctrl:
            #To Geometry
            if context.object.mode == "EDIT":
                bpy.ops.object.mode_set(mode = 'OBJECT')
                
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            
        
        elif event.alt:
            #Geometry To Origin
            bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
            
            
        else:
            #si len>1 cursor to active
            if len([obj for obj in context.selected_objects]) >= 2: 
                bpy.ops.view3d.snap_cursor_to_active()
                act_obj = context.active_object 

                act_obj.select_set(state=False)
                for obj in context.selected_objects :
                    context.view_layer.objects.active=obj
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            
            else:
                if context.object.mode == "EDIT":
                    bpy.ops.view3d.snap_cursor_to_selected()
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                else:
                    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            
        del(selection[:])
        return {"FINISHED"}

# #Remove double
# class WAZOU_RMB_PIE_MENUS_OT_remove_double(bpy.types.Operator):
#     """    REMOVE DOUBLE
#
#     CLICK - Remove Double on Selected Vertices
#     SHIFT - Select All and Remove Double
#     """
#     bl_idname = 'object.rmb_remove_double'
#     bl_label = "Remove Double"
#     bl_options = {'REGISTER'}
#
#     @classmethod
#     def poll(cls, context):
#         obj = context.active_object
#         return (obj and obj.type == 'MESH' and context.mode == 'EDIT_MESH')
#
#     def invoke(self, context, event):
#
#         if event.shift:
#             bpy.ops.mesh.select_all(action='SELECT')
#             bpy.ops.mesh.remove_doubles('INVOKE_DEFAULT', True)
#         else:
#             bpy.ops.mesh.remove_doubles('INVOKE_DEFAULT', True)
#
#
#         return {'FINISHED'}

#Bridge
class WAZOU_RMB_PIE_MENUS_OT_bridge(bpy.types.Operator):
    """    BRIDGE

    CLICK - Bridge
    SHIFT - Merge Bridge
    """
    bl_idname = 'wazou_rmb_pie_menus.bridge'
    bl_label = "Bridge"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return True

    def invoke(self, context, event):

        if event.shift:
            bpy.ops.mesh.bridge_edge_loops(True, use_merge=True, merge_factor=0.5, number_cuts=0, smoothness=0,
                                           profile_shape_factor=0)

        else:
            bpy.ops.mesh.bridge_edge_loops(True, use_merge=False, merge_factor=0.5, number_cuts=0, smoothness=0,
                                           profile_shape_factor=0)

        return {'FINISHED'}



CLASSES =  [#WAZOU_RMB_PIE_MENUS_OT_import_image_as_brush,
            WAZOU_RMB_PIE_MENUS_OT_particle_path_steps,
            WAZOU_RMB_PIE_MENUS_OT_particle_childrens,
            WAZOU_RMB_PIE_MENUS_OT_particle_length,
            WAZOU_RMB_PIE_MENUS_OT_particle_x_mirror,
            WAZOU_RMB_PIE_MENUS_OT_particle_root,
            WAZOU_RMB_PIE_MENUS_OT_selection_particles_mode,
            WAZOU_RMB_PIE_MENUS_OT_selection_particles_brushes,
            WAZOU_RMB_PIE_MENUS_OT_particles_interpolate,
            WAZOU_RMB_PIE_MENUS_OT_copy_custom_orientation,
            WAZOU_RMB_PIE_MENUS_OT_looptools_circle,
            WAZOU_RMB_PIE_MENUS_OT_looptools_flatten,
            WAZOU_RMB_PIE_MENUS_OT_looptools_relax,
            WAZOU_RMB_PIE_MENUS_OT_looptools_space,
            WAZOU_RMB_PIE_MENUS_OT_looptools_gstretch,
            WAZOU_RMB_PIE_MENUS_OT_equalize_edges_length,
            WAZOU_RMB_PIE_MENUS_OT_align_space,
            WAZOU_RMB_PIE_MENUS_OT_auto_mirror,
            WAZOU_RMB_PIE_MENUS_OT_create_hole,
            WAZOU_RMB_PIE_MENUS_OT_apply_transforms,
            WAZOU_RMB_PIE_MENUS_OT_mark_clear_seam,
            WAZOU_RMB_PIE_MENUS_OT_unwrap,
            WAZOU_RMB_PIE_MENUS_OT_simplify_circle,
            WAZOU_RMB_PIE_MENUS_OT_extract_duplicate,
            WAZOU_RMB_PIE_MENUS_OT_inset_poke_faces,
            WAZOU_RMB_PIE_MENUS_OT_subsurf_operator,
            WAZOU_RMB_PIE_MENUS_OT_apply_remove_modifiers,
            WAZOU_RMB_PIE_MENUS_OT_knurl,
            # WAZOU_RMB_PIE_MENUS_OT_select_hierarchy,
            WAZOU_RMB_PIE_MENUS_OT_parent_objects,
            # WAZOU_RMB_PIE_MENUS_OT_add_empty_image,
            WAZOU_RMB_PIE_MENUS_OT_primitives,
            WAZOU_RMB_PIE_MENUS_OT_knife_tools,
            WAZOU_RMB_PIE_MENUS_OT_import_exports,
            WAZOU_RMB_PIE_MENUS_OT_offset_edges,
            WAZOU_RMB_PIE_MENUS_OT_shrink_fatten,
            WAZOU_RMB_PIE_MENUS_OT_spin,
            WAZOU_RMB_PIE_MENUS_OT_smart_merge,
            WAZOU_RMB_PIE_MENUS_OT_smart_merge_tool_raycast,
            WAZOU_RMB_PIE_MENUS_OT_smart_connect,
            WAZOU_RMB_PIE_MENUS_OT_smart_connect_tool_raycast,
            WAZOU_RMB_PIE_MENUS_OT_smart_loops_modal,
            WAZOU_RMB_PIE_MENUS_OT_subdivide_smooth,
            WAZOU_RMB_PIE_MENUS_OT_smart_loops,
            WAZOU_RMB_PIE_MENUS_OT_align_selection,
            WAZOU_RMB_PIE_MENUS_OT_normals,
            WAZOU_RMB_PIE_MENUS_OT_smooth_relax,
            WAZOU_RMB_PIE_MENUS_OT_cursor,
            WAZOU_RMB_PIE_MENUS_OT_origin,
            WAZOU_RMB_PIE_MENUS_OT_bridge,
            WAZOU_RMB_PIE_MENUS_OT_looptools_bridge,
            WAZOU_RMB_PIE_MENUS_OT_laprelax]

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


























