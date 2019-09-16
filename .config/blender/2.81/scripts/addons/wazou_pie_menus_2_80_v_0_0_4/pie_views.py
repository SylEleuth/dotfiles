import bpy


# Persp/Ortho
class PerspOrthoView(bpy.types.Operator):
    bl_idname = "persp.orthoview"
    bl_label = "Persp/Ortho"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.view_persportho()
        return {'FINISHED'}


# Lock Camera Transforms
class LockCameraTransforms(bpy.types.Operator):
    bl_idname = "object.lockcameratransforms"
    bl_label = "Lock Camera Transforms"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.object.lock_rotation[0] == False:
            bpy.context.object.lock_rotation[0] = True
            bpy.context.object.lock_rotation[1] = True
            bpy.context.object.lock_rotation[2] = True
            bpy.context.object.lock_location[0] = True
            bpy.context.object.lock_location[1] = True
            bpy.context.object.lock_location[2] = True
            bpy.context.object.lock_scale[0] = True
            bpy.context.object.lock_scale[1] = True
            bpy.context.object.lock_scale[2] = True

        elif bpy.context.object.lock_rotation[0] == True:
            bpy.context.object.lock_rotation[0] = False
            bpy.context.object.lock_rotation[1] = False
            bpy.context.object.lock_rotation[2] = False
            bpy.context.object.lock_location[0] = False
            bpy.context.object.lock_location[1] = False
            bpy.context.object.lock_location[2] = False
            bpy.context.object.lock_scale[0] = False
            bpy.context.object.lock_scale[1] = False
            bpy.context.object.lock_scale[2] = False
        return {'FINISHED'}


# Active Camera
bpy.types.Scene.cameratoto : bpy.props.StringProperty(default="")


class ActiveCameraSelection(bpy.types.Operator):
    bl_idname = "object.activecameraselection"
    bl_label = "Active Camera Selection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.data.objects[context.scene.cameratoto].select = True
        bpy.ops.view3d.object_as_camera()
        return {'FINISHED'}


# Select Camera
class CameraSelection(bpy.types.Operator):
    bl_idname = "object.cameraselection"
    bl_label = "Camera Selection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for cam in bpy.data.cameras:
            bpy.ops.object.select_camera()

        return {'FINISHED'}