import bpy

class WPM_Create_Material(bpy.types.Operator):
    bl_idname = 'object.wpm_create_material'
    bl_label = "Create Material"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return True


    def execute(self, context):
        bpy.context.scene.render.engine = 'CYCLES'

        for obj in bpy.context.selected_objects:
            if bpy.context.object.mode == "EDIT":
                bpy.ops.object.material_slot_add()

            # Create a new material
            material = bpy.data.materials.new(name=obj.name)
            material.use_nodes = True
            material_output = material.node_tree.nodes.get('Material Output')
            # remove diffuse
            diffuse = material.node_tree.nodes['Diffuse BSDF']
            material.node_tree.nodes.remove(diffuse)
            # add Principled
            shader = material.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
            shader.location[0] = 50
            shader.location[1] = 306

            # link shader to material
            material.node_tree.links.new(material_output.inputs[0], shader.outputs[0])
            # set active material to your new material
            obj.active_material = material

            # set_material_color_or_random(self, context)
                # bpy.context.scene.objects.active=obj
            if bpy.context.object.mode == "EDIT":
                bpy.ops.object.material_slot_assign()



        return {'FINISHED'}





