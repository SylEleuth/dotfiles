import bpy
from bpy.props import (StringProperty, 
                       BoolProperty, 
                       FloatVectorProperty,
                       FloatProperty,
                       EnumProperty,
                       IntProperty)

import os


##------------------------------------------------------  
#
# Funtions
#
##------------------------------------------------------  

def get_addon_preferences():
    addon_name = os.path.basename(os.path.dirname(os.path.abspath(__file__).split("utils")[0]))
    user_preferences = bpy.context.preferences
    addon_prefs = user_preferences.addons[addon_name].preferences
    
    return addon_prefs

