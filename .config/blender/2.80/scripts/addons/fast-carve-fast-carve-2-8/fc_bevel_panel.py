import bpy
from bpy.types import Panel

from . fc_bevel_op import FC_BevelOperator
from . fc_unbevel_op import FC_UnBevelOperator

class FC_PT_Bevel_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Selected objects"
    bl_category = "Fast Carve"
    
    def has_bevel_modifier(self, obj):
        if obj is None:
            return False

        for modifier in obj.modifiers:
            if modifier.type == "BEVEL":
                return True
        return False

    @classmethod
    def poll(cls, context):
        return (context.object is not None)
     
    def draw(self, context):
        
        layout = self.layout
        
        if context.object is not None:
            # Draw type
            row = layout.row()
            row.prop(context.object, "display_type", text="Display As")
                
        # Bevel button
        row = layout.row()
        
        mode = context.object.mode         
         
        row.operator('object.bevel', text=FC_BevelOperator.get_display(context.object.mode), icon='MOD_BEVEL')
                      
        if(mode == "OBJECT"):                

            if self.has_bevel_modifier(context.active_object):
                row = layout.row()
                row.prop(context.object.modifiers["Bevel"], "width", text="Bevel width")
                                
        # Un-Bevel button
        row = layout.row()
        row.operator('object.unbevel', text=FC_UnBevelOperator.get_display(context.object.mode), icon='MOD_BEVEL')   
  
        # Mirror                       
        row = layout.row()
        row.operator('object.mirror', text='Mirror', icon='MOD_MIRROR')

        # Array
        row = layout.row()
        row.operator('object.fc_array_mode_op', text='Array', icon='MOD_ARRAY')

        # Circular Array
        row = layout.row()
        row.operator('object.fc_circle_array_mode_op', text='Circle Array', icon='MOD_ARRAY')

        row = layout.row()
        row.operator('object.union_selected_op', text='Union', icon='MOD_BOOLEAN')
        
        # symmetrize negative
        row = layout.row()
        split = row.split(factor=0.33)
        col = split.column()
        col.operator('object.sym', text="-X", icon='MOD_MESHDEFORM').sym_axis = "NEGATIVE_X"
        
        col = split.column()
        col.operator('object.sym', text="-Y", icon='MOD_MESHDEFORM').sym_axis = "NEGATIVE_Y"
        
        col = split.column()
        col.operator('object.sym', text="-Z", icon='MOD_MESHDEFORM').sym_axis = "NEGATIVE_Z"
        
        # symmetrize positive
        row = layout.row()
        split = row.split(factor=0.33)
        col = split.column()
        col.operator('object.sym', text="X", icon='MOD_MESHDEFORM').sym_axis = "POSITIVE_X"
        
        col = split.column()
        col.operator('object.sym', text="Y", icon='MOD_MESHDEFORM').sym_axis = "POSITIVE_Y"
        
        col = split.column()
        col.operator('object.sym', text="Z", icon='MOD_MESHDEFORM').sym_axis = "POSITIVE_Z"

        row = layout.row()
        #split = row.split(factor=0.5)
        #col = split.column()
        row.operator('view3d.dissolve_edges', text='Dissolve', icon='LINENUMBERS_OFF')

        #col = split.column()
        row = layout.row()
        row.operator('view3d.origin_active', text='Set Origin', icon='PIVOT_CURSOR')

        row = layout.row()
        row.operator('view3d.snap_active', text='Cursor to Active', icon='PIVOT_CURSOR')