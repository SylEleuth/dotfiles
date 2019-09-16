# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

# ----------------------------------------------------------
# Author: Cody Winchester (codywinch)
# ----------------------------------------------------------

# ----------------------------------------------
# Define Addon info
# --

bl_info = {
    "name": "NPR Framerate Mixer",
    "author": "Cody Winchester (codywinch)",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "3D View > Object and Properties > Object tab",
    "description": "Tool for Mixing Stepped Framerate Objects with Camera on 1s",
    "warning": "",
    "wiki_url": "",
    "category": "3D View"
    }


if "bpy" in locals():
    import imp
    if "__init__" in locals():
        imp.reload(__init__)
    if "ui" in locals():
        imp.reload(ui)
    if "properties" in locals():
        imp.reload(properties)
    if "operators" in locals():
        imp.reload(operators)

import bpy
from bpy.props import *
from .ui import *
from .properties import *
from .operators import *



classes = (
    CW_OT_detect_bake_camera_hold_offsets,
    CW_OT_force_bake_camera_hold_offsets,
    
    
    FRMScnProperties,
    CW_PT_tools_panel,
)



def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    
    bpy.types.Scene.frm_props = PointerProperty(type=FRMScnProperties)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    
    del bpy.types.Scene.frm_props