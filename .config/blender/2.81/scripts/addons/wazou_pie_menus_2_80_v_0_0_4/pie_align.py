import bpy
from bpy.props import (EnumProperty)

#####################
#    Align To 0     #
#####################


class WAZOU_PIE_MENUS_OT_align(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.align"
    bl_label = "Wazou Align"
    bl_options = {'REGISTER', 'UNDO'}

    align_elements: EnumProperty(
        items=(('x', "X", ""),
               ('y', "EDGE", ""),
               ('z', "FACE", ""),
               ('to_x_0', "To X 0", ""),
               ('to_y_0', "To Y 0", ""),
               ('to_z_0', "To Z 0", ""),
               ('center_x_left', "Center X Left", ""),
               ('center_x_right', "Center X Right", ""),
               ('center_y_front', "Center Y Front", ""),
               ('center_y_back', "Center Y Back", ""),
               ('center_z_top', "Center Z Top", ""),
               ('center_z_bottom', "Center Z Bottom", ""),
               ('active_x', "Active X", ""),
               ('active_y', "Active Y", ""),
               ('active_z', "Active Z", ""),
               ),
        default='x'
    )

    def execute(self, context):
        mode = context.object.mode
        act_obj = context.active_object

        # Align scale to axis
        if self.align_elements in {'x','y','z'}:
            if context.object.mode == 'EDIT':
                if self.align_elements == 'x':
                    bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False))
                elif self.align_elements == 'y':
                    bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False))
                elif self.align_elements == 'z':
                    bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True))

            elif context.object.mode == 'OBJECT':
                if self.align_elements == 'x':
                    bpy.ops.object.align(align_mode='OPT_2', relative_to='OPT_3', align_axis={'X'})
                elif self.align_elements == 'y':
                    bpy.ops.object.align(align_mode='OPT_2', relative_to='OPT_3', align_axis={'Y'})
                elif self.align_elements == 'z':
                    bpy.ops.object.align(align_mode='OPT_2', relative_to='OPT_3', align_axis={'Z'})

        # Align to Axis 0
        if self.align_elements in {'to_x_0', 'to_y_0', 'to_z_0'}:
            saved_location = bpy.context.scene.cursor.location.copy()

            if context.object.mode == 'EDIT':
                for obj in bpy.context.selected_objects:
                    obj.select_set(state=True)
                    context.view_layer.objects.active = obj

                    bpy.ops.object.mode_set(mode='OBJECT')
                    bpy.ops.view3d.snap_cursor_to_active()
                    saved_location_object = bpy.context.scene.cursor.location.copy()
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

                    bpy.ops.object.transform_apply(location=True, rotation=True, scale=False)

                    bpy.context.scene.cursor.location[0] = 0
                    bpy.context.scene.cursor.location[1] = 0
                    bpy.context.scene.cursor.location[2] = 0

                    if self.align_elements == 'to_x_0':
                        for vert in bpy.context.object.data.vertices:
                            if vert.select:
                                vert.co[0] = 0
                    elif self.align_elements == 'to_y_0':
                        for vert in bpy.context.object.data.vertices:
                            if vert.select:
                                vert.co[1] = 0
                    elif self.align_elements == 'to_z_0':
                        for vert in bpy.context.object.data.vertices:
                            if vert.select:
                                vert.co[2] = 0

                    bpy.context.scene.cursor.location = saved_location_object
                    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                    bpy.context.scene.cursor.location = saved_location

            elif context.object.mode == 'OBJECT':
                if self.align_elements == 'to_x_0':
                    bpy.ops.object.align(align_mode='OPT_2', relative_to='OPT_1', align_axis={'X'})
                elif self.align_elements == 'to_y_0':
                    bpy.ops.object.align(align_mode='OPT_2', relative_to='OPT_1', align_axis={'Y'})
                elif self.align_elements == 'to_z_0':
                    bpy.ops.object.align(align_mode='OPT_2', relative_to='OPT_1', align_axis={'Z'})

        # Align to Axis + or - CENTER
        if self.align_elements in {'center_x_left','center_x_right',
                                   'center_y_front','center_y_back',
                                   'center_z_top','center_z_bottom'}:

            if context.object.mode == 'EDIT':
                for obj in bpy.context.selected_objects:
                    obj.select_set(state=True)
                    context.view_layer.objects.active = obj

                    bpy.ops.object.mode_set(mode='OBJECT')

                    # X
                    # if self.align_elements == 'center_x_left':
                    #     count = 0
                    #     axe = 0
                    #     for vert in bpy.context.object.data.vertices:
                    #         if vert.select:
                    #             if count == 0:
                    #                 max = vert.co[axe]
                    #                 count += 1
                    #                 continue
                    #             count += 1
                    #             if vert.co[axe] < max:
                    #                 max = vert.co[axe]
                    #
                    # elif self.align_elements == 'center_x_right':
                    #     count = 0
                    #     axe = 0
                    #     for vert in bpy.context.object.data.vertices:
                    #         if vert.select:
                    #             if count == 0:
                    #                 max = vert.co[axe]
                    #                 count += 1
                    #                 continue
                    #             count += 1
                    #             if vert.co[axe] > max:
                    #                 max = vert.co[axe]
                    # # Y
                    # if self.align_elements == 'center_y_front':
                    #     count = 0
                    #     axe = 0
                    #     for vert in bpy.context.object.data.vertices:
                    #         if vert.select:
                    #             if count == 0:
                    #                 max = vert.co[axe]
                    #                 count += 1
                    #                 continue
                    #             count += 1
                    #             if vert.co[axe] < max:
                    #                 max = vert.co[axe]
                    #
                    # elif self.align_elements == 'center_y_back':
                    #     count = 0
                    #     axe = 1
                    #     for vert in bpy.context.object.data.vertices:
                    #         if vert.select:
                    #             if count == 0:
                    #                 max = vert.co[axe]
                    #                 count += 1
                    #                 continue
                    #             count += 1
                    #             if vert.co[axe] > max:
                    #                 max = vert.co[axe]
                    #
                    # # Z
                    # if self.align_elements == 'center_z_top':
                    #     count = 0
                    #     axe = 2
                    #     for vert in bpy.context.object.data.vertices:
                    #         if vert.select:
                    #             if count == 0:
                    #                 max = vert.co[axe]
                    #                 count += 1
                    #                 continue
                    #             count += 1
                    #             if vert.co[axe] < max:
                    #                 max = vert.co[axe]
                    #
                    # elif self.align_elements == 'center_z_bottom':
                    #     count = 0
                    #     axe = 1
                    #     for vert in bpy.context.object.data.vertices:
                    #         if vert.select:
                    #             if count == 0:
                    #                 max = vert.co[axe]
                    #                 count += 1
                    #                 continue
                    #             count += 1
                    #             if vert.co[axe] > max:
                    #                 max = vert.co[axe]
                    #
                    # bpy.ops.object.mode_set(mode='OBJECT')
                    #
                    # for vert in bpy.context.object.data.vertices:
                    #     if vert.select:
                    #         vert.co[axe] = max

                    count = 0
                    if self.align_elements in {'center_x_left','center_x_right'}:
                        self.axe = 0
                    elif self.align_elements in {'center_y_front','center_y_back'}:
                        self.axe = 1
                    elif self.align_elements in {'center_z_top','center_z_bottom'}:
                        self.axe = 2

                    for vert in bpy.context.object.data.vertices:
                        if vert.select:
                            if count == 0:
                                self.max = vert.co[self.axe]
                                count += 1
                                continue
                            count += 1
                            if self.align_elements in {'center_x_left','center_y_front','center_z_top'}:
                                if vert.co[self.axe] < self.max:
                                    self.max = vert.co[self.axe]
                            elif self.align_elements in {'center_x_right', 'center_y_back','center_z_bottom'}:
                                if vert.co[self.axe] > self.max:
                                    self.max = vert.co[self.axe]

                    bpy.ops.object.mode_set(mode='OBJECT')

                    for vert in bpy.context.object.data.vertices:
                        if vert.select:
                            vert.co[self.axe] = self.max

                # print(self.axe)


            elif context.object.mode == 'OBJECT':
                if self.align_elements == 'center_x_left':
                    bpy.ops.object.align(align_mode='OPT_3', relative_to='OPT_3', align_axis={'X'})
                elif self.align_elements == 'center_x_right':
                    bpy.ops.object.align(align_mode='OPT_1', relative_to='OPT_3', align_axis={'X'})
                elif self.align_elements == 'center_y_front':
                    bpy.ops.object.align(align_mode='OPT_3', relative_to='OPT_3', align_axis={'Y'})
                elif self.align_elements == 'center_y_back':
                    bpy.ops.object.align(align_mode='OPT_1', relative_to='OPT_3', align_axis={'Y'})
                elif self.align_elements == 'center_z_top':
                    bpy.ops.object.align(align_mode='OPT_3', relative_to='OPT_3', align_axis={'Z'})
                elif self.align_elements == 'center_z_bottom':
                    bpy.ops.object.align(align_mode='OPT_1', relative_to='OPT_3', align_axis={'Z'})

        # Align to Axis + or - ACTIVE
        if self.align_elements in {'active_x', 'active_y', 'active_z'}:

            if context.object.mode == 'OBJECT':
                if self.align_elements == 'active_x':
                    bpy.ops.object.align(align_mode='OPT_2', relative_to='OPT_4', align_axis={'X'})
                elif self.align_elements == 'active_y':
                    bpy.ops.object.align(align_mode='OPT_2', relative_to='OPT_4', align_axis={'Y'})
                elif self.align_elements == 'active_z':
                    bpy.ops.object.align(align_mode='OPT_2', relative_to='OPT_4', align_axis={'Z'})

        bpy.ops.object.mode_set(mode=mode)
        act_obj.select_set(state=True)
        context.view_layer.objects.active = act_obj
        return {'FINISHED'}

