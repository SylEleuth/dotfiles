import bpy
import random
from bpy.props import *
from .functions_general import *


class CW_OT_detect_bake_camera_hold_offsets(bpy.types.Operator):
    bl_idname = "cw_tools.cw_detect_bake_camera_hold_offsets"
    bl_label = "Detect Hold Frames"
    bl_options = {"REGISTER", "UNDO", "INTERNAL"}
    
    
    def execute(self, context):
        data = bpy.data
        context = bpy.context
        scn = context.scene
        ob = context.active_object
        
        scn.frame_set(scn.frame_start)
        
        cam = scn.camera
        cam_name = cam.name
        
        if ob.type != 'MESH' and ob.type != 'CURVE' and ob.type != 'ARMATURE':
            self.report({'ERROR'}, 'Select an Mesh/Armature/Curve object to bake the offsets')
            return {'CANCELLED'}
        
        #set by user defined property or create a new empty
        bake_emp = data.objects.new('Camera Hold Frame Offset Bake', None)
        scn.collection.objects.link(bake_emp)
        bake_emp.location = [0,0,0]
        bake_emp.rotation_euler = [0,0,0]
        bake_emp.scale = [1,1,1]


        for i in range(scn.frame_end-scn.frame_start+1):
            bake_emp.location = [0,0,0]
            bake_emp.rotation_euler = [0,0,0]
            bake_emp.scale = [1,1,1]
            
            #first frame store camera matrix
            if i == 0:
                mat_offset = cam.matrix_world.copy()
                
                neutralize_bake_emp(bake_emp)
                
                if context.object.type == 'MESH' or context.object.type == 'CURVE':
                    prev_ob_coords = store_ob_coords(ob)
                
                if context.object.type == 'ARMATURE':
                    prev_bo_transforms = store_bone_transforms(ob)
            
            
            else:
                #camera has changed so reset camera and reset empty back to neutral
                if scn.camera.name != cam_name:
                    cam = scn.camera
                    cam_name = cam.name
                    mat_offset = cam.matrix_world.copy()
                    
                    neutralize_bake_emp(bake_emp)
                
                
                else:
                    hold_frame = False
                    
                    
                    if context.object.type == 'ARMATURE':
                        
                        #compare previous bone head/tails  and current if same bake the offset
                        hold_frame = compare_bone_transforms(ob, prev_bo_transforms)
                        if hold_frame == True:
                            bake_cam_offset(mat_offset, cam, bake_emp)
                    
                    
                    if context.object.type == 'MESH' or context.object.type == 'CURVE':
                        
                        #compare previous bone head/tails  and current if same bake the offset
                        hold_frame = compare_ob_coords(ob, prev_ob_coords)
                        if hold_frame == True:
                            bake_cam_offset(mat_offset, cam, bake_emp)
                    
                    
                    
                    #not a hold frame so neutralize the bake empty
                    if hold_frame == False:
                        neutralize_bake_emp(bake_emp)
                        mat_offset = cam.matrix_world.copy()
                        
                        if context.object.type == 'ARMATURE':
                            prev_bo_transforms = store_bone_transforms(ob)
                        
                        if context.object.type == 'MESH' or context.object.type == 'CURVE':
                            prev_ob_coords = store_ob_coords(ob)
            
            
            scn.frame_set(scn.frame_current+1)

#        for fc in bake_emp.animation_data.action.fcurves:
#            for kp in fc.keyframe_points:
#                kp.interpolation = 'CONSTANT'
        
        return {'FINISHED'}


class CW_OT_force_bake_camera_hold_offsets(bpy.types.Operator):
    bl_idname = "cw_tools.cw_force_bake_camera_hold_offsets"
    bl_label = "Force Bake Forward Frames"
    bl_options = {"REGISTER", "UNDO", "INTERNAL"}
    
    
    def execute(self, context):
        data = bpy.data
        context = bpy.context
        scn = context.scene
        scn_prop = scn.frm_props
        ob = context.active_object
        
        cam = scn.camera
        cam_name = cam.name
        
        
        mat_offset = cam.matrix_world.copy()
        
        neutralize_bake_emp(ob)
        
        for i in range(scn_prop.force_frame_range):
            scn.frame_set(scn.frame_current+1)
            
            if scn.camera.name != cam_name:
                cam = scn.camera
                cam_name = cam.name
                mat_offset = cam.matrix_world.copy()
                
                neutralize_bake_emp(ob)
            
            else:
                bake_cam_offset(mat_offset, cam, ob)
        
        
#        for fc in bake_emp.animation_data.action.fcurves:
#            for kp in fc.keyframe_points:
#                kp.interpolation = 'CONSTANT'
        
        
        return {'FINISHED'}