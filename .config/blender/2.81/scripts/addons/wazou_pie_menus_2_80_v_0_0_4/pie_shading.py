import bpy
from bpy.props import (StringProperty,
                       BoolProperty,
                       FloatVectorProperty,
                       FloatProperty,
                       EnumProperty,
                       IntProperty,
                       PointerProperty)
import bmesh

from math import ceil
######################
#      Shading       #
######################

class ShadingVariable(bpy.types.Operator):
    bl_idname = "object.shadingvariable"
    bl_label = "Shading Variable"
    bl_options = {'REGISTER', 'UNDO'}

    variable : bpy.props.StringProperty()

    def execute(self, context):
        bpy.context.space_data.viewport_shade = self.variable
        return {'FINISHED'}


class ShadingSmooth(bpy.types.Operator):
    bl_idname = "shading.smooth"
    bl_label = "Shading Smooth"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.object.mode == "OBJECT":
            bpy.ops.object.shade_smooth()

        elif bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.shade_smooth()
            bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}


class ShadingFlat(bpy.types.Operator):
    bl_idname = "shading.flat"
    bl_label = "Shading Flat"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.object.mode == "OBJECT":
            bpy.ops.object.shade_flat()

        elif bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.shade_flat()
            bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}


# Material List
class MaterialListMenu(bpy.types.Operator):
    bl_idname = "object.material_list_menu"
    bl_label = "Material List"
    bl_options = {"REGISTER"}

    sortElement : bpy.props.StringProperty(
        default=""
    )

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.selected_objects and len(bpy.data.materials)

    def check(self, context):
        return True

    def execute(self, context):
        return {"FINISHED"}

    def invoke(self, context, event):
        if self.sortElement:
            self.materialList = [mat for mat in bpy.data.materials if
                                 mat.name.lower().startswith(self.sortElement.lower())]
        else:
            self.materialList = [mat for mat in bpy.data.materials]
        self.materialCount = len(self.materialList)
        self.maxMaterial = 10
        self.maxColumns = 6
        self.columns = 1
        self.start = 0
        self.steps = 0
        self.end = 0

        # Calcul du nombre de colonne en arrondissant a l'entier superieur (fonction ceil du module math)
        # pour une quantite de ligne maximum de 10 par colonne
        self.colCount = ceil(self.materialCount / self.maxMaterial)

        # Si le nombre de colonne trouve est superieur au nombre maximum de colonne "autorise",
        # on limite le nombre de colonne au miximum de colonne autorise
        # Repartition de la quantite de datas de facon homogene dans les colonnes
        # Definition du premier stop pour changer de colonne
        if self.colCount > self.maxColumns:
            self.columns = self.maxColumns
            self.steps = ceil(self.materialCount / self.maxColumns)
            self.end = self.steps

        # Sinon, le nombre de colonne sera le nombre trouve lors du calcul
        else:
            self.columns = self.colCount
            self.steps = ceil(self.materialCount / self.colCount)
            self.end = self.steps

        dpi_value = bpy.context.user_preferences.system.dpi
        return context.window_manager.invoke_props_dialog(self, width=dpi_value * 3 * self.columns, height=100)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "sortElement", text="Sort Element")
        row = layout.row()

        if self.sortElement:
            col = row.column()
            box = col.box()
            for mat in self.materialList:
                name = mat.name
                try:
                    icon_val = layout.icon(mat)
                except:
                    icon_val = 1
                    print("WARNING [Mat Panel]: Could not get icon value for %s" % name)

                if mat.name.lower().startswith(self.sortElement.lower()):
                    box.operator("object.apply_material", text=name, icon_value=icon_val).mat_to_assign = name

            # on doit reinitialiser self.steps, self.start et self.end
            if self.colCount > self.maxColumns:
                self.steps = ceil(self.materialCount / self.maxColumns)

            else:
                self.steps = ceil(self.materialCount / self.colCount)

            self.start = 0
            self.end = self.steps

        else:
            for i in range(self.columns):
                col = row.column()
                box = col.box()
                for idx in range(self.start, self.end):
                    mat = self.materialList[idx]
                    name = mat.name
                    try:
                        icon_val = layout.icon(mat)
                    except:
                        icon_val = 1
                        print("WARNING [Mat Panel]: Could not get icon value for %s" % name)

                    box.operator("object.apply_material", text=name, icon_value=icon_val).mat_to_assign = name

                self.start += self.steps
                if self.end + self.steps <= self.materialCount:
                    self.end += self.steps
                else:
                    self.end = self.materialCount

            # on doit reinitialiser self.steps, self.start et self.end
            if self.colCount > self.maxColumns:
                self.steps = ceil(self.materialCount / self.maxColumns)

            else:
                self.steps = ceil(self.materialCount / self.colCount)

            self.start = 0
            self.end = self.steps


