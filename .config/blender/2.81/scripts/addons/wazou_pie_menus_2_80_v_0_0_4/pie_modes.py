import bpy


######################
#       Modes        #
######################

# Define Class Texture Paint
class WAZOU_PIE_MENUS_OT_texturePaint(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.texture_paint"
    bl_label = "Mode Texture Paint"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode="OBJECT")
            bpy.ops.paint.texture_paint_toggle()
        else:
            bpy.ops.paint.texture_paint_toggle()
        return {'FINISHED'}

# Define Class Weight Paint
class WAZOU_PIE_MENUS_OT_weightPaint(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.weight_paint"
    bl_label = "Mode Weight Paint"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode="OBJECT")
            bpy.ops.paint.weight_paint_toggle()
        else:
            bpy.ops.paint.weight_paint_toggle()
        return {'FINISHED'}

# Define Class Vertex Paint
class WAZOU_PIE_MENUS_OT_vertexPaint(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.vertex_paint"
    bl_label = "Mode Vertex Paint"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode="OBJECT")
            bpy.ops.paint.vertex_paint_toggle()
        else:
            bpy.ops.paint.vertex_paint_toggle()
        return {'FINISHED'}


# Define Class Particle Edit
class WAZOU_PIE_MENUS_OT_particleEdit(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.particle_edit"
    bl_label = "Mode Particle Edit"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode="OBJECT")
            bpy.ops.particle.particle_edit_toggle()
        else:
            bpy.ops.particle.particle_edit_toggle()

        return {'FINISHED'}

# Define Class Object Mode
class WAZOU_PIE_MENUS_OT_Object(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.object"
    bl_label = "Mode Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode == "OBJECT":
            bpy.ops.object.mode_set(mode="EDIT")
        else:
            bpy.ops.object.mode_set(mode="OBJECT")
        return {'FINISHED'}


# Define Class Vertex
class WAZOU_PIE_MENUS_OT_Vertex(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.vertex"
    bl_label = "Mode Vertex"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
        if bpy.ops.mesh.select_mode != "EDGE, FACE":
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            return {'FINISHED'}


# Define Class Edge
class WAZOU_PIE_MENUS_OT_edge(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.edge"
    bl_label = "Mode Edge"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
        if bpy.ops.mesh.select_mode != "VERT, FACE":
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
            return {'FINISHED'}

# Define Class Face
class WAZOU_PIE_MENUS_OT_face(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.face"
    bl_label = "Mode Face"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
        if bpy.ops.mesh.select_mode != "VERT, EDGE":
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            return {'FINISHED'}



# Define Class Edge
class WAZOU_PIE_MENUS_OT_xray(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.xray"
    bl_label = "Mode Xray"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):

        shading = context.space_data.shading
        shading.show_xray = not shading.show_xray

        return {'FINISHED'}

CLASSES =  [WAZOU_PIE_MENUS_OT_xray,
            WAZOU_PIE_MENUS_OT_face,
            WAZOU_PIE_MENUS_OT_edge,
            WAZOU_PIE_MENUS_OT_Vertex,
            WAZOU_PIE_MENUS_OT_Object,
            WAZOU_PIE_MENUS_OT_particleEdit,
            WAZOU_PIE_MENUS_OT_vertexPaint,
            WAZOU_PIE_MENUS_OT_weightPaint,
            WAZOU_PIE_MENUS_OT_texturePaint
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