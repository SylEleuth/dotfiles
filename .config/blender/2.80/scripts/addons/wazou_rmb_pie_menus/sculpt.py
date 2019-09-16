import bpy
import bmesh
from bpy.props import IntProperty, FloatProperty, BoolProperty
#from bl_ui.properties_paint_common import (
#        UnifiedPaintPanel,
#        brush_texture_settings,
#        brush_texpaint_common,
#        brush_mask_texture_settings,
#        )

class WAZOU_RMB_PIE_MENUS_OT_smooth_sculpt(bpy.types.Operator):
    bl_idname = "object.smooth_sculpt"
    bl_label = "Smooth Sculpt"
    bl_description = "Smooth the mesh while sculpting"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        
        
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.modifier_add(type='SMOOTH')
        bpy.context.object.modifiers["Smooth"].factor = 1
        bpy.context.object.modifiers["Smooth"].iterations = 2
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Smooth")

        bpy.ops.sculpt.sculptmode_toggle()
        if bpy.context.sculpt_object.use_dynamic_topology_sculpting :
            pass
        else :
            bpy.ops.enable.dyntopo()
        bpy.ops.sculpt.optimize()
        
        return {"FINISHED"}
    
#Symetry Lock Y
class WAZOU_RMB_PIE_MENUS_OT_symetry_lock_y(bpy.types.Operator):
    bl_idname = "object.symetrylocky"
    bl_label = "Symetry Lock Y"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        if bpy.context.scene.tool_settings.sculpt.use_symmetry_y == True:
            bpy.context.scene.tool_settings.sculpt.use_symmetry_y = False
        elif bpy.context.scene.tool_settings.sculpt.use_symmetry_y == False:
            bpy.context.scene.tool_settings.sculpt.use_symmetry_y = True   
        return {'FINISHED'}
    
#Symetry Lock Z
class WAZOU_RMB_PIE_MENUS_OT_symetry_lock_z(bpy.types.Operator):
    bl_idname = "object.symetrylockz"
    bl_label = "Symetry Lock Z"
    bl_options = {'REGISTER', 'UNDO'}
    

    def execute(self, context):
        if bpy.context.scene.tool_settings.sculpt.use_symmetry_z == True:
            bpy.context.scene.tool_settings.sculpt.use_symmetry_z = False
        elif bpy.context.scene.tool_settings.sculpt.use_symmetry_z == False:
            bpy.context.scene.tool_settings.sculpt.use_symmetry_z = True   
        return {'FINISHED'}   
     
#Dyntopo Shading
class WAZOU_RMB_PIE_MENUS_OT_dyntopo_smooth_shading(bpy.types.Operator):
    bl_idname = "object.dtpsmoothshading"
    bl_label = "Dyntopo Smooth Shading"
    bl_options = {'REGISTER', 'UNDO'}
    

    def execute(self, context):
        if bpy.context.scene.tool_settings.sculpt.use_smooth_shading == True:
            bpy.context.scene.tool_settings.sculpt.use_smooth_shading = False
        elif bpy.context.scene.tool_settings.sculpt.use_smooth_shading == False:
            bpy.context.scene.tool_settings.sculpt.use_smooth_shading = True   
        return {'FINISHED'} 
    
#detail Variable Constant    
class WAZOU_RMB_PIE_MENUS_OT_detail_size_variable(bpy.types.Operator):
    bl_idname = "object.detailsizevariable"
    bl_label = "Detail Size Variable"
    bl_options = {'REGISTER', 'UNDO'}
    variable : bpy.props.FloatProperty()

    def execute(self, context):
        bpy.context.scene.tool_settings.sculpt.constant_detail = self.variable
        return {'FINISHED'}  
    
#Detail Variable Relative         
class  WAZOU_RMB_PIE_MENUS_OT_detail_size_variable_relative(bpy.types.Operator):
    bl_idname = "object.detailsizevariablerelative"
    bl_label = "Detail Size Variable  Relative"
    bl_options = {'REGISTER', 'UNDO'}
    variable : bpy.props.FloatProperty()

    def execute(self, context):
        bpy.context.scene.tool_settings.sculpt.detail_size = self.variable
        return {'FINISHED'} 
    
#Detail Type    
class WAZOU_RMB_PIE_MENUS_OT_detail_type(bpy.types.Operator):
    bl_idname = "object.detailtype"
    bl_label = "Detail Type"
    bl_options = {'REGISTER', 'UNDO'}
    variable : bpy.props.StringProperty()

    def execute(self, context):
        bpy.context.scene.tool_settings.sculpt.detail_type_method = self.variable
        return {'FINISHED'} 
    
#Detail Refine
class WAZOU_RMB_PIE_MENUS_OT_detail_refine(bpy.types.Operator):
    bl_idname = "object.detailrefine"
    bl_label = "Detail Refine"
    bl_options = {'REGISTER', 'UNDO'}
    variable : bpy.props.StringProperty()

    def execute(self, context):
        bpy.context.scene.tool_settings.sculpt.detail_refine_method = self.variable
        return {'FINISHED'} 

