'''
Copyright (C) 2016 YOUR NAME
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
    "name": "Wazou's Pie Menus 2.80",
    "description": "Pie Menus for blender",
    "author": "Cedric Lepiller",
    "version": (0, 0, 4),
    "blender": (2, 80, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "3D View" }



##################################
# Import des modules
##################################
import bpy
import rna_keymap_ui
from bpy.props import (StringProperty,
                       BoolProperty,
                       FloatVectorProperty,
                       FloatProperty,
                       EnumProperty,
                       IntProperty,
                       PointerProperty)

if "bpy" in locals():
    import importlib
    reloadable_modules = [
        "ui",
        "pie_modes",
        "pie_snapping",
        "pie_active_tools",
        "pie_align",
        "pie_pivot_origin",
        "pie_apply_transforms",
        "pie_areas",
        "pie_delete",
        "pie_selection",

    ]
    for module in reloadable_modules:
        if module in locals():
            importlib.reload(locals()[module])

from . import ( ui,
                pie_modes,
                pie_snapping,
                pie_active_tools,
                pie_align,
                pie_pivot_origin,
                pie_apply_transforms,
                pie_areas,
                pie_delete,
                pie_selection,
               )


keymaps_items_dict = {  "Modes Pie Menu":['wm.call_menu_pie', 'WAZOU_PIE_MENUS_MT_modes',
                                      'Object Non-modal', 'EMPTY', 'WINDOW',
                                       'TAB', 'PRESS', False, False, False
                                      ],

                        "Snapping Pie Menu":['wm.call_menu_pie', 'WAZOU_PIE_MENUS_MT_snapping',
                                      '3D View', 'VIEW_3D', 'WINDOW',
                                       'TAB', 'PRESS', False, True, False
                                      ],

                        "Active Tools Pie Menu":['wm.call_menu_pie', 'WAZOU_PIE_MENUS_MT_active_tools',
                                      '3D View', 'VIEW_3D', 'WINDOW',
                                       'C', 'PRESS', False, False, False
                                      ],

                        "Align Pie Menu":['wm.call_menu_pie', 'WAZOU_PIE_MENUS_MT_align',
                                      '3D View', 'VIEW_3D', 'WINDOW',
                                       'X', 'PRESS', False, False, True
                                      ],

                        "Pivot/Origin Pie Menu":['wm.call_menu_pie', 'WAZOU_PIE_MENUS_MT_origin_pivot',
                                      '3D View', 'VIEW_3D', 'WINDOW',
                                       'S', 'PRESS', False, True, False
                                      ],

                        "Apply/Clear transforms Pie Menu":['wm.call_menu_pie', 'WAZOU_PIE_MENUS_MT_apply_clear_transforms',
                                      'Object Mode', 'EMPTY', 'WINDOW',
                                       'A', 'PRESS', True, False, False
                                      ],

                        "Areas Pie Menu":['wm.call_menu_pie', 'WAZOU_PIE_MENUS_MT_area_views',
                                      'Screen', 'EMPTY', 'WINDOW',
                                       'SPACE', 'PRESS', False, False, True
                                      ],

                        "Delete Pie Menu": ['wm.call_menu_pie', 'WAZOU_PIE_MENUS_MT_delete',
                                           'Mesh', 'EMPTY', 'WINDOW',
                                           'X', 'PRESS', False, False, False
                                           ],

                        "Object Mode Selection Pie Menu": ['wm.call_menu_pie', 'WAZOU_PIE_MENUS_MT_selection_object_mode',
                                            'Object Mode', 'EMPTY', 'WINDOW',
                                            'A', 'PRESS', False, False, False
                                            ],

                        "Edit Mode Selection Pie Menu": ['wm.call_menu_pie', 'WAZOU_PIE_MENUS_MT_selection_edit_mode',
                                               'Mesh', 'EMPTY', 'WINDOW',
                                               'A', 'PRESS', False, False, False
                                               ],

                     }
##################################
# Preferences                    #
##################################

class WAZOU_PIE_MENUS_MT_addon_prefs(bpy.types.AddonPreferences):
    bl_idname = __name__

    prefs_tabs: EnumProperty(
        items=(('info', "Info", "NFORMATIONS"),
               # ('options', "Options", "ADDON OPTIONS"),
               ('keymaps', "Keymaps", "CHANGE KEYMAPS"),
               # ('docs', "Doc", "DOCUMENTATION"),
               ('tutorials', 'Tutorials', 'Tutorials'),
               ('addons', "Addons", "Addons"),
               ('links', "Links", "LINKS")),
        default='info')

    def draw(self, context):
        layout = self.layout

        row = layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)

        # Info
        if self.prefs_tabs == 'info':
            box = layout.box()
            split = box.split()
            col = split.column()
            col.separator()
            col.label(text="Wazou's Pie menus is different from official pie menus")
            col.label(text="It's faster, with more possibilities and smart tools")
            col.label(text="The addon is still in development and will change a lot")
            col.label(text="With new pie menus for different parts of Blender")
            col.separator()
            col.label(text="You can activate or disable pie menus and change the keys in the keymap tab")

        # -----------Keymap settings
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
        col.operator(WAZOU_PIE_MENUS_OT_Add_Hotkey.bl_idname, icon='ADD')

    # for operators
    else:
        if km.keymap_items.get(kmi_name):
            col.context_pointer_set('keymap', km)
            rna_keymap_ui.draw_kmi(
                    [], kc, km, km.keymap_items[kmi_name], col, 0)
        else:
            col.label(text=f"No hotkey entry found for {kmi_name}")
            col.operator(WAZOU_PIE_MENUS_OT_Add_Hotkey.bl_idname, icon='ADD')


class WAZOU_PIE_MENUS_OT_Add_Hotkey(bpy.types.Operator):
    ''' Add hotkey entry '''
    bl_idname = "template.add_hotkey"
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
    # In background mode, there's no such thing has keyconfigs.user,
    # because headless mode doesn't need key combos.
    # So, to avoid error message in background mode, we need to check if
    # keyconfigs is loaded.
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

CLASSES = [WAZOU_PIE_MENUS_MT_addon_prefs,
           WAZOU_PIE_MENUS_OT_Add_Hotkey]

# Register
def register():
    ui.register()
    pie_modes.register()
    pie_snapping.register()
    pie_active_tools.register()
    pie_align.register()
    pie_pivot_origin.register()
    pie_apply_transforms.register()
    pie_areas.register()
    pie_delete.register()
    pie_selection.register()

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
    pie_modes.unregister()
    pie_snapping.unregister()
    pie_active_tools.unregister()
    pie_align.unregister()
    pie_pivot_origin.unregister()
    pie_apply_transforms.unregister()
    pie_areas.unregister()
    pie_delete.unregister()
    pie_selection.unregister()


    for cls in CLASSES:
        bpy.utils.unregister_class(cls)


    # hotkey cleanup
    remove_hotkey()


