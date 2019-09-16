import bpy
from math import radians
from bpy.props import (StringProperty, 
                       IntProperty, 
                       FloatProperty,
                       EnumProperty,
                       BoolProperty)
import bgl
import blf


# def draw_callback_rmb_smooth(self, context):
#
#     font_id = 0  # XXX, need to find out how best to get this.
#
#     #Smoothing
#     bgl.glColor4f(1,1,1,1)
#     blf.position(font_id, 80, 350, 0)
#     blf.size(font_id, 30, 72)
#     blf.draw(font_id, "SMOOTHING : " )
#
#     bgl.glColor4f(0.5,1,0,0.7)
#     blf.position(font_id, 300, 350, 0)
#     blf.size(font_id, 40, 72)
#     blf.draw(font_id, str(round(bpy.context.window_manager.operators[-1].factor, 2)))
#
#     #Line
#     bgl.glColor4f(1,1,1,1)
#     blf.position(font_id, 80, 340, 0)
#     blf.size(font_id, 20, 72)
#     blf.draw(font_id, "____________________" )
#
#     #SMOOTHNESS
#     bgl.glColor4f(1,1,1,1)
#     blf.position(font_id, 80, 300, 0)
#     blf.size(font_id, 30, 72)
#     blf.draw(font_id, "REPEAT         : " )
#
#     bgl.glColor4f(0.5,1,0,0.7)
#     blf.position(font_id, 300, 300, 0)
#     blf.size(font_id, 40, 72)
#     blf.draw(font_id, str(round(bpy.context.window_manager.operators[-1].repeat, 2)))
#
#     #Keys
#     bgl.glColor4f(0.5,1,0,0.8)
#     blf.position(font_id, 80, 70, 0)
#     blf.size(font_id, 25, 72)
#     blf.draw(font_id, "DEL/ESC/RMB"  )
#
#     bgl.glColor4f(1,1,1,1)
#     blf.position(font_id, 250, 70, 0)
#     blf.size(font_id, 25, 72)
#     blf.draw(font_id, ": Exit"  )
    
class WAZOU_RMB_PIE_MENUS_OT_modal_smooth(bpy.types.Operator):
    """Move an object with the mouse, example"""
    bl_idname = "object.rmb_modal_smooth"
    bl_label = "Rmb Modal Smooth"

    first_mouse_x : IntProperty()
    first_value : FloatProperty()
    factor : FloatProperty()
    repeat : FloatProperty()
    def modal(self, context, event):
        if event.type == 'MIDDLEMOUSE':
            return {'PASS_THROUGH'} 
            
        if event.type == 'MOUSEMOVE':
            bpy.context.area.tag_redraw()
            
            if event.shift:
                bpy.context.window_manager.operators[-1].repeat = (self.first_mouse_x - event.mouse_x)*-0.005
            else:
                bpy.context.window_manager.operators[-1].factor = (self.first_mouse_x - event.mouse_x)*-0.01
                
            bpy.ops.ed.undo_redo()
            
        elif event.type == 'LEFTMOUSE':
            context.area.header_text_set()
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'FINISHED'}

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            context.area.header_text_set()
            context.object.location.x = self.first_value
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.object:
            
            bpy.ops.mesh.vertices_smooth(True)
            
            self.first_mouse_x = event.mouse_x
            
            #Text in BGL
            # args = (self, context)
            # self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_rmb_smooth, args, 'WINDOW', 'POST_PIXEL')
            
            #Textx in the Header
            context.area.header_text_set("Click: Smooth, Shift+Click: Repeat") 
            
            self.factor = bpy.context.window_manager.operators[-1].factor
            self.repeat = bpy.context.window_manager.operators[-1].repeat
            
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "No active object, could not finish")
            return {'CANCELLED'}