#Enable Dyntopo
class WAZOU_RMB_PIE_MENUS_OT_enable_dyntopo(bpy.types.Operator):
    bl_idname = "enable.dyntopo"  
    bl_label = "Enable Dyntopo" 
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.sculpt.dynamic_topology_toggle()
        bpy.context.scene.tool_settings.sculpt.detail_refine_method = 'SUBDIVIDE_COLLAPSE'
        bpy.context.scene.tool_settings.sculpt.detail_type_method = 'CONSTANT'
        bpy.context.scene.tool_settings.sculpt.use_smooth_shading = True
        return {'FINISHED'} 

#Sculpt Symmetrize +X to -X
class WAZOU_RMB_PIE_MENUS_OT_sculpt_symmetrize_plus_x(bpy.types.Operator):
    bl_idname = "sculpt.symmetrizeplusx"  
    bl_label = "Sculpt Symmetrize +X to -X" 
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.sculpt.symmetrize()
        if bpy.context.scene.tool_settings.sculpt.symmetrize_direction ==  'NEGATIVE_X' :
            bpy.context.scene.tool_settings.sculpt.symmetrize_direction = 'POSITIVE_X'
        return {'FINISHED'}     

#Sculpt Symmetrize -X to +X
class WAZOU_RMB_PIE_MENUS_OT_sculpt_symmetrize_moins_x(bpy.types.Operator):
    bl_idname = "sculpt.symmetrizemoinsx"  
    bl_label = "Sculpt Symmetrize - X to + X" 
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.sculpt.symmetrize()
        if bpy.context.scene.tool_settings.sculpt.symmetrize_direction ==  'POSITIVE_X' :
            bpy.context.scene.tool_settings.sculpt.symmetrize_direction = 'NEGATIVE_X'
        return {'FINISHED'} 

#Sculpt Use symetry X
class WAZOU_RMB_PIE_MENUS_OT_sculpt_use_symmetry_x(bpy.types.Operator):
    bl_idname = "sculpt.sculptusesymmetryx"  
    bl_label = "Sculpt Use symetry X" 
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        if bpy.context.scene.tool_settings.sculpt.use_symmetry_x == (True):
            bpy.context.scene.tool_settings.sculpt.use_symmetry_x = False
            
        elif bpy.context.scene.tool_settings.sculpt.use_symmetry_x == (False) :
             bpy.context.scene.tool_settings.sculpt.use_symmetry_x = True
        return {'FINISHED'}     

#Sculpt Use symetry Y
class WAZOU_RMB_PIE_MENUS_OT_sculpt_usesymmetry_y(bpy.types.Operator):
    bl_idname = "sculpt.sculptusesymmetryy"  
    bl_label = "Sculpt Use symetry Y" 
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        if bpy.context.scene.tool_settings.sculpt.use_symmetry_y == (True):
            bpy.context.scene.tool_settings.sculpt.use_symmetry_y = False
            
        elif bpy.context.scene.tool_settings.sculpt.use_symmetry_y == (False) :
             bpy.context.scene.tool_settings.sculpt.use_symmetry_y = True
        return {'FINISHED'}     

#Sculpt Use symetry Z
class WAZOU_RMB_PIE_MENUS_OT_sculpt_use_symmetry_z(bpy.types.Operator):
    bl_idname = "sculpt.sculptusesymmetryz"  
    bl_label = "Sculpt Use symetry Z" 
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        if bpy.context.scene.tool_settings.sculpt.use_symmetry_z == (True):
            bpy.context.scene.tool_settings.sculpt.use_symmetry_z = False
            
        elif bpy.context.scene.tool_settings.sculpt.use_symmetry_z == (False) :
             bpy.context.scene.tool_settings.sculpt.use_symmetry_z = True
        return {'FINISHED'} 

CLASSES =  [WAZOU_RMB_PIE_MENUS_OT_smooth_sculpt,
            WAZOU_RMB_PIE_MENUS_OT_symetry_lock_y,
            WAZOU_RMB_PIE_MENUS_OT_symetry_lock_z,
            WAZOU_RMB_PIE_MENUS_OT_dyntopo_smooth_shading,
            WAZOU_RMB_PIE_MENUS_OT_detail_size_variable,
            WAZOU_RMB_PIE_MENUS_OT_detail_size_variable_relative,
            WAZOU_RMB_PIE_MENUS_OT_detail_type,
            WAZOU_RMB_PIE_MENUS_OT_detail_refine,
            WAZOU_RMB_PIE_MENUS_OT_enable_dyntopo,
            WAZOU_RMB_PIE_MENUS_OT_sculpt_symmetrize_plus_x,
            WAZOU_RMB_PIE_MENUS_OT_sculpt_symmetrize_moins_x,
            WAZOU_RMB_PIE_MENUS_OT_sculpt_use_symmetry_x,
            WAZOU_RMB_PIE_MENUS_OT_sculpt_usesymmetry_y,
            WAZOU_RMB_PIE_MENUS_OT_sculpt_use_symmetry_z]

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
    