import bpy

class WAZOU_PIE_MENUS_OT_view_selection(bpy.types.Operator):
    """    VIEW SELECTED/ALL

    CLICK - View Selected
    SHIFT - View All"""
    bl_idname = 'wazou_pie_menus.view_selection'
    bl_label = "View Selection"
    bl_options = {'REGISTER'}

    def invoke(self, context, event):
        if event.shift:
            bpy.ops.view3d.view_all()
        else:
            bpy.ops.view3d.view_selected()

        return {'FINISHED'}

class WAZOU_PIE_MENUS_OT_local_view(bpy.types.Operator):
    bl_idname = 'wazou_pie_menus.local_view'
    bl_label = "Local View"
    bl_options = {'REGISTER'}


    def execute(self, context):
        bpy.ops.view3d.localview()
        bpy.ops.view3d.view_all()

        return {'FINISHED'}


# Object Select all
class WAZOU_PIE_MENUS_OT_mesh_selection(bpy.types.Operator):
    """    SELECT/DESELECT

    CLICK - Select Toggle
    SHIFT - Select All visible objects
    CTRL  - Deselect
    ALT    - Invert"""

    bl_idname = 'wazou_pie_menus.mesh_selection'
    bl_label = "Select/Deselect"
    bl_options = {'REGISTER'}


    def invoke(self, context, event):

        if event.shift:
            if context.object.mode == 'EDIT':
                bpy.ops.mesh.select_all(action='SELECT')
            else:
                bpy.ops.object.select_all(action='SELECT')

        elif event.ctrl:
            if context.object.mode == 'EDIT':
                bpy.ops.mesh.select_all(action='DESELECT')
            else:
                bpy.ops.object.select_all(action='DESELECT')

        elif event.alt:
            if context.object.mode == 'EDIT':
                bpy.ops.mesh.select_all(action='INVERT')
            else:
                bpy.ops.object.select_all(action='INVERT')

        else:
            if context.object.mode == 'EDIT':
                bpy.ops.mesh.select_all(action='TOGGLE')
            else:
                bpy.ops.object.select_all(action='TOGGLE')

        return {'FINISHED'}

# SELECT LOOP INNER REGION
class WAZOU_PIE_MENUS_OT_select_loop_inner_region(bpy.types.Operator):
    """    SELECT LOOP INNER REGION

    CLICK - Select
    SHIFT - Invert Selected
    """
    bl_idname = 'wazou_pie_menus.select_loop_inner_region'
    bl_label = ""
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return True

    def invoke(self, context, event):
        if event.shift:
            bpy.ops.mesh.loop_to_region(True, select_bigger=True)

        else:
            bpy.ops.mesh.loop_to_region(True, select_bigger=False)

        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')

        return {'FINISHED'}


# select_hierarchy
def find_child(ob, lst):
    for x in ob.children:
        lst.append(x)
        find_child(x, lst)


def find_parent(ob, lst):
    lst.append(ob)
    if ob.parent:
        find_parent(ob.parent, lst)


class WAZOU_PIE_MENUS_OT_select_hierarchy(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.select_hierarchy"
    bl_label = "sel hierarchy[shs]"
    bl_options = {"UNDO"}

    def execute(self, context):
        lst = []  # list for all objects
        find_parent(bpy.context.object, lst)  # find parent

        if len(lst) > 0:

            last_parent = lst[0]
            for p in lst:
                # parent of everything has no parent itself
                if not p.parent: last_parent = p

            # find children for each parent
            for c in lst: find_child(c, lst)

            # select all
            for x in lst: x.select = True

            # make parent active
            bpy.context.scene.objects.active = last_parent

        #            print(lst)
        bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
        return {'FINISHED'}


# Components Selection Mode
class WAZOU_PIE_MENUS_OT_verts_edges(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.verts_edges"
    bl_label = "Verts Edges"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.context.tool_settings.mesh_select_mode = (True, True, False)
        if bpy.context.object.mode == "EDIT":
            bpy.context.tool_settings.mesh_select_mode = (True, True, False)
            return {'FINISHED'}


class WAZOU_PIE_MENUS_OT_edges_faces(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.edges_faces"
    bl_label = "EdgesFaces"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.context.tool_settings.mesh_select_mode = (False, True, True)
        if bpy.context.object.mode == "EDIT":
            bpy.context.tool_settings.mesh_select_mode = (False, True, True)
            return {'FINISHED'}


class WAZOU_PIE_MENUS_OT_verts_faces(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.verts_faces"
    bl_label = "Verts Faces"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.context.tool_settings.mesh_select_mode = (True, False, True)
        if bpy.context.object.mode == "EDIT":
            bpy.context.tool_settings.mesh_select_mode = (True, False, True)
            return {'FINISHED'}


class WAZOU_PIE_MENUS_OT_verts_edges_faces(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.edges_faces"
    bl_label = "Verts Edges Faces"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.context.tool_settings.mesh_select_mode = (True, True, True)
        if bpy.context.object.mode == "EDIT":
            bpy.context.tool_settings.mesh_select_mode = (True, True, True)
            return {'FINISHED'}


# Select All By Selection
class WAZOU_PIE_MENUS_OT_select_all_by_selection(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.select_all_by_selection"
    bl_label = "Verts Edges Faces"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.select_all(action='TOGGLE')
        bpy.ops.mesh.select_all(action='TOGGLE')
        return {'FINISHED'}


CLASSES =  [WAZOU_PIE_MENUS_OT_view_selection,
            WAZOU_PIE_MENUS_OT_local_view,
            WAZOU_PIE_MENUS_OT_mesh_selection,
            WAZOU_PIE_MENUS_OT_select_loop_inner_region,
            WAZOU_PIE_MENUS_OT_select_hierarchy,
            WAZOU_PIE_MENUS_OT_verts_edges,
            WAZOU_PIE_MENUS_OT_edges_faces,
            WAZOU_PIE_MENUS_OT_verts_faces,
            WAZOU_PIE_MENUS_OT_verts_edges_faces,
            WAZOU_PIE_MENUS_OT_select_all_by_selection]

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