
import bpy
from . import auto_load
#from . import subclasses as auto_load

from . util.config_util import keymap_conf


auto_load.init()

bl_info = {
    "name": "zh tools",
    "author": "zhch",
    "blender": (2, 80, 0),
    "location": "3DView",
    "description": "一些小工具",
    "wiki_url": "",
    "tracker_url": "http://www.github.com/",
    "version": ('0', '0', '1'),
    "category": "3D View",
}


    
kmi_defs = (
    # MERGE NODES
    # NWMergeNodes with Ctrl (AUTO).
    ('zh_object.unselect_select', 'NUMPAD_0', 'PRESS', True, False, False,
        (('mode', 'MIX'), ('merge_type', 'AUTO'),), "Merge Nodes (Automatic)"),
    ('zh_object.unselect_select', 'ZERO', 'PRESS', True, False, False,
        (('mode', 'MIX'), ('merge_type', 'AUTO'),), "Merge Nodes (Automatic)"),
)


addon_keymaps = []

def register():
    auto_load.register()



    # 设置快捷键
    wm = bpy.context.window_manager

    for c in keymap_conf:
        km = wm.keyconfigs.addon.keymaps.new(name=c['km']['name'], space_type = c['km']['space_type11'])
        i = c['item']
        kmi = km.keymap_items.new(i['op'], i['key'], i['type'], 
            ctrl=i['ctrl'],shift=i['shift'], alt=i['alt'],
            oskey=i['oskey'])
        if 'prop' in c and 'name' in c['prop']:
            kmi.properties.name = c['prop']['name']
        kmi.active = True
        addon_keymaps.append((km, kmi))


def unregister():
    auto_load.unregister()

    # for clazz in addon_classes:
    #     bpy.utils.unregister_class(clazz)

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

