import bpy
import os

# External Data
class WAZOU_MT_ExternalData(bpy.types.Menu):
    bl_idname = "WAZOU_MT_ExternalData"
    bl_label = "External Data"

    def draw(self, context):
        layout = self.layout

        layout.operator("file.autopack_toggle", text="Automatically Pack Into .blend")
        layout.separator()
        layout.operator("file.pack_all", text="Pack All Into .blend")
        layout.operator("file.unpack_all", text="Unpack All Into Files")
        layout.separator()
        layout.operator("file.make_paths_relative", text="Make All Paths Relative")
        layout.operator("file.make_paths_absolute", text="Make All Paths Absolute")
        layout.operator("file.report_missing_files", text="Report Missing Files")
        layout.operator("file.find_missing_files", text="Find Missing Files")


# Save Incremental
class FileIncrementalSave(bpy.types.Operator):
    bl_idname = "file.save_incremental"
    bl_label = "Save Incremental"
    bl_options = {"REGISTER"}

    def execute(self, context):
        f_path = bpy.data.filepath
        if f_path.find("_") != -1:
            str_nb = f_path.rpartition("_")[-1].rpartition(".blend")[0]
            int_nb = int(str_nb)
            new_nb = str_nb.replace(str(int_nb), str(int_nb + 1))
            output = f_path.replace(str_nb, new_nb)

            i = 1
            while os.path.isfile(output):
                str_nb = f_path.rpartition("_")[-1].rpartition(".blend")[0]
                i += 1
                new_nb = str_nb.replace(str(int_nb), str(int_nb + i))
                output = f_path.replace(str_nb, new_nb)
        else:
            output = f_path.rpartition(".blend")[0] + "_001" + ".blend"

        bpy.ops.wm.save_as_mainfile(filepath=output)
        self.report({'INFO'}, "File: {0} - Created at: {1}".format(output[len(bpy.path.abspath("//")):],
                                                                   output[:len(bpy.path.abspath("//"))]))

        # bpy.ops.file.auto_save_incremental_modal()
        return {'FINISHED'}