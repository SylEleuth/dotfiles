import bpy


# Sculpt Polish
class SculptPolish(bpy.types.Operator):
    bl_idname = "sculpt.polish"
    bl_label = "Sculpt Polish"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.tool_settings.sculpt.brush = bpy.data.brushes['Polish']
        return {'FINISHED'}

    # Sculpt Polish


class SculptSculptDraw(bpy.types.Operator):
    bl_idname = "sculpt.sculptraw"
    bl_label = "Sculpt SculptDraw"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.tool_settings.sculpt.brush = bpy.data.brushes['SculptDraw']
        return {'FINISHED'}