# def draw_callback_rmb_subdivide(self, context):
#
#     font_id = 0  # XXX, need to find out how best to get this.
#
#     #SUBDIVISIONS
#     bgl.glColor4f(1,1,1,1)
#     blf.position(font_id, 80, 350, 0)
#     blf.size(font_id, 30, 72)
#     blf.draw(font_id, "SUBDIVISIONS : " )
#
#     bgl.glColor4f(0.5,1,0,0.7)
#     blf.position(font_id, 330, 350, 0)
#     blf.size(font_id, 40, 72)
#     blf.draw(font_id, str(round(bpy.context.window_manager.operators[-1].number_cuts, 2)))
#
#     #Line
#     bgl.glColor4f(1,1,1,1)
#     blf.position(font_id, 80, 340, 0)
#     blf.size(font_id, 20, 72)
#     blf.draw(font_id, "_______________________" )
#
#     #SMOOTHNESS
#     bgl.glColor4f(1,1,1,1)
#     blf.position(font_id, 80, 300, 0)
#     blf.size(font_id, 30, 72)
#     blf.draw(font_id, "SMOOTHNESS : " )
#
#     bgl.glColor4f(0.5,1,0,0.7)
#     blf.position(font_id, 330, 300, 0)
#     blf.size(font_id, 40, 72)
#     blf.draw(font_id, str(round(bpy.context.window_manager.operators[-1].smoothness, 2)))
#
#     #Line
#     bgl.glColor4f(1,1,1,1)
#     blf.position(font_id, 80, 290, 0)
#     blf.size(font_id, 20, 72)
#     blf.draw(font_id, "_______________________" )
#
#     #SUBDIVISIONS
#     bgl.glColor4f(1,1,1,1)
#     blf.position(font_id, 80, 250, 0)
#     blf.size(font_id, 30, 72)
#     blf.draw(font_id, "FRACTAL          : " )
#
#     bgl.glColor4f(0.5,1,0,0.7)
#     blf.position(font_id, 330, 250, 0)
#     blf.size(font_id, 40, 72)
#     blf.draw(font_id, str(round(bpy.context.window_manager.operators[-1].fractal, 2)))
#
#
#
#
#     #Keys
#     bgl.glColor4f(0.5,1,0,0.8)
#     blf.position(font_id, 80, 70, 0)
#     blf.size(font_id, 25, 72)
#     blf.draw(font_id, "DEL/ESC/RMB"  )
#
#     bgl.glColor4f(1,1,1,1)
#     blf.position(font_id, 250, 70, 0)
#     blf.size(font_id, 25, 72)
#     blf.draw(font_id, ": Exit"  )
    
class WAZOU_RMB_PIE_MENUS_OT_modal_subdivide(bpy.types.Operator):
    bl_idname = "object.rmb_modal_subdivide"
    bl_label = "Rmb Modal Subdivide"

    first_mouse_x : IntProperty()
    first_value : FloatProperty()
                               
    def modal(self, context, event):
        if event.type == 'MIDDLEMOUSE':
            return {'PASS_THROUGH'} 
            
        if event.type == 'MOUSEMOVE':
            bpy.context.area.tag_redraw()
            if event.shift:
                bpy.context.window_manager.operators[-1].smoothness = (self.first_mouse_x - event.mouse_x)*-0.001
            elif event.ctrl:
                bpy.context.window_manager.operators[-1].fractal = (self.first_mouse_x - event.mouse_x)*-0.001
            else:
                bpy.context.window_manager.operators[-1].number_cuts = (self.first_mouse_x - event.mouse_x)*-0.02
            bpy.ops.ed.undo_redo()
            
        elif event.type == 'LEFTMOUSE':
            context.area.header_text_set()
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'FINISHED'}

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            context.area.header_text_set()
            context.object.location.x = self.first_value
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.object:
            
            bpy.ops.mesh.subdivide(True)

            self.first_mouse_x = event.mouse_x
            
            #Text in BGL
            # args = (self, context)
            # self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_rmb_subdivide, args, 'WINDOW', 'POST_PIXEL')
            
            #Textx in the Header
            context.area.header_text_set("Click: Subdivide, Shift+Click: Smoothness, Ctrl+Click: Fractal") 

            self.number_cuts = bpy.context.window_manager.operators[-1].number_cuts
            self.smoothness = bpy.context.window_manager.operators[-1].smoothness
            self.fractal = bpy.context.window_manager.operators[-1].fractal
            
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "No active object, could not finish")
            return {'CANCELLED'}

CLASSES =  [WAZOU_RMB_PIE_MENUS_OT_modal_subdivide,
            WAZOU_RMB_PIE_MENUS_OT_modal_smooth]

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