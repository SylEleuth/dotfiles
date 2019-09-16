# -*- coding: utf-8 -*-﻿

'''
Copyright (C) 2017 YOUR NAME
YOUR@MAIL.com

Created by YOUR NAME

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "Wazou RMB Pie Menu",
    "description": "Lot of usefull tools on the RMB button",
    "author": "Cedric Lepiller, Andreas Strømberg(MergeTool), Andy Davies(fastLoops)",
    "version": (2, 2, 7),
    "blender": (2, 80, 0),
    "location": "View3D",
    "wiki_url": "",
    "category": "Tools" }


import bpy
import rna_keymap_ui
from bpy.props import (StringProperty,
                       BoolProperty,
                       FloatVectorProperty,
                       FloatProperty,
                       EnumProperty,
                       IntProperty)

# from .ui import *
# from .operator import *
# from .functions import *

if "bpy" in locals():
    import importlib
    reloadable_modules = [
        "ui",
        "modals",
        "operator",
        "sculpt",
        "mesh_edge_equalize_operator"
    ]
    for module in reloadable_modules:
        if module in locals():
            importlib.reload(locals()[module])

from . import ( ui,
                modals,
                operator,
                sculpt,
                mesh_edge_equalize_operator
               )

keymaps_items_dict = {  "Wazou RMB Pie Menu":['wm.call_menu_pie', 'WAZOU_RMB_PIE_MENUS_MT_menu',
                                      '3D View Generic', 'VIEW_3D', 'WINDOW',
                                       'RIGHTMOUSE', 'PRESS', False, False, True
                                      ],

                     }

# keymaps_items_dict_rmb = {"3D Cursor":['view3d.cursor3d', None, '3D View '
#                                       'Generic', 'VIEW_3D', 'WINDOW',
#                                       'LEFTMOUSE', 'DOUBLE_CLICK', False, False, True
#                                       ],
#
#                      "RMB Pie Menu":['wm.call_menu_pie', 'pie.rightclicmenu',
#                                       '3D View Generic', 'VIEW_3D', 'WINDOW',
#                                        'ACTIONMOUSE', 'PRESS', False, False, False
#                                       ],
#
#                      "RMB Pie Menu Particles":['wm.call_menu_pie', 'pie.particleparameters',
#                                       '3D View Generic', 'VIEW_3D', 'WINDOW',
#                                        'ACTIONMOUSE', 'PRESS', False, False, True
#                                       ]
#                      }


########################
#      Properties      #               
########################

class WAZOU_RMB_PIE_MENUS_MT_prefs(bpy.types.AddonPreferences):
    bl_idname = __name__

    prefs_tabs: EnumProperty(
        items=(('info', "Info", "NFORMATIONS"),
               ('options', "Options", "ADDON OPTIONS"),
               ('keymaps', "Keymaps", "CHANGE KEYMAPS"),
               # ('docs', "Doc", "DOCUMENTATION"),
               ('tutorials', 'Tutorials', 'Tutorials'),
               ('addons', "Addons", "Addons"),
               ('links', "Links", "LINKS")),
        default='info')

    use_modals : BoolProperty(
            name="Use Modals",
            default=False,
            description="Use Modals, Works only on 2.78.5"
            )
    
    scale_y : FloatProperty(
            name="",
            default=1,
            min=1, max=2
            )
                           
    def draw(self, context):
        layout = self.layout
        
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
        if self.prefs_tabs == 'info':
            box=layout.box() 
            box.label(text="To have all the tools, you need to Activate or install :")
            box.label(text="- Looptools - Offset Edges - Auto Mirror")
            row=box.row(align=True)
            row.label(text="- Mesh Vertex tools")
            row.operator("wm.url_open", text="Link").url = "http://samoloty.wjaworski.pl/scripts-254_p.xml"
            row = box.row(align=True)
            row.label(text="- Set Equal Edges Lengths")
            row.operator("wm.url_open", text="Link").url = "https://github.com/kroopson/blenderedgeequalize/blob/master/mesh_edge_equalize_operator.py"

            box=layout.box() 
            box.label(text="Place your mouse over Buttons to see possibilities")
            box.label(text="You can use Ctrl, Shift, Alt do do multiple operations with one button")
            box.label(text="You can combine keys Ctrl+shift, Shift+Alt etc")
            box.separator()
            box.label(text="PRIMITIVES:")
            box.label(text="Click : Add on the cursor")
            box.label(text="Shift : Add on a selection, if no selection, on the cursor")
            box.label(text="Ctrl  : Add on the mouse, to place is where you want")
            box.label(text="Alt   : Add in Edit mode, you can combine with Shift and Ctrl")
            box.label(text="Blender don't allow editable mesh after moving them, so I added normal primitives")
            box.separator()
            box.label(text="CAMERA:")
            box.label(text="Click : Add on the cursor")
            box.label(text="Shift : Add a Camera and see through with the object selected to turn around selection")
            box.label(text="Ctrl  : Add on the mouse, to place is where you want")
            box.label(text="Alt   : Add a Camera and an empty as Dof object, keep the previous selection active")
            box.separator()
            box.label(text="TRANSFORMS:")
            box.label(text="Click : Apply transforms")
            box.label(text="Shit  : Apply Transforms and keep Origin")
            box.separator()
            box.label(text="PARENT/UNPARENT:")
            box.label(text="Click        : Parent to active Object")
            box.label(text="Ctrl         : Unparent")
            box.label(text="Ctrl + Shift : Unparent and clear transforms")
            box.label(text="Works on parent and Children")
            box.separator()
            box.label(text="SUBSURF:")
            box.label(text="Click                : Add/remove subsurf level 2")
            box.label(text="Shift in Object Mode : Apply subsurf")
            box.label(text="Shift in Edit Mode   : Add and Apply subsurf level 1")
            box.label(text="Ctrl in Edit Mode    : Add and Apply subsurf level 2")
            box.separator()
            box.label(text="SEPARATE:")
            box.label(text="Click : Join or Separate objects by loose parts")
            box.label(text="Shift : Join Object and Remove Double")
            box.label(text="Click in Edit Mode > Duplicate Selection to a new object")
            box.label(text="Ctrl  : Go in Edit mode")
            box.label(text="Shift + Click in Edit Mode : Separate selection to a new object")
            box.label(text="Ctrl  : Go in Edit mode")
            box.label(text="Click : Join or Separate objects by loose parts")
            box.separator()
            box.label(text="MODIFIERS:")
            box.label(text="Click : Apply Modifiers on selection")
            box.label(text="Ctrl  : Remove Modifiers on selection")
            box.separator()
            box.label(text="KNIFE:")
            box.label(text="Click : Enter in Knife too mode")
            box.label(text="Shift : Enter in Knife too mode and cut through")
            box.separator()
            box.label(text="INSERT/POKE:")
            box.label(text="Click : Enter in insert tool")
            box.label(text="Shift : Poke face")
            box.label(text="Ctrl  : Poke and Enter in insert tool")
            box.separator()
            box.label(text="SEAM:")
            box.label(text="Click : Add Seam")
            box.label(text="Ctrl  : Remove Seam")
            box.separator()
            box.label(text="UNWRAP:")
            box.label(text="Click : Add Seam and Unwrap")
            box.label(text="Shift : Smart Uv Project")
            box.label(text="Ctrl  : Follow Active Quad")
            box.label(text="Alt   : Reset Uv's")
            box.separator()
            box.label(text="CIRCLE:")
            box.label(text="Click : Add circle")
            box.label(text="Shift : Add circle with a loop")
            box.label(text="Ctrl  : Individual")
            box.label(text="Alt   : Sudivide")
            box.label(text="You can combine Individual, subdivide and loop on faces")
            box.label(text="You cannot subdivide on several vertices")
            box.separator()
            box.label(text="MERGE:")
            box.label(text="Click: Merge at Center")
            box.label(text="Shift: Merge at First")
            box.label(text="Ctrl: Merge at Last")
            box.label(text="Alt: Merge at Cursor")
            box.label(text="Ctrl + Shift: collapse")
            box.label(text="Ctrl + OSKEY: Use MergeTool from Andreas Strømberg")
            box.label(text="You enter in a modal, Click: continuous merge, Drag and Click: Merge at direction")
            box.separator() 
            box.label(text="CONNECT:")
            box.label(text="Click: Connect")
            box.label(text="Shift: Smart connect, same as the Merge Modal")
            box.label(text="You enter in a modal, Click: Continuous connect, Drag and Click: Connect at direction")
            box.separator() 
            box.label(text="LOOPTOOLS:")
            box.label(text="Click: Looptools")
            box.label(text="Shift: Smart Loops")
            box.separator() 
            box.separator() 
            box.label(text="ALIGN:")
            box.label(text="Click: Align to in X")
            box.label(text="Shift: Align to in Y")
            box.label(text="Ctrl : Align to in Z")
            box.label(text="Alt  : Align to in X,Y,Z")
            box.label(text="This tool apply the transforms")
            box.separator() 
            box.label(text="CURSOR:")
            box.label(text="Click: To Selection")
            box.label(text="Shift: Selection to Cursor")
            box.label(text="Ctrl : Cursor to Center")
            box.label(text="Alt  : Cursor to Active")
            box.label(text="Ctrl + Shift: Cursor to Selected to Object Mode")
            box.label(text="Ctrl + Alt  : Sel to Cursor Offset")
            box.separator() 
            box.label(text="ORIGIN:")
            box.label(text="Click: To Selection")
            box.label(text="Shift: To Cursor")
            box.label(text="Ctrl : Geometry To Origin")
            box.label(text="Alt  : To Geometry")
            box.label(text="Ctrl + Shift: To Center Of Mass")
            box.label(text="Ctrl + Alt  : To Bottom")
            box.separator() 
            box.label(text="Smooth:")
            box.label(text="Click: Normal Smooth in Edit Mode")
            box.label(text="Shift: Use LapRelax")
            # box.operator("wm.url_open", text="Settings for the pie menu").url = "http://pitiwazou.com/screenshots/blender_2017-05-22_16-30-57.jpg"

        if self.prefs_tabs == 'options':
            # box = layout.box()
            # split = box.split()
            # row = box.row(align=True)
            # row.label(text="Use Modals :")
            # row.prop(self, 'use_modals', expand=True, text=" ")
            # row = box.row(align=True)
            # row.label(text="Works only on 2.78.5", icon='ERROR')

            box = layout.box()
            row = box.row(align=True)
            row.label(text="Pie Menus Buttons Scale Y :")
            row.prop(self, 'scale_y', expand=True, text=" ")

            userpref = context.preferences
            view = userpref.view
            row = box.row(align=True)
            row.label(text="Pie Menus Radius :")
            row.prop(view, "pie_menu_radius", expand=True, text=" ")

        # ------KEYMAPS
        if self.prefs_tabs == 'keymaps':
            wm = bpy.context.window_manager
            draw_keymap_items(wm, layout)


        # ------TUTORIALS
        if self.prefs_tabs == 'tutorials':
            box = layout.box()
            box.label(text="Free Tutorials:", icon='COMMUNITY')
            box.operator("wm.url_open", text="Youtube Channel").url = "https://www.youtube.com/user/pitiwazou"
            box.label(text="Paid Tutorials:", icon='HAND')
            box.operator("wm.url_open",
                         text="Sony BSP10 Non - Destructive Workflow").url = "https://gumroad.com/l/sony_bsp10_non_destructive_tutorial"
            box.operator("wm.url_open",
                         text="Non - Destructive Workflow Tutorial 1").url = "https://gumroad.com/l/Non-Destructive_Workflow_Tutorial_1"
            box.operator("wm.url_open",
                         text="Non - Destructive Workflow Tutorial 2").url = "https://gumroad.com/l/Non-Destructive_Workflow_Tutorial_2"
            box.operator("wm.url_open",
                         text="Non - Destructive Workflow Tutorial 3").url = "https://gumroad.com/l/Non-Destructive_Workflow_Tutorial_3"
            box.operator("wm.url_open",
                         text="Hydrant Modeling Tutorial").url = "https://gumroad.com/l/hydrant_modeling_tutorial"
            box.operator("wm.url_open",
                         text="Hydrant Unwrapping Tutorial").url = "https://gumroad.com/l/hydrant_unwrapping_tutorial"
            box.operator("wm.url_open",
                         text="Furry Warfare Plane Modeling Tutorial").url = "https://gumroad.com/l/furry_warfare_plane_modeling_tutorial"

        # ------Addons
        if self.prefs_tabs == 'addons':
            box = layout.box()
            box.operator("wm.url_open", text="Addon's Discord").url = "https://discord.gg/ctQAdbY"
            box.separator()
            box.operator("wm.url_open", text="Asset Management").url = "https://gumroad.com/l/asset_management"
            box.operator("wm.url_open", text="Speedflow").url = "https://gumroad.com/l/speedflow"
            box.operator("wm.url_open", text="SpeedSculpt").url = "https://gumroad.com/l/SpeedSculpt"
            box.operator("wm.url_open", text="SpeedRetopo").url = "https://gumroad.com/l/speedretopo"
            box.operator("wm.url_open", text="Easyref").url = "https://gumroad.com/l/easyref"
            box.operator("wm.url_open", text="RMB Pie Menu").url = "https://gumroad.com/l/wazou_rmb_pie_menu_v2"
            box.operator("wm.url_open", text="Wazou's Pie Menu").url = "https://gumroad.com/l/wazou_pie_menus"
            box.operator("wm.url_open", text="Smart Cursor").url = "https://gumroad.com/l/smart_cursor"
            box.operator("wm.url_open",
                         text="My 2.79 Theme").url = "https://www.dropbox.com/s/x6vcip7n11j5w4e/wazou_2_79_001.xml?dl=0"

        # ------URls
        if self.prefs_tabs == 'links':
            box = layout.box()
            box.label(text="Support me:", icon='HAND')
            box.operator("wm.url_open", text="Patreon").url = "https://www.patreon.com/pitiwazou"
            box.operator("wm.url_open", text="Tipeee").url = "https://www.tipeee.com/blenderlounge"
            box.separator()

            box.label(text="Archipack", icon='BLENDER')
            box.operator("wm.url_open", text="Archi Pack").url = "https://blender-archipack.org"

            box.separator()
            box.label(text="Web:", icon='WORLD')
            box.operator("wm.url_open", text="Pitiwazou.com").url = "http://www.pitiwazou.com/"
            box.separator()
            box.label(text="Youtube:", icon='SEQUENCE')
            box.operator("wm.url_open", text="Youtube - Pitiwazou").url = "https://www.youtube.com/user/pitiwazou"
            box.operator("wm.url_open",
                         text="Youtube - Blenderlounge").url = "https://www.youtube.com/channel/UCaA3_WSE5A0H6YrS1SDfAQw/videos"
            box.separator()
            box.label(text="Social:", icon='USER')
            box.operator("wm.url_open", text="Artstation").url = "https://www.artstation.com/artist/pitiwazou"
            box.operator("wm.url_open", text="Twitter").url = "https://twitter.com/#!/pitiwazou"
            box.operator("wm.url_open",
                         text="Facebook").url = "https://www.facebook.com/Pitiwazou-C%C3%A9dric-Lepiller-120591657966584/"
            box.operator("wm.url_open", text="Google+").url = "https://plus.google.com/u/0/116916824325428422972"
            box.operator("wm.url_open", text="Blenderlounge's Discord").url = "https://discord.gg/MBDphac"


# -----------------------------------------------------------------------------
#    Keymap
# -----------------------------------------------------------------------------
addon_keymaps = []

def draw_keymap_items(wm, layout):
    kc = wm.keyconfigs.user

    for name, items in keymaps_items_dict.items():
        kmi_name, kmi_value, km_name = items[:3]
        box = layout.box()
        split = box.split()
        col = split.column()
        col.label(text=name)
        col.separator()
        km = kc.keymaps[km_name]
        get_hotkey_entry_item(kc, km, kmi_name, kmi_value, col)


def get_hotkey_entry_item(kc, km, kmi_name, kmi_value, col):

    # for menus and pie_menu
    if kmi_value:
        for km_item in km.keymap_items:
            if km_item.idname == kmi_name and km_item.properties.name == kmi_value:
                col.context_pointer_set('keymap', km)
                rna_keymap_ui.draw_kmi([], kc, km, km_item, col, 0)
                return

        col.label(text=f"No hotkey entry found for {kmi_value}")
        col.operator(WAZOU_RMB_PIE_MENUS_OT_Add_Hotkey.bl_idname, icon='ADD')

    # for operators
    else:
        if km.keymap_items.get(kmi_name):
            col.context_pointer_set('keymap', km)
            rna_keymap_ui.draw_kmi(
                    [], kc, km, km.keymap_items[kmi_name], col, 0)
        else:
            col.label(text=f"No hotkey entry found for {kmi_name}")
            col.operator(WAZOU_RMB_PIE_MENUS_OT_Add_Hotkey.bl_idname, icon='ADD')


class WAZOU_RMB_PIE_MENUS_OT_Add_Hotkey(bpy.types.Operator):
    ''' Add hotkey entry '''
    bl_idname = "template_rmb.add_hotkey"
    bl_label = "Add Hotkeys"
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        add_hotkey()

        self.report({'INFO'},
                    "Hotkey added in User Preferences -> Input -> Screen -> Screen (Global)")
        return {'FINISHED'}

def add_hotkey():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if not kc:
        return

    for items in keymaps_items_dict.values():
        kmi_name, kmi_value, km_name, space_type, region_type = items[:5]
        eventType, eventValue, ctrl, shift, alt = items[5:]
        km = kc.keymaps.new(name = km_name, space_type = space_type,
                            region_type=region_type)

        kmi = km.keymap_items.new(kmi_name, eventType,
                                  eventValue, ctrl = ctrl, shift = shift,
                                  alt = alt

                                  )
        if kmi_value:
            kmi.properties.name = kmi_value

        kmi.active = True

    addon_keymaps.append((km, kmi))


def remove_hotkey():
    ''' clears all addon level keymap hotkeys stored in addon_keymaps '''

    kmi_values = [item[1] for item in keymaps_items_dict.values() if item]
    kmi_names = [item[0] for item in keymaps_items_dict.values() if item not in ['wm.call_menu', 'wm.call_menu_pie']]

    for km, kmi in addon_keymaps:
        # remove addon keymap for menu and pie menu
        if hasattr(kmi.properties, 'name'):
            if kmi_values:
                if kmi.properties.name in kmi_values:
                    km.keymap_items.remove(kmi)

        # remove addon_keymap for operators
        else:
            if kmi_names:
                if kmi.name in kmi_names:
                    km.keymap_items.remove(kmi)

    addon_keymaps.clear()

##################################
# register                       #
##################################

CLASSES = [WAZOU_RMB_PIE_MENUS_MT_prefs,
           WAZOU_RMB_PIE_MENUS_OT_Add_Hotkey]

# Register
def register():
    ui.register()
    modals.register()
    operator.register()
    sculpt.register()
    mesh_edge_equalize_operator.register()

    for cls in CLASSES:
        try:
            bpy.utils.register_class(cls)
        except:
            print(f"{cls.__name__} already registred")

    # hotkey setup
    add_hotkey()

# Unregister
def unregister():
    ui.unregister()
    modals.unregister()
    operator.unregister()
    sculpt.unregister()
    mesh_edge_equalize_operator.unregister()


    for cls in CLASSES:
        bpy.utils.unregister_class(cls)


    # hotkey cleanup
    remove_hotkey()