class WAZOU_PIE_MENUS_OT_clear_cursor_rot_loc(bpy.types.Operator):
    bl_idname = "wazou_pie_menus.cursor_rot_loc"
    bl_label = "Wazou Align Elements"
    bl_options = {'REGISTER', 'UNDO'}

    clear_cursor: EnumProperty(
        items=(('rot', "Rotation", ""),
               ('loc', "Location", ""),
               ('loc_rot', "Location and Rotation", ""),
               ),
        default='loc'
    )

    def execute(self, context):
        if self.clear_cursor == 'loc':
            bpy.context.scene.cursor.location[0] = \
            bpy.context.scene.cursor.location[1] = \
            bpy.context.scene.cursor.location[2] = 0

        elif self.clear_cursor == 'rot':

            bpy.context.scene.cursor.rotation_euler[0] = \
            bpy.context.scene.cursor.rotation_euler[1] = \
            bpy.context.scene.cursor.rotation_euler[2] = 0

        else:
            bpy.context.scene.cursor.location[0] = \
            bpy.context.scene.cursor.location[1] = \
            bpy.context.scene.cursor.location[2] = 0
            bpy.context.scene.cursor.rotation_euler[0] = \
            bpy.context.scene.cursor.rotation_euler[1] = \
            bpy.context.scene.cursor.rotation_euler[2] = 0

        return {'FINISHED'}


CLASSES =  [WAZOU_PIE_MENUS_OT_align,
            WAZOU_PIE_MENUS_OT_clear_cursor_rot_loc]

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