class ApplyMaterial(bpy.types.Operator):
    bl_idname = "object.apply_material"
    bl_label = "Apply material"

    mat_to_assign : bpy.props.StringProperty(default="")

    def execute(self, context):

        if context.object.mode == 'EDIT':
            obj = context.object
            bm = bmesh.from_edit_mesh(obj.data)

            selected_face = [f for f in bm.faces if
                             f.select]  # si des faces sont sélectionnées, elles sont stockées dans la liste "selected_faces"

            mat_name = [mat.name for mat in bpy.context.object.material_slots if len(
                bpy.context.object.material_slots)]  # pour tout les material_slots, on stock les noms des mat de chaque slots dans la liste "mat_name"

            if self.mat_to_assign in mat_name:  # on test si le nom du mat sélectionné dans le menu est présent dans la liste "mat_name" (donc, si un des slots possède le materiau du même nom). Si oui:
                context.object.active_material_index = mat_name.index(
                    self.mat_to_assign)  # on definit le slot portant le nom du comme comme étant le slot actif
                bpy.ops.object.material_slot_assign()  # on assigne le matériau à la sélection
            else:  # sinon
                bpy.ops.object.material_slot_add()  # on ajout un slot
                bpy.context.object.active_material = bpy.data.materials[
                    self.mat_to_assign]  # on lui assigne le materiau choisi
                bpy.ops.object.material_slot_assign()  # on assigne le matériau à la sélection

            return {'FINISHED'}

        elif context.object.mode == 'OBJECT':

            obj_list = [obj.name for obj in context.selected_objects]

            for obj in obj_list:
                bpy.ops.object.select_all(action='DESELECT')
                bpy.data.objects[obj].select = True
                bpy.context.scene.objects.active = bpy.data.objects[obj]
                bpy.context.object.active_material_index = 0

                if self.mat_to_assign == bpy.data.materials:
                    bpy.context.active_object.active_material = bpy.data.materials[mat_name]

                else:
                    if not len(bpy.context.object.material_slots):
                        bpy.ops.object.material_slot_add()

                    bpy.context.active_object.active_material = bpy.data.materials[self.mat_to_assign]

            for obj in obj_list:
                bpy.data.objects[obj].select = True

            return {'FINISHED'}

######################
#   Object shading   #
######################


#Wire on selected objects
class WireSelectedAll(bpy.types.Operator):
    """    SHOW WIRE

    CLICK - Show/Hide wire
    SHIFT - Show wire
    CTRL  - Hide Wire
    """
    bl_idname = "wire.selectedall"
    bl_label = "Wire Selected All"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def invoke(self, context, event):

        if event.shift:
            for obj in bpy.context.selected_objects:
                bpy.context.scene.objects.active=obj
                obj.show_all_edges = True
                obj.show_wire = True

        elif event.ctrl:
            for obj in bpy.context.selected_objects:
                bpy.context.scene.objects.active=obj
                obj.show_all_edges = False
                obj.show_wire = False

        else:
            for obj in bpy.data.objects:
                if bpy.context.selected_objects:
                    if obj.select:
                        if obj.show_wire:
                            obj.show_all_edges = False
                            obj.show_wire = False
                        else:
                            obj.show_all_edges = True
                            obj.show_wire = True
                elif not bpy.context.selected_objects:
                    if obj.show_wire:
                        obj.show_all_edges = False
                        obj.show_wire = False
                    else:
                        obj.show_all_edges = True
                        obj.show_wire = True
        return {'FINISHED'}


# Overlays
class WAZOU_MT_mesh_display_overlays(bpy.types.Menu):
    bl_idname = "WAZOU_MT_mesh_display_overlays"
    bl_label = "Mesh Display Overlays"
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        layout = self.layout

        with_freestyle = bpy.app.build_options.freestyle

        mesh = context.active_object.data
        scene = context.scene

        split = layout.split()

        col = split.column()
        col.label(text="Overlays:")
        col.prop(mesh, "show_faces", text="Faces")
        col.prop(mesh, "show_edges", text="Edges")
        col.prop(mesh, "show_edge_crease", text="Creases")
        col.prop(mesh, "show_edge_seams", text="Seams")
        layout.prop(mesh, "show_weight")
        col.prop(mesh, "show_edge_sharp", text="Sharp")
        col.prop(mesh, "show_edge_bevel_weight", text="Bevel")
        col.prop(mesh, "show_freestyle_edge_marks", text="Edge Marks")
        col.prop(mesh, "show_freestyle_face_marks", text="Face Marks")

#Grid show/hide with axes
class ToggleGridAxis(bpy.types.Operator):
    bl_idname = "scene.togglegridaxis"
    bl_label = "Toggle Grid and Axis in 3D view"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.space_data.show_axis_y = not bpy.context.space_data.show_axis_y
        bpy.context.space_data.show_axis_x = not bpy.context.space_data.show_axis_x
        bpy.context.space_data.show_floor = not bpy.context.space_data.show_floor
        return {'FINISHED'}