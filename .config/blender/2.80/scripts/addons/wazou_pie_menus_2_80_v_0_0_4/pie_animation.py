import bpy


# Insert Auto Keyframe
class InsertAutoKeyframe(bpy.types.Operator):
    bl_idname = "insert.autokeyframe"
    bl_label = "Insert Auto Keyframe"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if bpy.context.scene.tool_settings.use_keyframe_insert_auto == True:
            bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

        if bpy.context.scene.tool_settings.use_keyframe_insert_auto == False:
            bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        return {'FINISHED'}